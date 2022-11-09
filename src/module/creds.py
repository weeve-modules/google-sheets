from .params import PARAMS

CREDS_DICT = {
  "type": "service_account",
  "project_id": PARAMS['PROJECT_ID'],
  "private_key_id": PARAMS['PRIVATE_KEY_ID'],
  "private_key": PARAMS['PRIVATE_KEY'],
  "client_email": PARAMS['CLIENT_EMAIL'],
  "client_id": PARAMS['CLIENT_ID'],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/" + PARAMS['CLIENT_EMAIL'].replace('%', '%40')
}
