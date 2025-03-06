CREATE TABLE addition_info (
    book_id INT PRIMARY KEY,
    dimension_x DECIMAL(6,2), -- width
    dimension_y DECIMAL(6,2), -- height
    dimension_z DECIMAL(6,2), -- depth
    rating_avg DECIMAL(3,2), -- average rating
    rating_count INT, -- number of ratings
    weight DECIMAL(8,2), -- book weight in grams
    bestsellers_rank INT, -- bestseller ranking
    for_ages VARCHAR(255), -- recommended age group
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
);