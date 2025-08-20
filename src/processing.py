#! /usr/bin/env python3

import scrubadub
import xml.etree.ElementTree as ET


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


def extract_top_tag_genealogy_xml_tree(
    root: ET.Element, top_level_tag: str) -> str:
    """
    Extract the top-level tag from a genealogy XML tree
    """

    namespace = root.tag.split('}')[0].strip('{')
    tag = f'{{{namespace}}}{top_level_tag}'

    return tag


def clean_genealogy_xml_tree(
    root: ET.Element, top_level_tag: str) -> ET.Element:
    """
    Clean the genealogy XML tree by removing phone numbers and email addresses
    Text fields in the tree are filtered before applying 'clean_phone_email' to
        avoid false positives, especially with the email detector, which 
        incorrectly identifies email addresses in text using the word 'at'.
    """

    for e in root.iter():
        if e.tag == top_level_tag:
            if e.text is not None:

                if 'txtForward' in e.text:
                    e.text = clean_phone_email(e.text)

                elif (
                    'from:' in e.text.lower() and 
                    # 'to:' in e.text.lower() and
                    'date:' in e.text.lower() and
                    'subject:' in e.text.lower()):

                    e.text = clean_phone_email(e.text)

    return root


