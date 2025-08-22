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


def extract_namespace_and_top_tag_genealogy_xml_tree(
    root: ET.Element, top_level_tag: str) -> tuple[str, str]:
    """
    Extract the top-level tag from a genealogy XML tree
    """

    namespace = root.tag.split('}')[0].strip('{')
    tag = f'{{{namespace}}}{top_level_tag}'

    return namespace, tag


def extract_gramps_version_from_namespace(namespace: str) -> str:
    """
    The Gramps version number is contained within the URL that is also the XML
        tree namespace; extract it
    """

    namespace_split_1 = namespace.split('/')
    namespace_split_2 = [e for e in namespace_split_1 if e]
    version_number = namespace_split_2[-1]

    return version_number


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


def encode_gramps_xml_header(
    namespace: str, gramps_version_number: str) -> tuple[bytes, bytes]:
    """
    Encode the Gramps XML header with the namespace and version number
    """

    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n'
    doctype_str = (
        f'<!DOCTYPE database PUBLIC "-//Gramps//DTD Gramps XML '
        f'{gramps_version_number}//EN"\n'
        f'"{namespace}grampsxml.dtd">\n')

    xml_bytes = xml_str.encode('utf-8')
    doctype_bytes = doctype_str.encode('utf-8')

    return xml_bytes, doctype_bytes


