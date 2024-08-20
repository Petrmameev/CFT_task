import sqlite3


def insert_data():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO TARIFS (ID, NAME, COST) VALUES (1, 'Тариф за выдачу кредита', 10)"
        )
        c.execute(
            "INSERT INTO TARIFS (ID, NAME, COST) VALUES (2, 'Тариф за открытие счета', 10)"
        )
        c.execute(
            "INSERT INTO TARIFS (ID, NAME, COST) VALUES (3, 'Тариф за обслуживание карты', 10)"
        )

        c.execute(
            "INSERT INTO PRODUCT_TYPE (ID, NAME, BEGIN_DATE, END_DATE, TARIF_REF) VALUES (1, 'КРЕДИТ', '2018-01-01', NULL, 1)"
        )
        c.execute(
            "INSERT INTO PRODUCT_TYPE (ID, NAME, BEGIN_DATE, END_DATE, TARIF_REF) VALUES (2, 'ДЕПОЗИТ', '2018-01-01', NULL, 2)"
        )
        c.execute(
            "INSERT INTO PRODUCT_TYPE (ID, NAME, BEGIN_DATE, END_DATE, TARIF_REF) VALUES (3, 'КАРТА', '2018-01-01', NULL, 3)"
        )
        c.execute(
            "INSERT INTO PRODUCT_TYPE (ID, NAME, BEGIN_DATE, END_DATE, TARIF_REF) VALUES (4, 'СТРАХОВАНИЕ', '2018-01-01', NULL, NULL)"
        )

        c.execute(
            "INSERT INTO CLIENTS (ID, NAME, PLACE_OF_BIRTH, DATE_OF_BIRTH, ADDRESS, PASSPORT) VALUES (1, 'Сидоров Иван Петрович', 'Россия, Московская область, г. Пушкин', '2001-01-01', 'Россия, Московская область, г. Пушкин, ул. Грибоедова, д. 5', '2222 555555')"
        )
        c.execute(
            "INSERT INTO CLIENTS (ID, NAME, PLACE_OF_BIRTH, DATE_OF_BIRTH, ADDRESS, PASSPORT) VALUES (2, 'Иванов Петр Сидорович', 'Россия, Московская область, г. Клин', '2001-01-01', 'Россия, Московская область, г. Клин, ул. Мясникова, д. 3', '4444 666666')"
        )
        c.execute(
            "INSERT INTO CLIENTS (ID, NAME, PLACE_OF_BIRTH, DATE_OF_BIRTH, ADDRESS, PASSPORT) VALUES (3, 'Петров Сидор Иванович', 'Россия, Московская область, г. Балашиха', '2001-01-01', 'Россия, Московская область, г. Балашиха, ул. Пушкина, д. 7', '4444 666666')"
        )

        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (1, 1, 'Кредитный договор с Сидоровым И.П.', 1, '2015-06-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (2, 2, 'Депозитный договор с Ивановым П.С.', 2, '2017-08-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (3, 3, 'Карточный договор с Петровым С.И.', 3, '2017-08-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (4, 1, 'Кредитный договор с Петровым С.И.', 3, '2018-09-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (5, 1, 'Кредитный договор с полным погашением', 1, '2015-06-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (6, 1, 'Кредитный договор с частичным погашением', 2, '2015-06-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (7, 4, 'Страховой договор без движений', 3, '2018-01-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (8, 4, 'Страховой договор с движениями', 1, '2018-01-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (9, 2, 'Депозитный договор', 2, '2017-08-01', NULL)"
        )
        c.execute(
            "INSERT INTO PRODUCTS (ID, PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE, CLOSE_DATE) VALUES (10, 3, 'Карточный договор', 1, '2017-08-01', NULL)"
        )

        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (1, 'Кредитный счет для Сидоровым И.П.', -2000, 1, '2015-06-01', NULL, 1, '45502810401020000022')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (2, 'Депозитный счет для Ивановым П.С.', 6000, 2, '2017-08-01', NULL, 2, '42301810400000000001')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (3, 'Карточный счет для Петровым С.И.', 8000, 3, '2017-08-01', NULL, 3, '40817810700000000001')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (4, 'Кредитный счет для Петровым С.И.', -5000, 3, '2018-09-01', NULL, 4, '45502810401020000023')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (5, 'Кредитный счет с полным погашением', 0, 1, '2015-06-01', NULL, 5, '45502810401020000024')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (6, 'Кредитный счет с частичным погашением', -2000, 2, '2015-06-01', NULL, 6, '45502810401020000025')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (7, 'Счет страхового договора без движений', 1000, 3, '2018-01-01', NULL, 7, '45502810401020000026')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (8, 'Счет страхового договора с движениями', 1000, 1, '2018-01-01', NULL, 8, '45502810401020000027')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (9, 'Депозитный счет', 10000, 2, '2017-08-01', NULL, 9, '42301810400000000002')"
        )
        c.execute(
            "INSERT INTO ACCOUNTS (ID, NAME, SALDO, CLIENT_REF, OPEN_DATE, CLOSE_DATE, PRODUCT_REF, ACC_NUM) VALUES (10, 'Карточный счет', 5000, 1, '2017-08-01', NULL, 10, '40817810700000000002')"
        )

        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (1, 1, 5000, 1, '2015-06-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (2, 0, 1000, 1, '2015-07-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (3, 0, 2000, 1, '2015-08-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (4, 0, 3000, 1, '2015-09-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (5, 1, 5000, 1, '2015-10-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (6, 0, 3000, 1, '2015-10-01')"
        )

        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (7, 0, 10000, 2, '2017-08-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (8, 1, 1000, 2, '2017-08-05')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (9, 1, 2000, 2, '2017-09-21')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (10, 1, 5000, 2, '2017-10-24')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (11, 0, 6000, 2, '2017-11-26')"
        )

        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (12, 0, 120000, 3, '2017-09-08')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (13, 1, 1000, 3, '2017-10-05')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (14, 1, 2000, 3, '2017-10-21')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (15, 1, 5000, 3, '2017-10-24')"
        )

        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (16, 1, 3000, 4, '2018-10-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (17, 1, 4000, 4, '2018-10-15')"
        )

        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (20, 0, 1000, 1, '2024-07-05')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (21, 1, 2000, 1, '2024-07-10')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (22, 0, 3000, 2, '2024-07-15')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (23, 1, 4000, 2, '2024-07-20')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (24, 0, 5000, 3, '2024-07-25')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (25, 1, 6000, 3, '2024-07-30')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (26, 1, 5000, 5, '2015-06-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (27, 0, 5000, 5, '2015-07-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (28, 1, 5000, 6, '2015-06-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (29, 0, 3000, 6, '2015-07-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (30, 0, 500, 8, '2024-07-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (31, 1, 200, 8, '2024-07-15')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (32, 0, 10000, 9, '2017-08-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (33, 1, 2000, 9, '2017-09-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (34, 0, 5000, 10, '2017-08-01')"
        )
        c.execute(
            "INSERT INTO RECORDS (ID, DT, SUM, ACC_REF, OPER_DATE) VALUES (35, 1, 1000, 10, '2017-09-01')"
        )
    except sqlite3.OperationalError as e:
        if "data already exists" in str(e):
            print("Данные уже существуют.")
        else:
            raise e
    conn.commit()
    conn.close()
