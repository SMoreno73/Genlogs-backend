from pydantic import BaseModel, ConfigDict, Field, field_validator


class SearchRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True, str_strip_whitespace=True)

    origin: str = Field(..., alias="from", min_length=1, description="Origin city")
    destination: str = Field(..., alias="to", min_length=1, description="Destination city")

    @field_validator("origin", "destination")
    @classmethod
    def validate_city(cls, value: str) -> str:
        cleaned_value = " ".join(value.split())
        if not cleaned_value:
            raise ValueError("City value cannot be empty.")
        return cleaned_value


class CarrierResponse(BaseModel):
    name: str
    trucks_per_day: int
