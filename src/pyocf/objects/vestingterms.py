"""Object describing the terms under which a security vests"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/objects/VestingTerms.schema.json

from pyocf.enums.allocationtype import AllocationType
from pyocf.primitives.objects.object import Object
from pyocf.types.vesting.vestingcondition import VestingCondition
from typing import Literal
from typing import Optional


class VestingTerms(Object):
    """Object describing the terms under which a security vests"""

    object_type: Literal["VESTING_TERMS"] = "VESTING_TERMS"
    # Concise name for the vesting schedule
    name: str
    # Detailed description of the vesting schedule
    description: str
    # Allocation/rounding type for the vesting schedule
    allocation_type: AllocationType
    # Conditions and triggers that describe the graph of vesting schedules and events
    vesting_conditions: list[VestingCondition]
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
