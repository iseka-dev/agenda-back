"""Global Configuration file for Tests Suite."""

import pytest
from fastapi.testclient import TestClient

from agenda_back.main import app
from agenda_back.schemas.v1.calendar_event_schemas import (
    CalendarEventCreateRequest,
    CalendarEventSchema,
    CalendarEventsPaginatedResponse,
)
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.schemas.v1.user_schemas import UserSchema

client = TestClient(app)


@pytest.fixture()
def client() -> TestClient:
    client = TestClient(app)
    yield client


@pytest.fixture()
def calendar_event() -> CalendarEventSchema:
    return CalendarEventSchema(
        id="a0866e45-9dd6-4874-b4b2-74efd20e5761",
        start_datetime="2023",
        end_datetime="2023",
        title="Some Title",
        description="Some not necessary description",
        owner=UserSchema(
            id="a0866e45-9dd6-4874-b4b2-74efd20e5872",
            email="some_email@mail.com",
            first_name="Juan",
            last_name="Perez"
        ),
        attendees=[UserSchema(
            id="a0866e45-9dd6-4874-b4b2-74efd20e5872",
            email="some_email@mail.com",
            first_name="Juan",
            last_name="Perez"
        )]
    )


@pytest.fixture()
def calendar_events_data() -> CalendarEventsPaginatedResponse:
    return CalendarEventsPaginatedResponse(
        calendar_events=[{
            "id": "a0866e45-9dd6-4874-b4b2-74efd20e5761",
            "start_datetime": "2023",
            "end_datetime": "2023",
            "title": "Event Title",
            "description": "Some event description"
        }],
        total_count=1
    )


@pytest.fixture()
def calendar_event_create_data() -> CalendarEventCreateRequest:
    return {
        "start_datetime": "2023",
        "end_datetime": "2023",
        "title": "Event Title",
        "description": "Some event description"
    }


@pytest.fixture()
def id_uuid_data() -> IdOnlyResponse:
    return IdOnlyResponse(id="a0866e45-9dd6-4874-b4b2-74efd20e5761")


@pytest.fixture()
def id_uuid_string() -> str:
    return "a0866e45-9dd6-4874-b4b2-74efd20e5761"
