from datetime import datetime
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Location(CamelCaseModel):
    countries: Optional[List[str]] = Field(
        None,
        title="Countries",
        description="Country codes of the location as the numeric codes according to ISO 3166",
        examples=["FI"],
    )
    regions: Optional[List[str]] = Field(
        None,
        title="Regions",
        description="The numeric codes according to Statistics Finland's classification of Regions 2022 are used as the code for the region data",
        examples=["09"],
    )
    municipalities: Optional[List[str]] = Field(
        None,
        title="Municipalities",
        description="The code of the municipality of location data is the numerical codes of municipalities according to Statistics Finland's municipalities 2022 classification",
        examples=["405"],
    )


class Requirement(CamelCaseModel):
    occupations: Optional[List[str]] = Field(
        None,
        title="Occupations",
        description="Professions being sought. The occupation codes used are in an URL format according to ESCO 1.1.0",
        examples=[
            "http://data.europa.eu/esco/occupation/8d3e8aaa-791b-4c75-a465-f3f827028f50"
        ],
    )
    skills: Optional[List[str]] = Field(
        None,
        title="Skills",
        description="Areas of expertise being sought. The codes for skills are in an URL format according to ESCO 1.1.0",
        examples=[
            "http://data.europa.eu/esco/skill/a17286c5-238d-4f0b-bc24-29e9121345de"
        ],
    )


class Paging(CamelCaseModel):
    limit: Optional[int] = Field(None, title="Limit", description="Paging limit")
    offset: Optional[int] = Field(None, title="Offset", description="Paging offset")


class JobLocation(CamelCaseModel):
    municipality: str = Field(
        ...,
        title="Municipality",
        description="The code of the municipality according to Statistics Finland's municipalities 2022 classification",
    )
    postcode: Optional[str] = Field(
        None,
        title="Postal code",
        description="Postal code of the location",
    )


class BasicInfo(CamelCaseModel):
    title: str = Field(
        ...,
        title="Title",
        description="Title of the job posting",
    )
    description: str = Field(
        ...,
        title="Description",
        description="Short description about the job",
    )
    work_time_type: Optional[str] = Field(
        None,
        title="Work time type",
        description="<pre>01 = Full time\n02 = Part time</pre>",
        examples="01",
    )


class JobPostingRequest(CamelCaseModel):
    query: Optional[str] = Field(
        None,
        title="Search query",
        description="Comma separated list of query keywords to search for",
    )
    location: Optional[Location] = Field(
        None, title="Location", description="Location to search jobs in"
    )
    requirements: Optional[Requirement] = Field(
        None,
        title="Requirements",
        description="Requirements for the job posting",
        examples="http://data.europa.eu/esco/occupation/8d3e8aaa-791b-4c75-a465-f3f827028f50",
    )
    paging: Optional[Paging] = Field(
        None,
        title="Paging",
        description="Paging for query",
    )


class JobPosting(CamelCaseModel):
    employer: str = Field(
        ...,
        title="Employer",
        description="Employer name",
    )
    location: JobLocation = Field(
        ..., title="Location", description="Job posting location"
    )
    basic_info: BasicInfo = Field(
        ...,
        title="Basic information",
        description="Basic information about job posting",
    )
    published_at: datetime = Field(
        ..., title="Published at", description="Published at"
    )
    application_end_date: Optional[datetime] = Field(
        None, title="Application end date", description="Last date to apply for the job"
    )
    application_url: Optional[str] = Field(
        None, title="Application URL", description="Link to external application page"
    )


class JobPostingResponse(CamelCaseModel):
    results: List[JobPosting] = Field(
        ..., title="Search results", description="Job postings"
    )
    total_count: int = Field(
        ...,
        title="Total count",
        description="Total count of job postings",
        examples=1,
    )


DEFINITION = DataProductDefinition(
    version="0.0.1",
    title="Job Posting",
    description="Data product for Job Posting",
    request=JobPostingRequest,
    response=JobPostingResponse,
)
