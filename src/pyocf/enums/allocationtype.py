"""Enumeration of allocation types for vesting terms. Using an example of 18 shares
split across 4 tranches, each allocation type results in a different schedule as
follows:
  1.  Cumulative Rounding (5 - 4 - 5 - 4)
  2.  Cumulative Round Down (4 - 5 - 4 - 5)
  3.  Front Loaded (5 - 5 - 4 - 4)
  4.  Back Loaded (4 - 4 - 5 - 5)
  5.  Front Loaded to Single Tranche (6 - 4 - 4 - 4)
  6.  Back Loaded to Single Tranche (4 - 4 - 4 - 6)
  7.  Fractional (4.5 - 4.5 - 4.5 - 4.5)"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/enums/AllocationType.schema.json

from enum import Enum


class AllocationType(Enum):
    """Enumeration of allocation types for vesting terms. Using an example of 18 shares
    split across 4 tranches, each allocation type results in a different schedule as
    follows:
      1.  Cumulative Rounding (5 - 4 - 5 - 4)
      2.  Cumulative Round Down (4 - 5 - 4 - 5)
      3.  Front Loaded (5 - 5 - 4 - 4)
      4.  Back Loaded (4 - 4 - 5 - 5)
      5.  Front Loaded to Single Tranche (6 - 4 - 4 - 4)
      6.  Back Loaded to Single Tranche (4 - 4 - 4 - 6)
      7.  Fractional (4.5 - 4.5 - 4.5 - 4.5)
    """

    ENUM_CUMULATIVE_ROUNDING = "CUMULATIVE_ROUNDING"
    ENUM_CUMULATIVE_ROUND_DOWN = "CUMULATIVE_ROUND_DOWN"
    ENUM_FRONT_LOADED = "FRONT_LOADED"
    ENUM_BACK_LOADED = "BACK_LOADED"
    ENUM_FRONT_LOADED_TO_SINGLE_TRANCHE = "FRONT_LOADED_TO_SINGLE_TRANCHE"
    ENUM_BACK_LOADED_TO_SINGLE_TRANCHE = "BACK_LOADED_TO_SINGLE_TRANCHE"
    ENUM_FRACTIONAL = "FRACTIONAL"
