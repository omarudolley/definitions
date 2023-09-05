from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, HttpUrl


class AgreementRequest(CamelCaseModel):
    pass


class AgreementResponse(CamelCaseModel):
    terms_of_service_url: HttpUrl = Field(
        ...,
        title="Terms of service URL",
        description="Link to the terms of service",
        example="https://example.com/terms-of-service-v1.0",
    )
    description: str = Field(
        ...,
        title="Description",
        description="Description of the terms of service",
        example="This is the terms of service for the example service",
    )
    version: str = Field(
        ...,
        title="Version",
        description="Version of the terms of service",
        example="1.0",
    )
    accepted: bool = Field(
        ...,
        title="Accepted",
        description="Whether the user has accepted the terms of service",
        example=False,
    )
    accepted_at: Optional[datetime] = Field(
        None,
        title="Datetime the terms of service was accepted at",
        description="A datetime in RFC3339 date-time syntax",
        example="2022-06-17T11:52:00Z",
        nullable=True,
    )
    accepted_previous_version: bool = Field(
        ...,
        title="Accepted previous version",
        description="Whether the user has accepted the previous version of the terms of service",
        example=False,
    )


DEFINITION = DataProductDefinition(
    summary="Data product for the user's terms of service agreement",
    request=AgreementRequest,
    response=AgreementResponse,
    route_summary="Retrieve user's terms of service agreement",
    requires_authorization=True,
)
