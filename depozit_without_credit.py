import sqlite3


def depozit_without_credit():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute(
        """
SELECT
    a.ID AS account_id,
    a.NAME AS account_name,
    a.SALDO AS account_balance,
    a.ACC_NUM AS account_number,
    p.NAME AS product_name,
    c.NAME AS client_name
FROM
    ACCOUNTS a
JOIN
    PRODUCTS p ON a.PRODUCT_REF = p.ID
JOIN
    CLIENTS c ON p.CLIENT_REF = c.ID
WHERE
    p.PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'ДЕПОЗИТ');
    """
    )
    results = c.fetchall()

    if results:
        for row in results:
            print(
                f"Account ID: {row[0]}, Account Name: {row[1]}, Balance: {row[2]}, Account Number: {row[3]}, Product Name: {row[4]}, Client Name: {row[5]}"
            )
    else:
        print("No results found.")

    conn.close()
