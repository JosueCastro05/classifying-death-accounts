## Processed Data

This folder contains **cleaned and labeled datasets** ready for modeling and analysis.

Files in this folder are derived from the raw data and should be :

- Tokenized
- Cleaned (e.g., removing HTML tags, stopwords)
- Labeled (e.g., `NDE`, or `RED`)

## What belongs here:

- `.csv` files with labeled and structured text data
- Pickled or NumPy-formatted data for model input (`.pkl`, `.npz`)
- Final datasets used by notebooks or `src/model.py`

## Notes:

- Use scripts in `src/preprocess.py` to generate these files.
- Keep backups of important processed datasets.
