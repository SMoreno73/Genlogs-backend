from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.routes.search import router as search_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API para buscar carriers segun ciudad origen y destino.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={
            "detail": "Invalid request body. Both 'from' and 'to' fields are required.",
            "errors": exc.errors(),
        },
    )


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Carrier search API is running."}


app.include_router(search_router)
