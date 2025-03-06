\COPY books FROM '['your path']\LIBRARY\dataset\to_sql\final_dataset.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY addition_info FROM '['your path']\LIBRARY\dataset\to_sql\addition_cleaned.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY authors FROM '['your path']\LIBRARY\dataset\to_sql\final_authors.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY categories FROM '['your path']\LIBRARY\dataset\to_sql\final_categories.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY formats FROM '['your path']\LIBRARY\dataset\to_sql\formats_cleaned.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY languages FROM '['your path']\LIBRARY\dataset\to_sql\final_lang.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY book_author FROM '['your path']\LIBRARY\dataset\to_sql\mn_author.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

\COPY book_category FROM '['your path']\LIBRARY\dataset\to_sql\mn_categories.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '', ENCODING 'UTF8');

