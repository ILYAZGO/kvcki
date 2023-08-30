import os
from datetime import datetime

#LIST OF URLS

URL = os.getenv('PUBLIC_URL') or "https://app.stand.imot.io/ru"
API_URL = "https://api.stand.imot.io"

# LIST OF TIMEOUTS

timeout = 55000
wait_until_visible = 30000

# LIST OF CREDENTIALS

USER ="1userIM"
OPERATOR ="2operatorIM"
MANAGER = "3managerIM"
ADMIN = "4adminIM"
USER_FOR_IMPORT = "importFrom"
PASSWORD = "Qaz123wsX"

ECOTELECOM = "ecotelecom"  #used for calls and reports test
ECOPASS = "ecopass1)"      #used for calls and reports test

LOGIN_NEGOTIVE = "1userI"
PASSWORD_NEGOTIVE ="Qaz123ws"

# LIST OF USERS FOR IMPORT
FROM_USER_IMPORT = "importFrom"
TO_USER_IMPORT = "importTo"

# CRED FOR REGISTRATIONS
REGISTRATION_NAME = "John Coltrane"
REGISTRATION_EMAIL = "ilyasmustafin@imot.io"
REGISTRATION_PHONE = "9169540252"

# LIST OF TOKENS

USEDESK_TOKEN = "445ab1e8e6853d3bbedf686ab02f4cb746098a9a"


# LIST OF USERS

name1 = "auto_test_user_1"
name2 = "auto_test_user_2"
name3 = "auto_test_user_3"
name4 = "auto_test_user_4"
name5 = "auto_test_user_5"
name6 = "auto_test_user_6"
name7 = "auto_test_user_7"
name8 = "auto_test_user_8"
name9 = "auto_test_user_9"
name10 = "auto_test_user_10"
name_usedesk = "usedeskTest"

login1 = "auto_test_user_1"
login2 = "auto_test_user_2"
login3 = "auto_test_user_3"
login4 = "auto_test_user_4"
login5 = "auto_test_user_5"
login6 = "auto_test_user_6"
login7 = "auto_test_user_7"
login8 = "auto_test_user_8"
login9 = "auto_test_user_9"
login10 = "auto_test_user_10"
login_usedesk = "usedesk"

# LIST OF ROLES

ROLE_USER = 'user'
ROLE_MANAGER = 'manager'
ROLE_ADMIN = 'admin'

# operator credentials

NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().microsecond}"

