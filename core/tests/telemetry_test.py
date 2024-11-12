import pytest
import pydantic
from uuid import uuid4

from server.telemetries import parse_telemetry, TelemetryData

def test_uuid4():
    telemetryDict = {
        "telemetry_id": "",
        "country": "test",
        "version": "test",
        "llm_model": "test",
        "embedder_model": "test",
        "system": "test",
    }

    # id blank
    with pytest.raises(pydantic.ValidationError):
        parse_telemetry(telemetryDict)

    # id is a random string
    telemetryDict["telemetry_id"] = "random string"

    with pytest.raises(pydantic.ValidationError):
        parse_telemetry(telemetryDict)

    # id is an uuid4
    uuid4_generated = uuid4()
    telemetryDict["telemetry_id"] = str(uuid4_generated)

    telemetry = parse_telemetry(telemetryDict)
    assert isinstance(telemetry, TelemetryData)
    assert telemetry.telemetry_id == uuid4_generated
