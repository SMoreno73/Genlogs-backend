from app.schemas.search_schema import CarrierResponse


def _normalize_city(city: str) -> str:
    return " ".join(city.strip().casefold().split())


RULED_CARRIERS: dict[tuple[str, str], list[CarrierResponse]] = {
    (
        _normalize_city("New York"),
        _normalize_city("Washington DC"),
    ): [
        CarrierResponse(name="Knight-Swift Transport Services", trucks_per_day=10),
        CarrierResponse(name="J.B. Hunt Transport Services Inc", trucks_per_day=7),
        CarrierResponse(name="YRC Worldwide", trucks_per_day=5),
    ],
    (
        _normalize_city("San Francisco"),
        _normalize_city("Los Angeles"),
    ): [
        CarrierResponse(name="XPO Logistics", trucks_per_day=9),
        CarrierResponse(name="Schneider", trucks_per_day=6),
        CarrierResponse(name="Landstar Systems", trucks_per_day=2),
    ],
}


DEFAULT_CARRIERS: list[CarrierResponse] = [
    CarrierResponse(name="UPS Inc.", trucks_per_day=11),
    CarrierResponse(name="FedEx Corp", trucks_per_day=9),
]


def get_carriers(origin: str, destination: str) -> list[CarrierResponse]:
    route_key = (_normalize_city(origin), _normalize_city(destination))
    return RULED_CARRIERS.get(route_key, DEFAULT_CARRIERS)
