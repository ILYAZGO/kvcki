how to run locally:
    pip install -r requirements.txt  (for install requirements)
    playwright install (for install browsers)

    from main directory:

    pytest --{some arg}
    --numprocesses auto  (few processes same time - faster tests, but can cause troubles)
    --headed  (browser head)
    --slowmo 3000  (if you want to slow tests down in 3000 ms)

    -m {some marker}  (you can call test-sets. look markers in pytest.ini)






