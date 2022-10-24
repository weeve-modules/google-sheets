from os import getenv

PARAMS = {
    "PROJECT_ID": getenv("PROJECT_ID", ""),
    "PRIVATE_KEY_ID": getenv("PRIVATE_KEY_ID", ""),
    "PRIVATE_KEY": getenv("PRIVATE_KEY", "").replace("\\n", "\n"),
    "CLIENT_EMAIL": getenv("CLIENT_EMAIL", ""),
    "CLIENT_ID": getenv("CLIENT_ID", ""),
    "SPREADSHEET_TITLE": getenv("SPREADSHEET_TITLE", ""),
    "WORKSHEET_TITLE": getenv("WORKSHEET_TITLE", ""),
    "COLUMN_HEADERS": bool(getenv("COLUMN_HEADERS", "False"))
}
