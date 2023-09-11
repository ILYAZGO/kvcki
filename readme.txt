HOW TO RUN LOCALLY:

install requirements and browsers:

    pip install -r requirements.txt  (for install requirements)
    playwright install (for install browsers)

from main directory:

    pytest -sv

    --headed  (browser head)
    --slowmo 3000  (if you want to slow tests down in 3000 ms)
    !--numprocesses auto  (few processes same time - faster tests, but can cause troubles) (DON'T USE)!

    -m {some marker}  (you can call test-sets. look markers in pytest.ini)


    preconditions:
    admin : login-4adminIM name-adminIM
    user : login-1userIM name-userIM
    manager : login-3managerIM name-managerIM
    operator : login-2operatorIM name-operatorIM

    user for import : importFrom importFrom
    with group 11111 rule 22222 inside
    with rule 33333 without group







