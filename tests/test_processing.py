 
import scrubadub

from src.processing import (
    clean_phone_email,
    )

PHONE_1 = '800-555-5555'
PHONE_2 = '800-764-4321'
EMAIL_1 = 'meow@ailurophile.com'
EMAIL_2 = 'purr@cat.com'
URL_1 = 'https://petme.org'


def test_valid_input_01():
    """
    Verify that strings selected as input to be cleaned by the scrubadub library
        are, in fact, removed
    """

    cleaned_txt = scrubadub.clean(PHONE_1)
    assert PHONE_1 not in cleaned_txt, (
        f'Expected "{PHONE_1}" to be removed from cleaned text')


def test_valid_input_02():
    """
    Verify that strings selected as input to be cleaned by the scrubadub library
        are, in fact, removed
    """

    cleaned_txt = scrubadub.clean(PHONE_2)
    assert PHONE_2 not in cleaned_txt, (
        f'Expected "{PHONE_2}" to be removed from cleaned text')


def test_valid_input_03():
    """
    Verify that strings selected as input to be cleaned by the scrubadub library
        are, in fact, removed
    """

    cleaned_txt = scrubadub.clean(EMAIL_1)
    assert EMAIL_1 not in cleaned_txt, (
        f'Expected "{EMAIL_1}" to be removed from cleaned text')


def test_valid_input_04():
    """
    Verify that strings selected as input to be cleaned by the scrubadub library
        are, in fact, removed
    """

    cleaned_txt = scrubadub.clean(EMAIL_2)
    assert EMAIL_2 not in cleaned_txt, (
        f'Expected "{EMAIL_2}" to be removed from cleaned text')


def test_valid_input_05():
    """
    Verify that strings selected as input to be cleaned by the scrubadub library
        are, in fact, removed
    """

    cleaned_txt = scrubadub.clean(URL_1)
    assert URL_1 not in cleaned_txt, (
        f'Expected "{URL_1}" to be removed from cleaned text')


def test_clean_phone_email_01():
    """
    Test valid input, requiring no changes
    """

    txt = '"Meow" said the cat, and "woof" said the dog.'
    result = clean_phone_email(txt)
    correct_result = txt
    assert result == correct_result


def test_clean_phone_email_02():
    """
    Test valid input, phone number
    """

    txt = f'"Meow" said the cat after dialing {PHONE_1}.'

    # uses all default detectors to clean text
    all_cleaned_txt = scrubadub.clean(txt)

    result = clean_phone_email(txt)
    correct_result = all_cleaned_txt 
    assert result == correct_result


def test_clean_phone_email_03():
    """
    Test valid input, phone numbers
    """

    txt = f'"Meow" said the cat after dialing {PHONE_1} and {PHONE_2}.'

    # uses all default detectors to clean text
    all_cleaned_txt = scrubadub.clean(txt)

    result = clean_phone_email(txt)
    correct_result = all_cleaned_txt 
    assert result == correct_result


def test_clean_phone_email_04():
    """
    Test valid input, email
    """

    txt = f'"Meow" said the cat after typing {EMAIL_1}.'

    # uses all default detectors to clean text
    all_cleaned_txt = scrubadub.clean(txt)

    result = clean_phone_email(txt)
    correct_result = all_cleaned_txt 
    assert result == correct_result


def test_clean_phone_email_05():
    """
    Test valid input, email
    """

    txt = f'"Meow" said the cat after typing {EMAIL_1} and {EMAIL_2}.'

    # uses all default detectors to clean text
    all_cleaned_txt = scrubadub.clean(txt)

    result = clean_phone_email(txt)
    correct_result = all_cleaned_txt 
    assert result == correct_result


def test_clean_phone_email_06():
    """
    Test valid input, phone number and email
    """

    txt = f'"Meow" said the cat after dialing {PHONE_1} and typing {EMAIL_1}.'

    # uses all default detectors to clean text
    all_cleaned_txt = scrubadub.clean(txt)

    result = clean_phone_email(txt)
    correct_result = all_cleaned_txt 
    assert result == correct_result


def test_clean_phone_email_07():
    """
    Test valid input:
        - clean phone number and email
        - ignore URL
    """

    txt = (
        f'"Meow" said the cat after dialing {PHONE_1}, typing {EMAIL_1}, '
        f'and browsing to {URL_1}.')

    result = clean_phone_email(txt)
    correct_result = (
        '"Meow" said the cat after dialing {{PHONE}}, typing {{EMAIL}}, '
        f'and browsing to {URL_1}.')
    assert result == correct_result


