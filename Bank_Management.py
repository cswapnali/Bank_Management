import mysql.connector 

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'mysql123', autocommit = True)
cur_ = conn.cursor()
cur_.execute("CREATE DATABASE IF NOT EXISTS bank_database")
cur_.execute("USE bank_database")
#creating tables
cur_.execute("CREATE TABLE IF NOT EXISTS bank_account(Acc_no INT AUTO_INCREMENT PRIMARY KEY, Name varchar(30), City char(20), Contact_no char(10), Balance int(10))")

print('-----------WELCOME TO BANK APP-----------')
while True:
    print('1. CREATE ACCOUNT\n2. DEPOSIT AMOUNT\n3. WITHDRAW MONEY\n4. SHOW BALANCE')
    ch = int(input('Action which you want to perform: '))
    #create new account
    if ch == 1:
        name = input('Enter your Name: ')
        city = input('Enter City Name: ')
        phone = input('Enter Mobile no.: ')
        balance = 0
        sql = "INSERT INTO bank_account(Name, City, Contact_no, Balance) values (%s, %s, %s, %s)"
        val = (name, city, phone, balance)
        cur_.execute(sql, val)
        cur_.execute("SELECT * FROM bank_account WHERE Name = '" + name + "'")
        print('Account created successfully!')
        for i in cur_:
            print(i)
        print('*******************************************************************************************************')

    #deposit amount
    elif ch == 2:
        acc_no = input('Enter account number: ')
        da = int(input('Enter amount to be deposited: '))
        cur_.execute("UPDATE bank_account SET Balance = Balance + '" + str(da) + "' WHERE Acc_no = '" + acc_no + "'")
        print('Amount of Rs.', da, 'has been deposited successfully in Account no:', acc_no)
        print('*******************************************************************************************************')
    
    #withdraw amount
    elif ch == 3:
        acc_no = input('Enter account number: ')
        wa = int(input('Enter amount you want to withdraw: '))
        select_query = "SELECT Balance FROM bank_account WHERE Acc_no = '" +acc_no+ "'"
        cur_.execute(select_query)
        bal = cur_.fetchone()[0]
        if wa < bal:
            cur_.execute("UPDATE bank_account SET Balance = Balance - '" +str(wa)+ "' WHERE Acc_no = acc_no")
            print('Amount of Rs.', wa, 'has been withdrawn successfully from Account no', acc_no)
            print('*******************************************************************************************************')
        else:
            print('Insufficient Balance!')
            print('*******************************************************************************************************')
    
    #show balance
    elif ch == 4:
        acc_no = input('Enter account number: ')
        cur_.execute("SELECT Name, Balance FROM bank_account WHERE Acc_no = '" +acc_no+ "'")
        for i in cur_:
            print(i)
        print('*******************************************************************************************************')
        
    else:
        print('Please Enter valid correct action!')
