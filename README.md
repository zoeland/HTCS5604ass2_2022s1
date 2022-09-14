# HTCS5604ass2_2022s1

## How to run locally

### Manage Python env and project dependencies with [PDM](https://github.com/pdm-project/pdm)

```
$ pdm init

$ pdm install
```

### Run Flask app locally

```
$ pdm run flask run

* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## How to test locally

### Run unittest

```
$ pdm run python -m unittest tests/test_functions.py -v

test_isAInt (tests.test_functions.TestFunctionMethods) ... ok
test_isValidChoice (tests.test_functions.TestFunctionMethods) ... ok
test_isValidInputNumber (tests.test_functions.TestFunctionMethods) ... ok
test_isValidName (tests.test_functions.TestFunctionMethods) ... ok
test_isValidPosition (tests.test_functions.TestFunctionMethods) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```