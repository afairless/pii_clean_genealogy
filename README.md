
# Genealogy XML PII Cleaner

This project processes genealogy XML files exported from [Gramps](https://gramps-project.org/wiki/index.php?title=main_page), removing personally identifiable information (PII) like phone numbers and email addresses, and outputs a cleaned XML file with the correct Gramps DOCTYPE and header.

## Features

- Cleans PII (phone numbers, emails, credit cards, SSNs) from Notes in genealogy XML files.
- Preserves Gramps XML structure and metadata.
- Outputs files compatible with Gramps Web and other genealogy tools.

## Setup

This project uses [Pixi](https://prefix.dev/docs/pixi/) for environment and dependency management.

1. **Install Pixi**  
   Follow the instructions at [https://prefix.dev/docs/pixi/overview](https://prefix.dev/docs/pixi/overview).

## Usage

1. Place your input XML file as `input/input.xml`.
2. Run the main entry point:
   ```
   python -m src.entry
   ```
3. The cleaned file will be saved as `output/input.gramps`.

## Project Structure

- `src/entry.py` — Entry point for running the cleaning pipeline.
- `src/main.py` — Main logic for file handling and XML processing.
- `src/processing.py` — Functions for cleaning PII and handling XML structure.
- `input/` — Place your raw XML files here.
- `output/` — Cleaned files are written here.
- `tests/` — Unit tests for processing functions.

## Testing

Run all tests with:
```
pixi run pytest
```

## Notes

- Only specific XML text fields are cleaned to avoid false positives.
- The output file includes the correct Gramps XML header and DOCTYPE for compatibility.
- The cleaning logic uses `scrubadub` with custom detectors for robust PII removal.
- The environment is configured for Linux-64 and Python 3.13.x.

