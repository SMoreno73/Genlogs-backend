# Genlogs-Backend

This is a backend API built with FastAPI to simulate a carrier search service based on an origin city and a destination city.

The project was designed as a simple API with no database, where all business logic is handled in memory using fixed rules. Its purpose is to serve as a base for frontend integrations, technical assessments, or clean backend architecture exercises.

## What this project does

The API receives a `POST /search` request with two fields:

- `from`: origin city
- `to`: destination city

Using that information, the system evaluates predefined rules and returns a list of available carriers along with their estimated daily truck capacity.

## Main features

- Built with Python 3.10+ and FastAPI
- Served with Uvicorn
- Modular layered structure
- Data validation with Pydantic
- CORS enabled for all origins in development mode
- Basic error handling
- In-memory logic, no database required
- Automatic API documentation with Swagger UI

## Business rules

### Case 1

If the origin is `New York` and the destination is `Washington DC`, the response will be:

```json
[
  { "name": "Knight-Swift Transport Services", "trucks_per_day": 10 },
  { "name": "J.B. Hunt Transport Services Inc", "trucks_per_day": 7 },
  { "name": "YRC Worldwide", "trucks_per_day": 5 }
]
```

### Case 2

If the origin is `San Francisco` and the destination is `Los Angeles`, the response will be:

```json
[
  { "name": "XPO Logistics", "trucks_per_day": 9 },
  { "name": "Schneider", "trucks_per_day": 6 },
  { "name": "Landstar Systems", "trucks_per_day": 2 }
]
```

### Default case

Any other city combination returns:

```json
[
  { "name": "UPS Inc.", "trucks_per_day": 11 },
  { "name": "FedEx Corp", "trucks_per_day": 9 }
]
```

## Data normalization

The API normalizes city values before comparing them. This means it:

- Ignores uppercase and lowercase differences
- Removes extra spaces at the beginning and end
- Collapses repeated spaces between words

Equivalent examples:

- `"New York"`
- `"new york"`
- `"  New   York  "`

## Project structure

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

requirements.txt
README.md
```

## File description

- `app/main.py`: initializes FastAPI, configures CORS, registers routes, and handles validation errors.
- `app/routes/search.py`: defines the `POST /search` endpoint.
- `app/schemas/search_schema.py`: contains the Pydantic models for request and response validation.
- `app/services/search_service.py`: implements the business logic and carrier rules.
- `app/core/config.py`: centralizes basic application settings.
- `requirements.txt`: lists project dependencies.

## Requirements

Before running the project, make sure you have installed:

- Python 3.10 or higher
- `pip`

You can verify your Python version with:

```bash
python --version
```

## Installation

1. Clone or download this project.
2. Open the project root directory.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## How to run the project

Once the dependencies are installed, start the server with:

```bash
uvicorn app.main:app --reload
```

### What this command means

- `uvicorn`: ASGI server used to run FastAPI
- `app.main:app`: points to the FastAPI instance named `app` inside `app/main.py`
- `--reload`: automatically reloads the server when code changes are detected

## Available URLs

When the server is running, you can access:

- Base API: [http://localhost:8000](http://localhost:8000)
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Main endpoint

### `POST /search`

Searches for carriers based on origin and destination cities.

### Request body

```json
{
  "from": "New York",
  "to": "Washington"
}
```

### Required fields

- `from`: string, required
- `to`: string, required

### Successful response

HTTP status:

```http
200 OK
```

Example:

```json
[
  { "name": "Knight-Swift Transport Services", "trucks_per_day": 10 },
  { "name": "J.B. Hunt Transport Services Inc", "trucks_per_day": 7 },
  { "name": "YRC Worldwide", "trucks_per_day": 5 }
]
```

## Error handling

If the request body is incomplete or required fields are missing, the API responds with a `400` error.

Invalid request example:

```json
{
  "from": "New York"
}
```

Example error response:

```json
{
  "detail": "Invalid request body. Both 'from' and 'to' fields are required.",
  "errors": [
    {
      "type": "missing",
      "loc": ["body", "to"],
      "msg": "Field required"
    }
  ]
}
```

## Usage examples

### Example 1

```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d "{\"from\": \"New York\", \"to\": \"Washington DC\"}"
```

### Example 2

```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d "{\"from\": \"San Francisco\", \"to\": \"Los Angeles\"}"
```

### Example 3

```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d "{\"from\": \"Miami\", \"to\": \"Orlando\"}"
```

## CORS

The project has CORS enabled for all origins:

```python
allow_origins=["*"]
```

This is useful for development and testing from any frontend. In production, you should restrict the allowed origins.

## Dependencies

The `requirements.txt` file includes:

```txt
fastapi
uvicorn
```

## Technical notes

- No database is used
- No environment variables are required to run it
- Business logic is separated into services for easier maintenance
- Pydantic models provide input and output typing and validation

## Possible future improvements

- Add unit tests with `pytest`
- Add structured logging
- Add environment-based configuration
- Version the API
- Add persistence if the use case grows
