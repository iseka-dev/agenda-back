"""Global Configuration file for Tests Suite."""

import pytest
from fastapi.testclient import TestClient

from agenda_back.main import app
from agenda_back.schemas.v1.calendar_event_schemas import CalendarEventSchema
from agenda_back.schemas.v1.common_schemas import IdResponse

client = TestClient(app)


@pytest.fixture()
def client() -> TestClient:
    client = TestClient(app)
    yield client


@pytest.fixture()
def calendar_events_data() -> list:
    return [{
        "id_": "a0866e45-9dd6-4874-b4b2-74efd20e5761",
        "start_datetime": "2023",
        "end_datetime": "2023",
        "title": "Event Title",
        "description": "Some event description"
    }]


@pytest.fixture()
def calendar_event_creation_data() -> CalendarEventSchema:
    return {
        "id_": "a0866e45-9dd6-4874-b4b2-74efd20e5761",
        "start_datetime": "2023",
        "end_datetime": "2023",
        "title": "Event Title",
        "description": "Some event description"
    }


@pytest.fixture()
def id_uuid_data() -> IdResponse:
    return IdResponse(id_="a0866e45-9dd6-4874-b4b2-74efd20e5761")
