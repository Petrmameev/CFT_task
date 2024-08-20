import sqlite3


def operation_in_last_month():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute(
        """
        SELECT
            c.NAME AS client_name,
            r.OPER_DATE AS operation_date,
            SUM(r.SUM) AS total_amount
        FROM
            RECORDS r
        JOIN
            ACCOUNTS a ON r.ACC_REF = a.ID
        JOIN
            PRODUCTS p ON a.PRODUCT_REF = p.ID
        JOIN
            CLIENTS c ON p.CLIENT_REF = c.ID
        WHERE
            r.OPER_DATE >= DATE('now', 'start of month', '-1 month') AND
            r.OPER_DATE < DATE('now', 'start of month')
        GROUP BY
            c.NAME,
            r.OPER_DATE
        ORDER BY
            c.NAME,
            r.OPER_DATE;
"""
    )
    results = c.fetchall()
    for row in results:
        print(
            f"Client Name: {row[0]}, Operation Date: {row[1]}, Total Amount: {row[2]}"
        )
    conn.close()
