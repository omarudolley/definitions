from datetime import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class PopulationResponse(CamelCaseModel):
    description: str = Field(
        "", title="Data description", examples=["Väkiluku, KOKO MAA, 2021"]
    )
    source_name: str = Field("", title="Data source name", examples=["Tilastokeskus"])
    population: int = Field(..., title="The population value", examples=[5548241])
    updated_at: datetime = Field(
        "",
        title="Datetime the data was last updated at",
        description="A datetime in RFC3339 date-time syntax",
        examples=["2022-06-17T11:52:00Z"],
    )


class PopulationRequest(CamelCaseModel):
    city: str = Field(
        "",
        title="City or region",
        description="City or a region name, leaving the field empty selects country's total",
    )
    year: int = Field(2021, title="Year")


DEFINITION = DataProductDefinition(
    version="0.0.1",
    title="Figure for population",
    description="Data Product for population figure",
    request=PopulationRequest,
    response=PopulationResponse,
)
