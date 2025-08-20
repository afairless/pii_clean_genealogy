#! /usr/bin/env python3

from pathlib import Path
import xml.etree.ElementTree as ET

from src.processing import (
    extract_top_tag_genealogy_xml_tree,
    clean_genealogy_xml_tree,
    )


def main():


    # SET INPUT AND OUTPUT FILE PATHS
    ##################################################

    input_path = Path.cwd() / 'input'
    input_filename = 'input.xml'
    input_filepath = input_path / input_filename 

    output_path = Path.cwd() / 'output'
    output_filepath = output_path / input_filename


    # SET INPUT AND OUTPUT FILE PATHS
    ##################################################

    tree = ET.parse(input_filepath)
    root = tree.getroot()

    top_level_tag = 'text'
    text_tag = extract_top_tag_genealogy_xml_tree(root, top_level_tag)
    clean_root = clean_genealogy_xml_tree(root, text_tag)

    clean_tree = ET.ElementTree(clean_root)
    clean_tree.write(output_filepath, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    main()
