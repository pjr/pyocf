"""Type represents a group of securities that constitutes some formally defined
part of the company (e.g. post-money capitalization vs pre-money for a security)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/types/CapitalizationDefinition.schema.json

from pydantic import BaseModel


class CapitalizationDefinition(BaseModel):
    """Type represents a group of securities that constitutes some formally defined
    part of the company (e.g. post-money capitalization vs pre-money for a security)
    """

    # All issuances of stock classes with these ids should be included (unless such an
    # issuance is specifically included in `exclude_security_ids`
    include_stock_class_ids: list[str]
    # All issuances of plan securities from stock plans with these ids should be
    # included (unless such an issuance is specifically excluded in
    # `exclude_security_ids`
    include_stock_plans_ids: list[str]
    # Securities (whether Stock, Plan Securities, Convertibles or Warrants) with these
    # security ids should be included from this definition of capitalization
    # (overrides plan or class-level rules)
    include_security_ids: list[str]
    # Securities (whether Stock, Plan Securities, Convertibles or Warrants) with these
    # security ids should be excluded from this definition of capitalization
    # (overrides plan or class-level rules)
    exclude_security_ids: list[str]
