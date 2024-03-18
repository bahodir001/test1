from connect_db import Database


def create_tables():

    customer_table = """
        CREATE TABLE customer(
            first_name VARCHAR(25),
            last_name VARCHAR(25),
            username VARCHAR(25),
            email VARCHAR(25),
            password VARCHAR(25),
            create_date TIMESTAMP DEFAULT now());
    """

    payment_table = """
            CREATE TABLE payment(
                payment_id SERIAL PRIMARY KEY,
                cash NUMERIC,
                card NUMERIC,
                last_update DATETIME DEFAULT now(),
                create_date TIMESTAMP DEFAULT now());
    """

    product_table = """
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(25),
            quantity NUMERIC,
            price NUMERIC,
            create_date TIMESTAMP DEFAULT now());
    """

    product_categories_table = """
        CREATE TABLE product_category(
            product_category_id SERIAL PRIMARY KEY,
            product_category_name VARCHAR(25),
            product_id INT REFERENCES product(product_id),
            create_date TIMESTAMP DEFAULT now());
    """

    seller_table = """
        CREATE TABLE seller(
            seller_id SERIAL PRIMARY KEY,
            seller_name VARCHAR(25),
            last_name VARCHAR(25),
            username VARCHAR(25),
            product_id INT REFERENCES product(product_id),
            create_date TIMESTAMP DEFAULT now());
    """


    orders_table = """
        CREATE TABLE order(
            order_id SERIAL PRIMARY KEY,
            amount INT,
            product_id INT REFERENCES product(product_id),
            customer_id INT REFERENCES customer(customer_id),
            payment_id INT REFERENCES payment(payment_id),
            order_history_id INT REFERENCES order_history(order_history_id),
            date_ordered DATE,
            create_date TIMESTAMP DEFAULT now());
    """

    order_history_table = """
        CREATE TABLE order_history(
            order_id SERIAL PRIMARY KEY,
            history TEXT,
            customer_id INT REFERENCES customer(customer_id),
            payment_id INT REFERENCES payment(payment_id),
            product_id INT REFERENCES product(product_id),
            created_date TIMESTAMP DEFAULT now());
    """

    order_details_table = """
        CREATE TABLE order_details(
            order_id SERIAL PRIMARY KEY,
            product_status TEXT,
            size NUMERIC,
            quantity NUMERIC,
            customer_id INT REFERENCES customer(customer_id),
            payment_id INT REFERENCES payment(payment_id),
            product_id INT REFERENCES product(product_id),
            created_date TIMESTAMP DEFAULT now());
    """

    storehouse_table = """
        CREATE TABLE storehouse(
            storehouse_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            product_id INT REFERENCES product(product_id),
            expired_product_id INT REFERENCES expired_product(expired_product_id),
            staff_category_id INT REFERENCES staff_category(staff_category_id),
            create_date TIMESTAMP DEFAULT now());
    """

    data = {
        "customer_table" : customer_table,
        "payment_table" : payment_table,
        "product_table" : product_table,
        "product_categories_table" : product_categories_table,
        "seller_table" : seller_table,
        "orders_table" : orders_table,
        "order_details_table" : order_details_table,
        "order_history_table" : order_history_table,
        "storehouse_table" : storehouse_table
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_tables()