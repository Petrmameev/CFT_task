## Тестовое задание курса разработчика
Запуск через терминал:

Windows: 
```python main.py```

Linux:
```python3 main.py```

### Описание процесса.
Обслуживание клиента в банке начинается с заведения карточки клиента (таблица CLIENTS), далее клиент выражает завести тот или иной продукт в банке -  КРЕДИТ, ДЕПОЗИТ, КАРТА (таблица PRODUCT_TYPE). После оформления документов в банке создается экземпляр продукта (таблица PRODUCTS), в рамках продукта открывается один или несколько счетов (таблица ACCOUNTS) с остатком равным 0.
Далее в случае, если оформлен продукт типа КРЕДИТ по счету продукта проходит дебетовая операция – банк выдает деньги клиенту (в таблице RECORDS появляется запись с полем DT = 1 и суммой зачисления, запись в таблице RECORDS влияет на поле SALDO таблицы ACCOUNTS). Если оформлен продукт ДЕПОЗИТ или КАРТА по счету клиента проходит кредитовая операция – клиент вносит средства на счета (в таблице RECORDS появляется запись с полем DT = 0 и суммой зачисления, запись в таблице RECORDS влияет на поле SALDO таблицы ACCOUNTS).
После чего клиент в случае, если ему открыт продукт типа КРЕДИТ, вносит средства на счет, погашая кредит, а если продукт типа ДЕПОЗИТ или КАРТА, может списывать средства со счета. После полного погашения продукта типа КРЕДИТ, выдача кредита может происходить снова, и клиент нужно опять осуществлять погашения. Если у клиента продукта типа ДЕПОЗИТ или КАРТА, клиент в любое время может внести средства.

![image](https://github.com/user-attachments/assets/458aa32c-977c-4876-b539-2fd77eadd09a)
