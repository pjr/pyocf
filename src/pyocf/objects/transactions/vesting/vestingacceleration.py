"""Object describing an acceleration of vesting, in which additional shares vest"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/objects/transactions/vesting/VestingAcceleration.schema.json

from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from pyocf.types.numeric import Numeric
from typing import Literal
from typing import Optional


class VestingAcceleration(Object, Transaction, SecurityTransaction):
    """Object describing an acceleration of vesting, in which additional shares vest
    ahead of the schedule specified in security's vesting terms.
    """

    object_type: Literal["TX_VESTING_ACCELERATION"] = "TX_VESTING_ACCELERATION"
    # Number of shares vesting ahead of schedule
    quantity: Numeric
    # Reason for the acceleration; unstructured text
    reason_text: str
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
    # Date on which the transaction occurred
    date: Date
    # Identifier for the security (stock, plan security, warrant, or convertible) by
    # which it can be referenced by other transaction objects. Note that while this
    # identifier is created with an issuance object, it should be different than the
    # issuance object's `id` field which identifies the issuance transaction object
    # itself. All future transactions on the security (e.g. acceptance, transfer,
    # cancel, etc.) must reference this `security_id` to qualify which security the
    # transaction applies to.
    security_id: str
