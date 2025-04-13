'''
-----------------------------------------------------------------------------
-------------------------- KENDRIYA VIDYALAYA DRDO --------------------------
-------------------------- HOTEL MANAGEMENT SYSTEM --------------------------
-----------------------------------------------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~ Hôtel Grandé da Louvre ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Designed and Maintained by:
    R.S. MOUMITHA  - CLASS XII A - ROLL NO - 12109 [2020-2021]
    ROHAN SANTHOSH - CLASS XII A - ROLL NO - 12130 [2020-2021]
    SUMIT PRASAD   - CLASS XII A - ROLL NO - 12136 [2020-2021]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------------------------------
''' 

import mysql.connector

# GLOBAL VARIABLES DECLARATION
mycon=""
cursor=""
userName=""
password =""
room_rent =0
restaurant_bill=0
totalAmount=0
cid=""

# MODULE TO CHECK MYSQL CONNECTIVITY AND CREATE/CHECK EXISTENCE OF REQUIRED DATABASE
def MYSQLconnectionCheck ():
       global mycon
       global userName
       global password
       userName = input("\nENTER MySQL SERVER'S USERNAME: ")
       password = input("\nENTER MySQL SERVER'S PASSWORD: ")
       mycon=mysql.connector.connect(host="localhost", user=userName, passwd=password, auth_plugin='mysql_native_password' )
       if mycon:
              print("\nMySQL CONNECTION ESTABLISHED SUCCESSFULLY!")
              cursor=mycon.cursor()
              cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
              cursor.execute("COMMIT")
              cursor.close()
              return mycon
       else:
              print("\nERROR ESTABLISHING MySQL CONNECTION. RECHECK USERNAME AND PASSWORD !")

# MODULE TO CONNECT TO REQUIRED DATABASE
def MYSQLconnection ():
       global userName
       global password
       global mycon
       global cid
       mycon=mysql.connector.connect(host="localhost", user=userName, passwd=password, database="HMS", auth_plugin='mysql_native_password' )
       if mycon:
              print('Running database "HMS".')
              return mycon
       else:
              print("\nERROR ESTABLISHING MySQL CONNECTION !")
              mycon.close()
              
def guest_details():
       global cid
       if mycon:
              cursor=mycon.cursor()
              createTable ="""CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),
                              C_NAME VARCHAR(30), C_ADDRESS VARCHAR(30), C_AGE VARCHAR(30),
                              C_COUNTRY VARCHAR(30), P_NO VARCHAR(30), C_EMAIL VARCHAR(30))"""
              cursor.execute(createTable)
              cid = input("Enter Guest Identification Number: ")
              name = input("Enter Guest Name: ")
              address = input("Enter Guest Address: ")
              age = input("Enter Guest Age: ")
              nationality = input("Enter Guest Country: ")
              phone_no = input("Enter Guest Contact Number: ")
              email = input("Enter Guest E-mail: ")
              sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
              values = (cid,name,address,age,nationality,phone_no,email)
              cursor.execute(sql,values)
              cursor.execute("COMMIT")
              print("\nNew Guest Registered Successfully!")
              cursor.close()
       else:
              print("\nERROR ESTABLISHING MySQL CONNECTION !")
              
def booking():
       global cid
       customer = guest_search()
       if customer:
              if mycon:
                     cursor = mycon.cursor()
                     createTable = "CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20), CHECK_IN DATE, CHECK_OUT DATE)"
                     cursor.execute(createTable)
                     checkin = input("\nEnter Guest Check-in Date [YYYY-MM-DD] : ")
                     checkout = input("\nEnter Guest Check-out Date [YYYY-MM-DD] : ")
                     sql = "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
                     values = (cid,checkin,checkout)
                     cursor.execute(sql,values)
                     cursor.execute("COMMIT")
                     print("\nCHECK-IN AND CHECK-OUT ENTRIES MADE SUCCESSFULLY!")
                     cursor.close()
       else:
              print("\nERROR ESTABLISHING MySQL CONNECTION!")

def room_rent():
       global cid
       customer=guest_search()
       if customer:
              global room_rent
              if mycon:
                     cursor=mycon.cursor()
                     createTable ="""CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20), ROOM_CHOICE INT, NO_OF_DAYS INT, room_no INT, room_rent INT)"""
                     cursor.execute(createTable)
                     print("""
\n^^^^^^^^^^ We Have The Following Rooms For You ^^^^^^^^^^
---------------------------------------------------------
    1. Ultra Royal - 10,000 INR
    2. Royal - 5,000 INR
    3. Elite - 3,500 INR
    4. Budget - 2,500 INR
---------------------------------------------------------
""")
                     room_choice =int(input("Enter Your Option : "))
                     room_no=int(input("Enter Customer Room No : "))
                     no_of_days=int(input("Enter No. Of Days : "))
                     if room_choice==1:
                            room_rent = no_of_days * 10000
                            print("\nUltra Royal Room Rent: ",room_rent)
                     elif room_choice==2:
                            room_rent = no_of_days * 5000
                            print("\nRoyal Room Rent: ",room_rent)
                     elif room_choice==3:
                            room_rent = no_of_days * 3500
                            print("\nElite Room Rent: ",room_rent)
                     elif room_choice==4:
                            room_rent = no_of_days * 2500
                            print("\nBudget Room Rent: ",room_rent)
                     else:
                            print("Invalid Input. Please Try Again!")
                            return
                     sql= "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
                     values= (cid,room_choice,no_of_days,room_no,room_rent,)
                     cursor.execute(sql,values)
                     cursor.execute("COMMIT")
                     print("Thank You! Your room has been booked for: ",no_of_days," days.")
                     print("Your total room rent is: ",room_rent," INR.")
                     cursor.close()
       else:
              print("\nERROR ESTABLISHING MySQL CONNECTION !")
              
def Restaurant():
       global cid
       customer=guest_search()
       if customer:
              global restaurant_bill
              if mycon:
                     cursor=mycon.cursor()
                     createTable ="""CREATE TABLE IF NOT EXISTS Restaurant(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"""
                     cursor.execute(createTable)
                     print("""
\n^^^^^^^^^^ We Have The Following Cuisine For You ^^^^^^^^^^
-----------------------------------------------------------
    1. Vegetarian Combo - 300 INR
    2. Non-Vegetarian Combo - 500 INR
    3. Veg & Non-Veg Combo - 750 INR
-----------------------------------------------------------
""")
                     choice_dish = int(input("Enter Your Cusine : "))
                     quantity=int(input("Enter Quantity : "))
                     if choice_dish==1:
                            print("\nYOUR ORDER IS: Vegetarian Combo.")
                            restaurant_bill = quantity * 300
                     elif choice_dish==2:
                            print("\nYOUR ORDER IS: Non-Vegetarian Combo.")
                            restaurant_bill = quantity * 500
                     elif choice_dish==3:
                            print("\nYOUR ORDER IS: Veg & Non-Veg Combo.")
                            restaurant_bill= quantity * 750
                     else:
                            print("Invalid Input. Please Try Again!")
                            return
                     sql= "INSERT INTO Restaurant VALUES(%s,%s,%s,%s)"
                     values= (cid,choice_dish,quantity,restaurant_bill)
                     cursor.execute(sql,values)
                     cursor.execute("COMMIT")
                     print("Your Total Bill Amount Is : Rs. ",restaurant_bill)
                     print("\n^^^^^^^^^^ HOPE YOU ENJOY YOUR MEAL! ^^^^^^^^^\n")
                     cursor.close()
       else:
              print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def totalAmount():
       global cid
       customer=guest_search()
       if customer:
              global grandTotal
              global room_rent
              global restaurant_bill
              if mycon:
                     cursor=mycon.cursor()
                     createTable ="""CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20),C_NAME
                              VARCHAR(30),room_rent INT ,restaurant_bill INT ,TOTALAMOUNT INT)"""
                     cursor.execute(createTable)
                     sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s)"
                     name = input("Enter Guest Name : ")
                     grandTotal=room_rent + restaurant_bill 
                     values= (cid,name,room_rent,restaurant_bill,grandTotal)
                     cursor.execute(sql,values)
                     cursor.execute("COMMIT")
                     cursor.close()
                     print("""
\n-------------------------------------------------------------------
~~~~~~~~~~~~~~~~~~~~~ Hôtel Grandé da Louvre ~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~ Customer Billing ~~~~~~~~~~~~~~~~~~~~~~~~~
""")
                     print("Customer Name: " ,name)
                     print("Room Rent: ",room_rent,"INR")
                     print("Restaurant Bill: ",restaurant_bill,"INR")
                     print("--------------------------------------------")
                     print("TOTAL AMOUNT : ",grandTotal,"INR")
                     print("""
-------------------------------------------------------------------
""")
                     cursor.close()
              else:
                     print("\nERROR ESTABLISHING MY=ySQL CONNECTION !")

def guest_search():
       global cid
       if mycon:
              cursor = mycon.cursor()
              cid = input("ENTER GUEST ID: ")
              sql = "SELECT * FROM C_DETAILS WHERE CID= %s"
              cursor.execute(sql,(cid,))
              data = cursor.fetchall()
              if data:
                     print(data)
                     return True
              else:
                     print("Record Not Found. Please Enter Valid ID!")
                     return False
                     cursor.close()

       else:
              print("\nERROR ESTABLISHING MySQL CONNECTION!")
 
#__main__
              
print('''
-----------------------------------------------------------------------------
------------------------- KENDRIYA VIDYALAYA DRDO ---------------------------
------------------------- HOTEL MANAGEMENT SYSTEM ---------------------------
-----------------------------------------------------------------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~ Hôtel Grandé da Louvre ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Designed and Maintained by:
    R.S. MOUMITHA  - CLASS XII A - ROLL NO - 12109 [2020-2021]
    ROHAN SANTHOSH - CLASS XII A - ROLL NO - 12130 [2020-2021]
    SUMIT PRASAD   - CLASS XII A - ROLL NO - 12136 [2020-2021]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-----------------------------------------------------------------------------
''')

mycon = MYSQLconnectionCheck ()
if mycon:
       MYSQLconnection ()
       while True:
             print("""
**************************************************
    Press |         To
   -------+----------------------------
      1   | Enter Guest Details.
      2   | Enter Booking Details.
      3   | Calculate Room Rent.
      4   | Calculate Restaurant Bill.
      5   | Display Guest Details.
      6   | Generate Total Bill Amount.
      7   | Finish Up and Exit.
**************************************************
""")
             choice = int(input("Select the required operation: "))
             if choice == 1:
                     guest_details()
             elif choice == 2:
                     booking()
             elif choice == 3:
                     room_rent()
             elif choice == 4:
                     Restaurant()
             elif choice == 5:
                     guest_search()
             elif choice == 6:
                     totalAmount()
             elif choice == 7:
                     break
             else:
                     print("Invalid input. Please try again!")
       print("Hôtel Grandé da Louvre management system shutting down...")
else:
        print("\nERROR ESTABLISHING MySQL CONNECTION!")
# END OF PROJECT 
