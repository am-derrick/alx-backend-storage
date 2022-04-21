-- creates a table users with attributes id, email, anme, country

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
