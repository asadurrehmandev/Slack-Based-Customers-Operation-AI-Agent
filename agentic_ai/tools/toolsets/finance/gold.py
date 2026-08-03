from typing import Annotated

from pydantic import BaseModel, Field

from . import finance_toolset

GRAMS_IN_TROY_OUNCE = 31.1034768
GRAMS_IN_TOLA = 11.6638038
USD_TO_PKR = 278


class GoldPriceResult(BaseModel):
    gram_price_pkr: float = Field(description="Gold price per gram in PKR")
    tola_price_pkr: float = Field(description="Gold price per tola in PKR")
    total_value: float = Field(
        description="Total price of Gold in PKR."
    )

    def __str__(self):
        return (
            f"""
-----------------------------
    GOLD PRICE BREAKDOWN
-----------------------------
GRAMS PRICE: {self.gram_price_pkr}
TOLA PRICE: {self.tola_price_pkr}
TOTAL VALUE: {self.total_value}
            """
        )


@finance_toolset.tool_plain
def calculate_gold_price(
        price: Annotated[
            float,
            Field(gt=0, description="Current gold price")
        ],
        weight: Annotated[
            float,
            Field(description="Gold weight in grams")
        ]
) -> GoldPriceResult:
    """
    Calculate the price of gold weight in grams, tola and total value, Using the currency PKR.
    Function returns the price breakdown of gold in Grams, Tola and Total Value

    Args:
        price:
            Current gold price.

        weight:
            Gold weights in grams.

    Returns:
        Price in PKR per gram,
        price in PKR per tola,
        and the total value of Gold weight in grams.
    """

    gram_price = (price / GRAMS_IN_TROY_OUNCE) * USD_TO_PKR
    tola_price = gram_price * GRAMS_IN_TOLA

    return GoldPriceResult(
        gram_price_pkr=round(gram_price, 2),
        tola_price_pkr=round(tola_price, 2),
        total_value=round(weight * gram_price, 2)
    )
