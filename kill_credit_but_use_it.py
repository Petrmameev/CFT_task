import sqlite3


def kill_credit_but_use_it():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()

    c.execute(
        """SELECT
    c.ID AS client_id,
    c.NAME AS client_name,
    p.NAME AS product_name,
    p.OPEN_DATE AS product_open_date,
    p.CLOSE_DATE AS product_close_date,
    SUM(CASE WHEN r.DT = 1 THEN r.SUM ELSE -r.SUM END) AS total_repayment,
    COUNT(CASE WHEN r.DT = 1 THEN r.ID END) AS repayment_count,
    COUNT(CASE WHEN r.DT = 0 THEN r.ID END) AS new_credit_count
FROM
    CLIENTS c
JOIN
    PRODUCTS p ON c.ID = p.CLIENT_REF
JOIN
    ACCOUNTS a ON p.ID = a.PRODUCT_REF
JOIN
    RECORDS r ON a.ID = r.ACC_REF
WHERE
    p.PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
    AND p.CLOSE_DATE IS NULL
GROUP BY
    c.ID, c.NAME, p.NAME, p.OPEN_DATE, p.CLOSE_DATE
HAVING
    SUM(CASE WHEN r.DT = 1 THEN r.SUM ELSE -r.SUM END) >= 0
    AND COUNT(CASE WHEN r.DT = 0 THEN r.ID END) > 0;"""
    )
    result = c.fetchall()
    for row in result:
        print(
            f"Client ID: {row[0]}, Client Name: {row[1]}, Product Name: {row[2]}, "
            f"Open Date: {row[3]}, Close Date: {row[4]}, Total Repayment: {row[5]}, "
            f"Repayment Count: {row[6]}, New Credit Count: {row[7]}"
        )
    conn.close()
