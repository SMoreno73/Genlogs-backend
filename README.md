# Carrier Search API

Backend en FastAPI para simular una API que recibe ciudad origen y destino, y retorna carriers segun reglas definidas en memoria.

## Requisitos

- Python 3.10 o superior

## Instalacion

```bash
pip install -r requirements.txt
```

## Ejecucion

```bash
uvicorn app.main:app --reload
```

## Endpoint principal

- `POST /search`

### Request body

```json
{
  "from": "New York",
  "to": "Washington DC"
}
```

### Ejemplo con curl

```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d "{\"from\": \"New York\", \"to\": \"Washington DC\"}"
```

## Documentacion

- Swagger UI: http://localhost:8000/docs

## Estructura

```bash
app/
 ├── main.py
 ├── routes/
 │   └── search.py
 ├── schemas/
 │   └── search_schema.py
 ├── services/
 │   └── search_service.py
 └── core/
     └── config.py
```
