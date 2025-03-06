CREATE TABLE books (
    book_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,  
    title TEXT NOT NULL,
    book_description TEXT,
    isbn13 char(13) UNIQUE,  
    publication_date TIMESTAMP,
    format_id INT, 
    language_id INT,
    FOREIGN KEY (format_id) REFERENCES formats(format_id),
    FOREIGN KEY (language_id) REFERENCES languages(language_id)
);
