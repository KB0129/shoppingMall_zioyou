-- file name: schema.sql
-- pwd: shoopinaMall_zioyou/start_shoppingmall/schema/schema.sql

-- CREATE DATABASE testDB;
CREATE DATABASE IF NOT EXISTS testDB;

-- initialize table before CREATE TABLES
DROP TABLE IF EXISTS cart_list;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS product;

-- use testDB;
USE testDB;

-- the table for account data
CREATE TABLE accounts(
    user_id         INT         UNIQUE      AUTO_INCREMENT,
    user_email      CHAR(50)    UNIQUE,
    user_name       CHAR(50),
    user_password   CHAR(100),

    -- primary keys
    PRIMARY KEY (user_id, user_email)
    )ENGINE = InnoDB;

-- the table for product data
CREATE TABLE product(
    product_id      INT         UNIQUE      AUTO_INCREMENT,
    product_name    CHAR(50)    UNIQUE,
    product_price   FLOAT       UNIQUE,

    -- primary keys
    PRIMARY KEY(product_price, product_name, product_id)
    )ENGINE = InnoDB;

-- the table for cart
CREATE TABLE cart_list(
    cart_user_id        INT,
    cart_product_id     INT,
    cart_product_price  FLOAT,
    cart_product_name   CHAR(50),
    quantity            INT,

    -- INDEX primary keys
    INDEX(cart_user_id, cart_product_price, cart_product_name, cart_product_id),

    -- CASCADE foreign keys
    FOREIGN KEY(cart_user_id)       REFERENCES accounts(user_id)      ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(cart_product_id)    REFERENCES product(product_id)    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(cart_product_price) REFERENCES product(product_price) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(cart_product_name) REFERENCES product(product_name) ON UPDATE CASCADE ON DELETE CASCADE
    )ENGINE = InnoDB;

