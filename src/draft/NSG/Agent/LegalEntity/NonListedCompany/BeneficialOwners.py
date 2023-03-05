from enum import Enum
from typing import List

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ShareSeriesClass(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


class Ownerships(CamelCaseModel):
    share_series_class: ShareSeriesClass = Field(
        ...,
        title="Share series class",
        description="The class of the share series that the shareholder owns",
        example=ShareSeriesClass.B,
    )
    quantity: int = Field(
        ...,
        title="Quantity",
        description="The number of shares that the shareholder owns a share series",
        example=20,
    )


class ShareSeries(CamelCaseModel):
    share_series_class: ShareSeriesClass = Field(
        ...,
        title="Share series class",
        description="The type of the share series of a company",
        example=ShareSeriesClass.A,
    )
    number_of_shares: int = Field(
        ...,
        title="Number of shares",
        description="The total number of the shares in the share series class",
        example=1000,
    )
    votes_per_share: int = Field(
        ...,
        title="Votes per share",
        description="The number of votes per share in the share series",
        example=1,
    )


class Shareholders(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The type of the share series of a company",
        example="Lars Lindberg | Company Ltd",
    )
    ownerships: List[Ownerships] = Field(..., title="Ownerships")


class BeneficialOwnersRequest(CamelCaseModel):
    national_identifier: str = Field(
        None,
        title="National identifier",
        description="The national identifier of the non-listed company issued by the trade register in any Nordic "
        "country.",
        example="FIN: 2464491-9 / SWE: 5560125791 / NOR:  923609016",
        max_length=40,
    )


class BeneficialOwnersResponse(CamelCaseModel):
    share_series: List[ShareSeries] = Field(
        ...,
        title="Share series",
        description="The details of the share series of the company",
    )
    share_holders: List[Shareholders] = Field(
        ...,
        title="Share holders",
        description="The list of beneficial owners of the company",
    )
    ownerships: Ownerships = Field(
        ...,
        title="Ownership",
    )


DEFINITION = DataProductDefinition(
    description="The list of shareholders of a non-listed company",
    request=BeneficialOwnersRequest,
    response=BeneficialOwnersResponse,
    summary="Non-listed Company Beneficial Owners",
    requires_authorization=True,
    requires_consent=True,
)
