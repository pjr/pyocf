"""Type representation of elective trigger valid at will (so long as instrument is
valid and outstanding)."""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/types/conversion_triggers/ElectiveConversionAtWillTrigger.sche
# ma.json

from pydantic import Field
from pyocf.primitives.types.conversion_triggers.conversiontrigger import (
    ConversionTrigger,
)
from pyocf.types.conversion_rights.convertibleconversionright import (
    ConvertibleConversionRight,
)
from pyocf.types.conversion_rights.stockclassconversionright import (
    StockClassConversionRight,
)
from pyocf.types.conversion_rights.warrantconversionright import WarrantConversionRight
from typing import Annotated
from typing import Literal
from typing import Optional
from typing import Union


class ElectiveConversionAtWillTrigger(ConversionTrigger):
    """Type representation of elective trigger valid at will (so long as instrument is
    valid and outstanding).
    """

    # Id for this conversion trigger, unique within list of ConversionTriggers in
    # parent convertible issuance's `conversion_triggers` field.
    trigger_id: str
    # Human-friendly nickname to describe the conversion right
    nickname: Optional[str]
    # Long-form description of the trigger
    trigger_description: Optional[str]
    type: Literal["ELECTIVE_AT_WILL"] = "ELECTIVE_AT_WILL"
    # When the conditions of the trigger are met, how does the convertible convert?
    conversion_right: Annotated[
        Union[
            ConvertibleConversionRight,
            WarrantConversionRight,
            StockClassConversionRight,
        ],
        Field(discriminator="type"),
    ]
