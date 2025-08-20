#! /usr/bin/env python3

from pathlib import Path

from src.processing import (
    read_text_file,
    write_text_file,
    clean_phone_email,
    )


def main():

    input_path = Path.cwd() / 'input'
    input_filepath = input_path / 'input.txt'

    output_path = Path.cwd() / 'output'
    output_filepath = output_path / 'output.txt'

    txt = read_text_file(input_filepath)
    cleaned_txt = clean_phone_email(txt)

    write_text_file(output_filepath, cleaned_txt)


if __name__ == '__main__':
    main()
