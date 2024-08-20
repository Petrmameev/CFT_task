import sqlite3


def close_credit():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute(
        """UPDATE PRODUCTS
    SET CLOSE_DATE = CURRENT_TIMESTAMP
    WHERE PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
    AND CLOSE_DATE IS NULL
    AND ID IN (
        SELECT p2.ID
        FROM PRODUCTS p2
        JOIN ACCOUNTS a ON p2.ID = a.PRODUCT_REF
        JOIN RECORDS r ON a.ID = r.ACC_REF
        WHERE p2.PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
        GROUP BY p2.ID
        HAVING SUM(CASE WHEN r.DT = 1 THEN r.SUM ELSE -r.SUM END) >= 0
        AND COUNT(CASE WHEN r.DT = 0 THEN r.ID END) = 0
    );"""
    )
    conn.commit()
    conn.close()
    print(
        "Функция close_credit() обновила дату закрытия для всех кредитов, по которым выполнены "
        "следующие условия: сумма всех платежей больше или равна 0 и нет ни одного платежа с дебетом."
    )
