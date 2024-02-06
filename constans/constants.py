class Constants:

    # Login page constans

    VALID_USERMAIL = "testerpython@test.pl"
    VALID_PASSWORD = "testerpython"

    INVALID_USERMAIL = "tester@com"
    BLANK_USERMAIL = ""

    INVALID_PASSWORD = "abcdefg1"
    BLANK_PASSWORD = ""

    VALID_LOGIN_DATA = [(VALID_USERMAIL, VALID_PASSWORD)]

    FAILED_LOGIN_DATA = [(INVALID_USERMAIL, INVALID_PASSWORD), (VALID_USERMAIL, INVALID_PASSWORD),
                         (INVALID_USERMAIL, VALID_PASSWORD)]

    BLANK_LOGIN_DATA = [(BLANK_USERMAIL, BLANK_PASSWORD), (BLANK_USERMAIL, VALID_PASSWORD),
                        (VALID_USERMAIL, BLANK_PASSWORD), (BLANK_USERMAIL, INVALID_PASSWORD),
                        (INVALID_USERMAIL, BLANK_PASSWORD)]

    popup_error_msg = "Wystąpił nieoczekiwany błąd"
    log_off_msg = "Wyloguj"
    log_in_check_msg = "Moje konto"
    logout_msg = "Strefa klienta"

    # Product search constans

    VALID_SEARCH_DATA = ["poduszka", "kubek", "puzzle"]
    INVALID_SEARCH_DATA = ["xyz123", "", "abcd"]
    search_msg = "Wyniki wyszukiwania"

    # User account constans

    FNAME = "tester"
    LNAME = "TESTER"
    PHONE_NUMBER = "512-345-678"
    COUNTRY = "Ukraine"
    CITY = "Wrocław"
    STREET = "Testowa 1/2"
    CODE = "00-001"

    ACCOUNT_DATA = (PHONE_NUMBER, FNAME + " " + LNAME, CODE + " " +CITY + " " + STREET)

    # basket constans

    empty_basket_msg = "Koszyk jest pusty"

