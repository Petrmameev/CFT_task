import sqlite3


def mean_activiti_in_day(date):
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute(
        """
        SELECT
            pt.NAME AS product_type,
            AVG(CASE WHEN r.DT = 1 THEN r.SUM ELSE 0 END) AS avg_debit,
            AVG(CASE WHEN r.DT = 0 THEN r.SUM ELSE 0 END) AS avg_credit
        FROM
            RECORDS r
        JOIN
            ACCOUNTS a ON r.ACC_REF = a.ID
        JOIN
            PRODUCTS p ON a.PRODUCT_REF = p.ID
        JOIN
            PRODUCT_TYPE pt ON p.PRODUCT_TYPE_ID = pt.ID
        WHERE
            r.OPER_DATE = ?
        GROUP BY
            pt.NAME;
        """,
        (date,),
    )

    results = c.fetchall()

    for row in results:
        print(
            f"Product Type: {row[0]}, Average Debit: {row[1]}, Average Credit: {row[2]}"
        )

    conn.close()
