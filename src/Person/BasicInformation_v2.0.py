from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field, constr


class BasicInformationRequest(CamelCaseModel):
    pass


class CitizenshipArea(str, Enum):
    EEA = "EEA"
    NON_EEA = "non-EEA"


class BasicInformationResponse(CamelCaseModel):
    given_name: Optional[str] = Field(
        None,
        title="Given name",
        description="The first name that the person is being called by",
        examples=["John"],
        max_length=250,
    )
    last_name: Optional[str] = Field(
        None,
        title="Last name",
        description="The person's current family name",
        examples=["Doe"],
        max_length=250,
    )
    email: EmailStr = Field(
        ...,
        title="Email",
        description="The person's contact email address",
        examples=["john.doe@test.fi"],
    )
    phone_number: Optional[str] = Field(
        None,
        title="Phone number",
        description="The person's phone number in the international format",
        examples=["+358501234567"],
        max_length=250,
    )
    citizenship_area: Optional[CitizenshipArea] = Field(
        None,
        title="Citizenship Area",
        description="The citizenship area based on his or her native country. "
        "Switzerland is considered as part of the EEA category.",
        examples=[CitizenshipArea.EEA],
    )


DEFINITION = DataProductDefinition(
    version="2.0.0",
    title="Person Basic Information",
    description="A minimal set of basic information of a person",
    request=BasicInformationRequest,
    response=BasicInformationResponse,
    requires_authorization=True,
    requires_consent=True,
)
