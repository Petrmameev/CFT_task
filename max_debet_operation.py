import sqlite3


def max_debet_operation():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()

    try:
        c.execute(
            """
            ALTER TABLE PRODUCTS
            ADD CONTRACT_AMOUNT NUMBER;
            """
        )
        print("Добавлен новый столбец CONTRACT_AMOUNT в таблицу PRODUCTS.")
    except sqlite3.OperationalError:
        print("Столбец CONTRACT_AMOUNT уже существует в таблице PRODUCTS.")

    c.execute(
        """
        UPDATE PRODUCTS
        SET CONTRACT_AMOUNT = CASE 
            WHEN PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ') THEN (
                SELECT MAX(r.SUM)
                FROM ACCOUNTS a
                JOIN RECORDS r ON a.ID = r.ACC_REF
                WHERE a.PRODUCT_REF = PRODUCTS.ID
                AND r.DT = 1
            )
            WHEN PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'ДЕПОЗИТ') THEN (
                SELECT MAX(r.SUM)
                FROM ACCOUNTS a
                JOIN RECORDS r ON a.ID = r.ACC_REF
                WHERE a.PRODUCT_REF = PRODUCTS.ID
                AND r.DT = 0
            )
            WHEN PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КАРТА') THEN (
                SELECT MAX(r.SUM)
                FROM ACCOUNTS a
                JOIN RECORDS r ON a.ID = r.ACC_REF
                WHERE a.PRODUCT_REF = PRODUCTS.ID
                AND r.DT = 0
            )
        END
        WHERE PRODUCT_TYPE_ID IN (
            SELECT ID FROM PRODUCT_TYPE WHERE NAME IN ('КРЕДИТ', 'ДЕПОЗИТ', 'КАРТА')
        );
        """
    )

    print(
        "Обновлены значения в столбце CONTRACT_AMOUNT для продуктов типа 'КРЕДИТ', 'ДЕПОЗИТ' и 'КАРТА' "
        "на максимальную сумму дебетовых или кредитовых операций соответственно."
    )

    conn.commit()
    conn.close()
