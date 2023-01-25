from datetime import datetime
from enum import Enum

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class StatusInfoValue(str, Enum):
    SENT = ("SENT",)
    PROCESSING = ("PROCESSING",)
    WAITING_FOR_COMPLETION = ("WAITING_FOR_COMPLETION",)
    READY = ("READY",)


class StatusInfoResponse(CamelCaseModel):
    status_name: str = Field(
        ...,
        title="Name of the status",
        description="Programmic identity field of the status",
        example="tax_form",
    )
    status_value: StatusInfoValue = Field(
        ...,
        title="Status",
        description="Value of the status",
        example=StatusInfoValue.SENT,
    )
    updated_at: datetime = Field(
        ...,
        title="Datetime the data was last updated at",
        description="A datetime in RFC3339 date-time syntax",
        example="2022-06-17T11:52:00Z",
    )


class StatusInfoRequest(CamelCaseModel):
    status_name: str = Field(
        ...,
        title="Name of the status",
        description="The name of the status to retrieve",
    )


DEFINITION = DataProductDefinition(
    summary="Data product for users status information",
    request=StatusInfoRequest,
    response=StatusInfoResponse,
    route_summary="Retrieve users status information",
    requires_authorization=True,
)
