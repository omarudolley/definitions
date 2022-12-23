from datetime import date, datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, constr


class Gender(str, Enum):
    male = "Male"
    female = "Female"
    other = "Other"


class EmploymentType(str, Enum):
    permanent = "permanent"
    temporary = "temporary"
    seasonal = "seasonal"
    summer_job = "summerJob"


class WorkTime(str, Enum):
    day_shift = "01"
    evening_shift = "02"
    night_shift = "03"
    work_in_episodes = "04"
    flexible_hours = "05"
    normal_days = "06"
    weekend_hours = "07"
    work_in_shifts = "08"


class WorkingLanguage(str, Enum):
    finnish = "fi"
    swedish = "sv"
    english = "en"


class Address(CamelCaseModel):
    street_address: Optional[str] = Field(
        None,
        title="Street address",
        description="Street address",
        example="Mannerheimintie 42",
        nullable=True,
    )
    zip_code: Optional[constr(min_length=5, max_length=5)] = Field(
        None,
        title="ZIP code",
        description="ZIP code of the address",
        example="00100",
        nullable=True,
    )
    city: Optional[str] = Field(
        None,
        title="City",
        description="City of the address location",
        example="Helsinki",
        nullable=True,
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        description="Country of the address",
        example="Suomi",
        nullable=True,
    )


class Occupation(CamelCaseModel):
    esco_identifier: Optional[str] = Field(
        None,
        title="Occupation",
        description="Occupation with ESCO URI as identifier",
        nullable=True,
    )
    occupation_class: Optional[str] = Field(
        None, title="Occupation class", description="Class of the occupation"
    )
    name: Optional[str] = Field(
        None,
        title="Occupation name",
        description="Name of the occupation",
        nullable=True,
        example="Farmer",
    )
    industry_sector: Optional[str] = Field(
        None, title="Industry sector", description="", nullable=True, example=""
    )
    work_experience_in_years: Optional[int] = Field(
        None, title="", description="", nullable=True, example=1
    )


class WorkPreferences(CamelCaseModel):
    preferred_location: Optional[str] = Field(
        None,
        title="Preferred location",
        description="List of locations from where the user would like to search for jobs",
        nullable=True,
        example=["405"],
    )
    work_type: Optional[EmploymentType] = Field(
        None,
        title="Type of employment",
        description="Enum value describing the type of employment",
        nullable=True,
    )
    working_hours: Optional[str] = Field(
        None, title="Working Hours", description="", nullable=True, example=""
    )
    working_time: Optional[WorkTime] = Field(
        None, title="Working Time", description="", nullable=True
    )
    working_language: Optional[str] = Field(
        None, title="Working Language", description="", nullable=True, example="fi"
    )
    created: Optional[datetime] = Field(
        None,
        title="Created at timestamp",
        description="Timestamp for when the work preferences were first saved",
        nullable=True,
    )
    modified: Optional[datetime] = Field(
        None,
        title="Modified at timestamp",
        description="Timestamp for when the work preferences were last modified",
        nullable=True,
    )


class ProfileResponse(CamelCaseModel):
    id: UUID = Field(
        title="Id",
        description="uuid formatted string used to identify users",
        example="cf57432e-809e-4353-adbd-9d5c0d733868",
    )
    created: datetime = Field(
        title="Created",
        description="Created at timestamp",
        example="2042-04-23T10:20:30.400",
    )
    modified: datetime = Field(
        title="Modified",
        description="Modified at timestamp",
        example="2042-04-23T10:20:30.400",
    )
    first_name: Optional[str] = Field(
        None,
        title="First name",
        description="First name of the user",
        example="John",
        nullable=True,
    )
    last_name: Optional[str] = Field(
        None,
        title="Last name",
        description="Last name of the user",
        example="Doe",
        nullable=True,
    )
    address: Address = Field(..., title="Address", description="Address of the user")
    date_of_birth: Optional[date] = Field(
        None,
        title="Date of birth",
        description="Date of Birth (date only)",
        example="2000-01-01",
        nullable=True,
    )
    gender: Optional[Gender] = Field(
        None, title="Gender", description="Gender of the user", nullable=True
    )
    country_of_birth_code: Optional[
        constr(min_length=2, max_length=2, to_upper=True)
    ] = Field(
        None,
        title="Country of birth code",
        description="ISO 3166-1 alpha-2 code for country",
        example="FI",
        nullable=True,
    )
    native_language_code: Optional[
        constr(
            min_length=3,
            max_length=3,
            to_lower=True,
        )
    ] = Field(
        None,
        title="Native language code",
        description="ISO 639-3 code for language",
        example="fin",
        nullable=True,
    )
    occupation_code: Optional[str] = Field(
        None,
        title="Occupation code",
        description="Code scheme for occupation. Full set of codes can be found at https://koodistot.suomi.fi/codelist-api/api/v1/coderegistries/jhs/codeschemes/ammatti_1_20100101/codes/",
        example="11122",
        nullable=True,
    )
    occupations: Optional[List[Occupation]] = Field(
        None,
        title="Occupations",
        description="List of occupations user has had",
        nullable=True,
    )
    work_preferences: Optional[WorkPreferences] = Field(
        None, title="Working preferences", description="", nullable=True
    )
    citizenship_code: Optional[
        constr(min_length=2, max_length=2, to_upper=True)
    ] = Field(
        None,
        title="Nationality code",
        description="ISO 3166-1 alpha-2 code for nationality",
        example="FI",
        nullable=True,
    )
    job_titles: List[str] = Field(
        ...,
        title="Job titles",
        description="List of job titles",
        example=["Chef", "Programmer"],
    )
    regions: List[str] = Field(
        ...,
        title="Regions",
        description="List of regions where user would want to search for a job",
        example=["Etelä-Suomi"],
    )


class ProfileRequest(CamelCaseModel):
    ...


DEFINITION = DataProductDefinition(
    description="Data product for basic user profile information",
    request=ProfileRequest,
    response=ProfileResponse,
    route_description="User profile information",
    summary="Basic user profile information",
)
