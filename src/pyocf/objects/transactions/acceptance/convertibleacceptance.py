"""Object describing a convertible acceptance transaction"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-OCF/t
# ree/v1.0.0/schema/objects/transactions/acceptance/ConvertibleAcceptance.schema.j
# son

from pyocf.primitives.objects.object import Object
from pyocf.primitives.objects.transactions.acceptance.acceptance import Acceptance
from pyocf.primitives.objects.transactions.securitytransaction import (
    SecurityTransaction,
)
from pyocf.primitives.objects.transactions.transaction import Transaction
from pyocf.types.date import Date
from typing import Literal
from typing import Optional


class ConvertibleAcceptance(Object, Transaction, SecurityTransaction, Acceptance):
    """Object describing a convertible acceptance transaction"""

    object_type: Literal["TX_CONVERTIBLE_ACCEPTANCE"] = "TX_CONVERTIBLE_ACCEPTANCE"
    # Identifier for the object
    id: str
    # Unstructured text comments related to and stored for the object
    comments: Optional[list[str]]
    # Identifier for the security (stock, plan security, warrant, or convertible) by
    # which it can be referenced by other transaction objects. Note that while this
    # identifier is created with an issuance object, it should be different than the
    # issuance object's `id` field which identifies the issuance transaction object
    # itself. All future transactions on the security (e.g. acceptance, transfer,
    # cancel, etc.) must reference this `security_id` to qualify which security the
    # transaction applies to.
    security_id: str
    # Date on which the transaction occurred
    date: Date
