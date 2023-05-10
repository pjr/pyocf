"""Top-level schema describing the OCF Manifest, which holds issuer information and"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/files/OCFManifestFile.schema.json

from pyocf.enums.ocfversiontype import OCFVersionType
from pyocf.objects.issuer import Issuer
from pyocf.primitives.files.file import FileObject
from pyocf.types.date import Date
from pyocf.types.file import File
from typing import Literal
from typing import Optional


class OCFManifestFile(FileObject):
    """Top-level schema describing the OCF Manifest, which holds issuer information and
    references ocf files containing transactions, stakeholders, stock classes, etc.
    """

    # OCF Version Identifier
    ocf_version: OCFVersionType
    file_type: Literal["OCF_MANIFEST_FILE"] = "OCF_MANIFEST_FILE"
    # Issuer for the cap table
    issuer: Issuer
    # The point-in-time represented by this OCF Package
    as_of: Date
    # Timestamp of when the package was generated. Useful when determining which set
    # of data is most up-to-date, if presented with two packages that have the same
    # `as_of` date, but different cap table data.
    generated_at: str
    # Unstructured text comments related to and stored for the cap table
    comments: Optional[list[str]]
    # List of files containing lists of issuer stock plans, indexed from the file
    # containing the first such object created to the file containing the last (See
    # separate /schema/files/stock_plans_file schema to validate loaded files)
    stock_plans_files: list[File]
    # List of files containing lists of issuer stock legend templates, indexed from
    # the file containing the first such object created to the file containing the
    # last (See separate /schema/files/stock_legend_templates_file schema to validate
    # loaded files)
    stock_legend_templates_files: list[File]
    # List of files containing lists of issuer stock classes, indexed from the file
    # containing the first such object created to the file containing the last (See
    # separate /schema/files/stock_classes_file schema to validate loaded files)
    stock_classes_files: list[File]
    # List of files containing lists of issuer vesting terms, indexed from the file
    # containing the first such object created to the file containing the last (See
    # separate /schema/files/vesting_terms_file schema to validate loaded files)
    vesting_terms_files: list[File]
    # List of files containing lists of issuer valuations, indexed from the file
    # containing the first such object created to the file containing the last (See
    # separate /schema/files/valuations_file schema to validate loaded files)
    valuations_files: list[File]
    # List of files containing lists of issuer transactions, indexed from the file
    # containing the first such object created to the file containing the last (See
    # separate /schema/files/transactions_file schema to validate loaded files)
    transactions_files: list[File]
    # List of files containing lists of issuer stakeholders, indexed from the file
    # containing the first such object created to the file containing the last (See
    # separate /schema/files/stakeholders_file schema to validate loaded files)
    stakeholders_files: list[File]
