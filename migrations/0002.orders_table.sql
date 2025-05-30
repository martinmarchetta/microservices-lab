CREATE TABLE orders (
    order_id BIGSERIAL NOT NULL,
    client_id BIGINT NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE
);
