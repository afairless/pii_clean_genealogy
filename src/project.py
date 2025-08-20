#! /usr/bin/env python3

from pathlib import Path
import scrubadub


def read_text_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_text_file(file_path, content):

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():

    input_path = Path.cwd() / 'input'
    input_filepath = input_path / 'input.txt'

    output_path = Path.cwd() / 'output'
    output_filepath = output_path / 'output.txt'

    txt = read_text_file(input_filepath)
    # cleaned_txt = scrubadub.clean(txt)
    scrubber = scrubadub.Scrubber()
    scrubber.remove_detector('email')
    cleaned_txt = scrubadub.clean(txt)

    write_text_file(output_filepath, cleaned_txt)




if __name__ == '__main__':
    main()
