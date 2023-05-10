"""Sets forth inputs and conversion mechanism of a convertible note"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/types/conversion_mechanisms/NoteConversionMechanism.schema.jso
# n

from pyocf.enums.accrualperiodtype import AccrualPeriodType
from pyocf.enums.compoundingtype import CompoundingType
from pyocf.enums.daycounttype import DayCountType
from pyocf.enums.interestpayouttype import InterestPayoutType
from pyocf.primitives.types.conversion_mechanisms.conversionmechanism import (
    ConversionMechanism,
)
from pyocf.types.interestrate import InterestRate
from pyocf.types.monetary import Monetary
from pyocf.types.percentage import Percentage
from pyocf.types.ratio import Ratio
from typing import Literal
from typing import Optional


class NoteConversionMechanism(ConversionMechanism):
    """Sets forth inputs and conversion mechanism of a convertible note"""

    type: Literal["CONVERTIBLE_NOTE_CONVERSION"] = "CONVERTIBLE_NOTE_CONVERSION"
    # Interest rate(s) of the convertible (if applicable)
    interest_rates: list[InterestRate]
    # How many days are there is a given period for calculation purposes?
    day_count_convention: DayCountType
    # How is interest paid out (if at applicable)
    interest_payout: InterestPayoutType
    # What is the period over which interest is calculated?
    interest_accrual_period: AccrualPeriodType
    # What type of interest compounding?
    compounding_type: CompoundingType
    # What is the percentage discount available upon conversion, if applicable?
    # (decimal representation - e.g. 0.125 for 12.5%)
    conversion_discount: Optional[Percentage]
    # What is the valuation cap (if applicable)?
    conversion_valuation_cap: Optional[Monetary]
    # For cash proceeds calculation during a liquidity event.
    exit_multiple: Optional[Ratio]
    # Is this an MFN (Most Favored Nations) flavored Convertible Note?
    conversion_mfn: Optional[bool]
