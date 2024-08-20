import sqlite3


def normalization():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()

    c.execute("SELECT ID, SALDO FROM ACCOUNTS")
    accounts = c.fetchall()
    print(accounts)

    for account in accounts:
        account_id = account[0]
        current_balance = account[1]
        c.execute(
            """
            SELECT SUM(CASE WHEN DT = 1 THEN -SUM ELSE SUM END) 
            FROM RECORDS 
            WHERE ACC_REF = ?
        """,
            (account_id,),
        )

        calculated_balance = c.fetchone()[0] or 0

        if calculated_balance != current_balance:
            c.execute(
                """
                UPDATE ACCOUNTS 
                SET SALDO = ? 
                WHERE ID = ?
            """,
                (calculated_balance, account_id),
            )

    conn.commit()
    conn.close()
