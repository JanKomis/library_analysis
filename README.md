## About

This project processes book depository data from ([Kaggle](https://www.kaggle.com/datasets/sp1thas/book-depository-dataset)) using the Pandas library, cleans it, and prepares it for import into a database.

### Project Features

- Standard data cleaning (handling duplicates, formatting adjustments, etc.)
- ISBN13 validation using the `isbnlib` library
- Language code validation using the `pycountry` library
- Unit tests for more complex functions using `pytest`
- Functions that create m:n and 1:1 relationships from datasets
- SQL schemas and a seed file for loading data into the database

## Scheme 

<p>
    <img src="scheme.png" alt="Description" width="400">
</p>