import os
from datetime import datetime

#LIST OF URLS
URL = os.getenv('PUBLIC_URL') or "https://app.stand.imot.io/ru"
API_URL = "https://api.stand.imot.io"

# LIST OF TIMEOUTS

timeout = 55000
wait_until_visible = 45000

# LIST OF CREDENTIALS

USER = "1userIM"
OPERATOR = "2operatorIM"
MANAGER = "3managerIM"
ADMIN = "4adminIM"
USER_FOR_IMPORT = "importFrom"
PASSWORD = "Qaz123wsX"

ECOTELECOM = "ecotelecom"  # used for calls and reports test
ECOPASS = "ecopass1)"      # used for calls and reports test

LOGIN_NEGOTIVE = "1userI"
PASSWORD_NEGOTIVE = "Qaz123ws"

# LIST OF USERS FOR IMPORT
# FROM_USER_IMPORT = "importFrom"
# TO_USER_IMPORT = "importTo"

# CRED FOR REGISTRATIONS
REGISTRATION_NAME = "John Coltrane"
REGISTRATION_EMAIL = "ilyasmustafin@imot.io"
REGISTRATION_PHONE = "9169540252"

# LIST OF ROLES

ROLE_USER = 'user'
ROLE_MANAGER = 'manager'
ROLE_ADMIN = 'admin'


# operator credentials
# used in test_add_delete_operator_by_user.py


NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
EMAIL = f"email_{datetime.now().microsecond}@mail.ru"

