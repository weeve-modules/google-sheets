"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import gspread
from logging import getLogger
from oauth2client.service_account import ServiceAccountCredentials
from .params import PARAMS
from .creds import CREDS_DICT

log = getLogger("module")

credentials = ServiceAccountCredentials.from_json_keyfile_dict(CREDS_DICT, ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"])
gc = gspread.authorize(credentials)
worksheet = gc.open(PARAMS['SPREADSHEET_TITLE']).worksheet(PARAMS['WORKSHEET_TITLE'])

if PARAMS["HAS_COLUMN_HEADERS"]:
    # read headers from the first row in the spreadsheet
    COLUMN_HEADERS = worksheet.row_values(1)
else:
    COLUMN_HEADERS = None

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Writing to Google Sheets ...")

    try:
        if type(received_data) is list:
            rows = [] # rows must be List[List]

            for data in received_data:
                # convert JSON to list of values
                if COLUMN_HEADERS:
                    single_row = [data[label] for label in COLUMN_HEADERS]
                else:
                    single_row = list(data.values())

                rows.append(single_row)

            worksheet.append_rows(rows)

        else:
            # convert JSON to list of values
            if COLUMN_HEADERS:
                single_row = [received_data[label] for label in COLUMN_HEADERS]
            else:
                single_row = list(received_data.values())

            worksheet.append_row(single_row)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
