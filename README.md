## Book depository data cleaning
 
 ### About

This project processes book depository data from ([Kaggle](https://www.kaggle.com/datasets/sp1thas/book-depository-dataset)) using the Pandas library, cleans it, and prepares it for import into a database.

#### Project Features

- Standard data cleaning (handling duplicates, formatting adjustments, etc.)
- ISBN13 validation using the `isbnlib` library
- Language code validation using the `pycountry` library
- Unit tests for more complex functions using `pytest`
- Functions that create m:n and 1:1 relationships from datasets
- SQL schemas and a seed file for loading data into the database

### Scheme 

<p>
    <img src="scheme.png" alt="Description" width="400">
</p>

### How to Use

The project is divided into three main folders:

- `datasets`
- `python scripts`
- `sql`

#### Steps to Use the Project:

1. Install the required packages using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
2. Download the dataset into the datasets/origin folder.
3. Run the notebooks for initial data cleaning:
    - `Clean_authors_dataset.ipynb`
    - `Clean_categories_dataset.ipynb`
    - `Clean_dataset.ipynb`
    - `Clean_formats_dataset.ipynb`
4. Run the notebook to create linking tables:
    - `Remove_duplicates.ipynb`
5. Create the database, then execute the SQL scripts in `sql/tables/` to create tables and load seed data from `sql/seed/seed_data.sql`.
