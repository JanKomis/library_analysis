CREATE TABLE book_category (
    book_id INT,
    category_id INT,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);