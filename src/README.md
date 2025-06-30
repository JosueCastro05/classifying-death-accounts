## Source code

This folder contains **core Python modules** used in the project. It supports scraping, preprocessing, modeling, and utility

## Files:

`__init__.py`: Marks this folder as a Python Package. This allows us to import modules from `src/ ` in other parts of the project using dot notation (e.g., `from src.scraper import scrape_data`). The file can be left empty.
`scraper.py`: Functions to scrape and extract text data from web pages
`preprocess.py`: Tools for cleaning, tokenizing, and preparing data
`model.py`: Code for training and evaluating classification models
`utils.py`: helper functions (e.g., saving files, formatting, metrics)

## Notes:

Reuse and import these scripts in `main.py` or notebooks.
Keep each script fcused and modular.
