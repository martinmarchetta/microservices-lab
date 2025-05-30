CREATE TABLE client (
    id BIGSERIAL NOT NULL,
    client_name VARCHAR(100) NOT NULL,
    client_address VARCHAR(500),
    PRIMARY KEY (id)
);
