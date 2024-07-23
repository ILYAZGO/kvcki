import os
from datetime import datetime

#LIST OF URLS
URL = 'http://192.168.10.101/feature-dev-2714/' #os.getenv('PUBLIC_URL') or "https://app.stand.imot.io/ru"
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
USER_FOR_CHECK = "comparelogin"
PASSWORD = "Qaz123wsX"

ECOTELECOM = "ecotelecom"  # used for calls and reports test
ECOPASS = "ecopass1)"      # used for calls and reports test

LOGIN_NEGOTIVE = "1userI"
PASSWORD_NEGOTIVE = "Qaz123ws"

# LIST OF USERS FOR IMPORT
# FROM_USER_IMPORT = "importFrom"


# LIST OF ROLES

ROLE_USER = 'user'
ROLE_MANAGER = 'manager'
ROLE_ADMIN = 'admin'

#NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"

#NEW_NAME = NEW_LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}0_{datetime.now().microsecond}0"


CHANGED_LOGIN1 = f"auto_test_user_ch_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}1"
CHANGED_LOGIN2 = f"auto_test_user_ch_{datetime.now().strftime('%m%d%H%M')}{datetime.now().microsecond}2"

#EMAIL12 = f"email_{datetime.now().microsecond}{random.randint(100,200)}@mail.ru"
