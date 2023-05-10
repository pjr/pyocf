"""JSON containing file type identifier and list of stock legend templates"""

# Autogenerated, do not edit.
# Copyright © 2023 FMR LLC
#
# Based on the Open Captable Format schema:
# Copyright © 2022 Open Cap Table Coalition (https://opencaptablecoalition.com) /
# Original File: https://github.com/Open-Cap-Table-Coalition/Open-Cap-Format-
# OCF/tree/v1.0.0/schema/files/StockLegendTemplatesFile.schema.json

from pyocf.objects.stocklegendtemplate import StockLegendTemplate
from pyocf.primitives.files.file import FileObject
from typing import Literal


class StockLegendTemplatesFile(FileObject):
    """JSON containing file type identifier and list of stock legend templates"""

    # List of OCF stock legend template objects
    items: list[StockLegendTemplate]
    file_type: Literal[
        "OCF_STOCK_LEGEND_TEMPLATES_FILE"
    ] = "OCF_STOCK_LEGEND_TEMPLATES_FILE"
