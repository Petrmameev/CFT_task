import sqlite3


def create_all_table():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    try:
        c.execute(
            """CREATE TABLE TARIFS (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        COST REAL NOT NULL)"""
        )
    except sqlite3.OperationalError as e:
        if "table TARIFS already exists" in str(e):
            print("Таблица TARIFS уже существует.")
        else:
            raise e

    try:
        c.execute(
            """CREATE TABLE PRODUCT_TYPE (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        BEGIN_DATE TEXT NOT NULL,
                        END_DATE TEXT,
                        TARIF_REF INTEGER,
                        FOREIGN KEY (TARIF_REF) REFERENCES TARIFS(ID))"""
        )
    except sqlite3.OperationalError as e:
        if "table PRODUCT_TYPE already exists" in str(e):
            print("Таблица PRODUCT_TYPE уже существует.")
        else:
            raise e

    try:
        c.execute(
            """CREATE TABLE CLIENTS (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        PLACE_OF_BIRTH TEXT NOT NULL,
                        DATE_OF_BIRTH TEXT NOT NULL,
                        ADDRESS TEXT NOT NULL,
                        PASSPORT TEXT NOT NULL)"""
        )
    except sqlite3.OperationalError as e:
        if "table CLIENTS already exists" in str(e):
            print("Таблица CLIENTS уже существует.")
        else:
            raise e

    try:
        c.execute(
            """CREATE TABLE PRODUCTS (
                        ID INTEGER PRIMARY KEY,
                        PRODUCT_TYPE_ID INTEGER,
                        NAME TEXT NOT NULL,
                        CLIENT_REF INTEGER,
                        OPEN_DATE TEXT NOT NULL,
                        CLOSE_DATE TEXT,
                        CONTRACT_AMOUNT REAL,
                        FOREIGN KEY (PRODUCT_TYPE_ID) REFERENCES PRODUCT_TYPE(ID),
                        FOREIGN KEY (CLIENT_REF) REFERENCES CLIENTS(ID))"""
        )
    except sqlite3.OperationalError as e:
        if "table PRODUCTS already exists" in str(e):
            print("Таблица PRODUCTS уже существует.")
        else:
            raise e

    try:
        c.execute(
            """CREATE TABLE ACCOUNTS (
                        ID INTEGER PRIMARY KEY,
                        NAME TEXT NOT NULL,
                        SALDO REAL NOT NULL,
                        CLIENT_REF INTEGER,
                        OPEN_DATE TEXT NOT NULL,
                        CLOSE_DATE TEXT,
                        PRODUCT_REF INTEGER,
                        ACC_NUM TEXT NOT NULL,
                        FOREIGN KEY (CLIENT_REF) REFERENCES CLIENTS(ID),
                        FOREIGN KEY (PRODUCT_REF) REFERENCES PRODUCTS(ID))"""
        )
    except sqlite3.OperationalError as e:
        if "table ACCOUNTS already exists" in str(e):
            print("Таблица ACCOUNTS уже существует.")
        else:
            raise e

    try:
        c.execute(
            """CREATE TABLE RECORDS (
                        ID INTEGER PRIMARY KEY,
                        DT INTEGER CHECK (DT IN (0, 1)),
                        SUM REAL NOT NULL,
                        ACC_REF INTEGER,
                        OPER_DATE TEXT NOT NULL,
                        FOREIGN KEY (ACC_REF) REFERENCES ACCOUNTS(ID))"""
        )
    except sqlite3.OperationalError as e:
        if "table RECORDS already exists" in str(e):
            print("Таблица RECORDS уже существует.")
        else:
            raise e

    conn.commit()
    conn.close()
