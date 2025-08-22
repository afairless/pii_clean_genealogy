#! /usr/bin/env python3

from pathlib import Path
import xml.etree.ElementTree as ET

from src.processing import (
    extract_namespace_and_top_tag_genealogy_xml_tree,
    extract_gramps_version_from_namespace,
    clean_genealogy_xml_tree,
    encode_gramps_xml_header,
    )


def main():


    # SET INPUT AND OUTPUT FILE PATHS
    ##################################################

    input_path = Path.cwd() / 'input'
    input_filename = 'input.xml'
    input_filepath = input_path / input_filename 

    output_path = Path.cwd() / 'output'
    output_path.mkdir(parents=True, exist_ok=True)
    output_filepath = output_path / input_filename
    output_suffix = '.gramps'


    # PROCESS/CLEAN TREE OF PII DATA
    ##################################################

    tree = ET.parse(input_filepath)
    root = tree.getroot()

    top_level_tag = 'text'
    namespace, text_tag = extract_namespace_and_top_tag_genealogy_xml_tree(
        root, top_level_tag)

    # Clean PII data from XML tree
    clean_root = clean_genealogy_xml_tree(root, text_tag)


    # SAVE CLEANED TREE
    ##################################################

    # These lines cannot be used because they erroneously omit the DOCTYPE and 
    #   Gramps XML header from the output file
    # clean_tree = ET.ElementTree(clean_root)
    # clean_tree.write(output_filepath, encoding='utf-8', xml_declaration=True)

    ET.register_namespace('', namespace)

    gramps_version_number = extract_gramps_version_from_namespace(namespace)
    xml_bytes, doctype_bytes = encode_gramps_xml_header(
        namespace, gramps_version_number)
    tree_str = ET.tostring(clean_root, encoding='utf-8', xml_declaration=True)

    # Manually add DOCTYPE and header to XML tree output
    with open(output_filepath.with_suffix(output_suffix), 'wb') as f:
        f.write(xml_bytes)
        f.write(doctype_bytes)
        f.write(tree_str.split(b'\n', 1)[1])


if __name__ == '__main__':
    main()
