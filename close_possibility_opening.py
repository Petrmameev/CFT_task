import sqlite3


def close_possibility_opening():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute(
        """
    UPDATE PRODUCT_TYPE
    SET END_DATE = CURRENT_TIMESTAMP
    WHERE ID IN (
        SELECT p.PRODUCT_TYPE_ID
        FROM PRODUCTS p
        JOIN ACCOUNTS a ON p.ID = a.PRODUCT_REF
        LEFT JOIN RECORDS r ON a.ID = r.ACC_REF
        WHERE p.CLOSE_DATE IS NULL
        GROUP BY p.PRODUCT_TYPE_ID
        HAVING MAX(r.OPER_DATE) < DATE('now', '-1 month') OR MAX(r.OPER_DATE) IS NULL
    );
    """
    )
    conn.commit()
    conn.close()
    print(
        "Функция close_possibility_opening() обновила дату окончания для всех типов продуктов, "
        "которые не имели операций более месяца или не имели операций вообще."
    )
