from pydantic import BaseModel, Field
from typing import Optional

class TelemetryData(BaseModel):
    telemetry_id: str
    country: Optional[str] = None
    version: str
    llm_model: Optional[str] = None
    embedder_model: Optional[str] = None
    system: str

    class Config:
        extra = "ignore"

def parse_telemetry(data: dict) -> TelemetryData:
    telemetry_data = TelemetryData(**data)
    return telemetry_data