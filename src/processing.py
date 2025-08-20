#! /usr/bin/env python3

import scrubadub


def read_text_file(file_path):
    """
    Read a text file and return its content as a string
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text_file(file_path, content):
    """
    Write a string content to a text file
    """

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def clean_phone_email(txt: str) -> str:
    """
    Replace phone numbers and email addresses in the text
    """

    detector_list = [
        scrubadub.detectors.EmailDetector,
        scrubadub.detectors.PhoneDetector,
        scrubadub.detectors.CreditCardDetector,
        scrubadub.detectors.en_US.SocialSecurityNumberDetector,
        ]
    scrubber = scrubadub.Scrubber(detector_list=detector_list)
    cleaned_txt = scrubber.clean(txt)

    return cleaned_txt

