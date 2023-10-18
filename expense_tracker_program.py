'''
Project Title: Expense Tracker
Project Description: Create a simple command-line expense tracker application in Python
that allows users to manage their expenses, keep track of spending categories, and
generate basic financial reports. This project will involve working with data structures and
file handling.
Key Features you can include :
Add expenses: Allow users to input expenses, including the expense amount, category
(e.g., groceries, transportation, entertainment), and a brief description.
List expenses: Display a list of all recorded expenses with details like date, amount,
category, and description.
Expense categories: Implement expense categories to help users organize their
spending.
Calculate total expenses: Calculate and display the total expenses for a specified time
frame (e.g., daily, weekly, monthly).
Monthly reports: Generate and display a monthly report that summarizes expenses by
category.
Save data: Store expense data in a text file, allowing users to retrieve their financial
history even after closing the program.
Load data: Enable users to load their saved expense data from the text file when they
start the program.
'''

#importing the libraries
import mysql.connector
import random
from datetime import date, timedelta
from rich.console import Console
from rich.table import Table

class expense_tracker:
    def __init__(self):
        pass
    def add_expense(self):
        try:
            print("you have chosen to add your expense")
            expense_category=input("enter the category of expense : ")
            expense_amount=int(input("enter the expense amount : "))
            expense_description=input("enter the description of expense(if any) : ")
            database_cursor.execute(f"insert into expense_tracker values('{expense_category}', '{expense_amount}', '{expense_description}', '{str(date.today())}')")
            sql_database.commit()
            print("Your expense is added to the list")
            print("================================================================")
        except:
            print("An error encountered")
    def view_expenses(self):
        try:
            database_cursor.execute("select *from expense_tracker")
            expense_records_tuple=database_cursor.fetchall()
            #print(expense_records_tuple)
            '''
            print("Expense")
            for i in expense_records_tuple:
                print(i[3],"\t",i[0],"\t",i[1],"\t",i[2])
            '''
            table = Table(title="View Expenses")
            columns = ["Expense_category", "Expense_amount", "Expense_description", "Date"]

            for column in columns:
                table.add_column(column)

            for row in expense_records_tuple:
                table.add_row(*row, style='bright_green')

            console = Console()
            console.print(table)
            print("================================================================")
        except:
            print("An error encountered")

    def expense_categories(self):
        try:
            database_cursor.execute("select expense_category, sum(expense_amount) from expense_tracker group by expense_category")
            expense_records_tuple=database_cursor.fetchall()#need to add table
            table = Table(title="View Total expense of each category")
            columns = ["Expense_category", "Expense_amount"]
            expense_records_tuple=list(expense_records_tuple)
            #print(expense_records_tuple)
            expense_records_tuple2=[]
            for i in expense_records_tuple:
                expense_records_tuple2.append([i[0],str(i[1])])
            print(expense_records_tuple2)
            for column in columns:
                table.add_column(column)

            for row in expense_records_tuple2:
                table.add_row(*row, style='bright_green')

            console = Console()
            console.print(table)
            print("================================================================")
        except:
            print("An error encountered")

    def calculate_total_expense(self):
        try:
            print("What expenses do you want to see : ")
            print("Press 1 to Current day ")
            print("Press 2 to Weekly")
            print("Press 3 to Monthly")
            print("Press 4 to go back to menu")
            userinput=int(input("Enter the choice : "))
            currentday = date.today()
            days_before7 = (date.today() - timedelta(days=7)).isoformat()
            days_before30 = (date.today() - timedelta(days=30)).isoformat()
            if(userinput==1):
                database_cursor.execute(f"select * from expense_tracker where date='{currentday}'")
                currentdayrecords=database_cursor.fetchall()
                currentdayrecords2 = []
                for i in currentdayrecords:
                    currentdayrecords2.append([i[0], str(i[1]),i[2],i[3]])
                table = Table(title="View Today's expense")
                columns = ["Expense_category", "Expense_amount", "Expense_description", "Date"]

                for column in columns:
                    table.add_column(column)

                for row in currentdayrecords2:
                    table.add_row(*row, style='bright_green')

                console = Console()
                console.print(table)

            elif(userinput==2):
                database_cursor.execute(f"select *from expense_tracker where date between '{days_before7}'and '{currentday}'")
                weeklyrecords=database_cursor.fetchall()
                weeklyrecords2 = []
                for i in weeklyrecords:
                    weeklyrecords2.append([i[0], str(i[1]),i[2],i[3]])
                table = Table(title="View Weekly expense")
                columns = ["Expense_category", "Expense_amount", "Expense_description", "Date"]

                for column in columns:
                    table.add_column(column)

                for row in weeklyrecords2:
                    table.add_row(*row, style='bright_green')

                console = Console()
                console.print(table)

            elif(userinput==3):
                database_cursor.execute(f"select *from expense_tracker where date between '{days_before30}'and '{currentday}'")
                monthlyrecords = database_cursor.fetchall()
                monthlyrecords2 = []
                for i in monthlyrecords:
                    monthlyrecords2.append([i[0], str(i[1]),i[2],i[3]])
                table = Table(title="View Monthly expense")
                columns = ["Expense_category", "Expense_amount", "Expense_description", "Date"]

                for column in columns:
                    table.add_column(column)

                for row in monthlyrecords2:
                    table.add_row(*row, style='bright_green')

                console = Console()
                console.print(table)

            elif(userinput==4):
                pass
            print("================================================================")
        except:
            print("An error encountered")

    def monthly_reports(self):
        try:
            currentday = date.today()
            days_before30 = (date.today() - timedelta(days=30)).isoformat()
            database_cursor.execute(f"select *from expense_tracker where date between '{days_before30}'and '{currentday}'")
            monthlyrecords = database_cursor.fetchall()
            monthlyrecords2 = []
            for i in monthlyrecords:
                monthlyrecords2.append([i[0], str(i[1]),i[2],i[3]])
            table = Table(title="View Monthly expense")
            columns = ["Expense_category", "Expense_amount", "Expense_description", "Date"]

            for column in columns:
                table.add_column(column)

            for row in monthlyrecords2:
                table.add_row(*row, style='bright_green')

            console = Console()
            console.print(table)
            print("================================================================")
        except:
            print("An error encountered")
if __name__ == '__main__':
    userchoice=0

    #mysql connection is established
    sql_database=mysql.connector.connect(user="root", password="root123", host="127.0.0.1", database="expense_tracker")
    database_cursor=sql_database.cursor()

    #object creation
    expense_tracker_object=expense_tracker()


    print("================================================================")
    print("=*=*=*=*========== Welcome to Expense Tracker ==========*=*=*=*=")
    print("================================================================")
    while(1==1):
        try:
            print("Choose the desired option from the menu")
            print("Press 1 to Add an expense")
            print("Press 2 to list the expenses")
            print("Press 3 to categorize expenses")
            print("Press 4 to Check Current Day's/Weekly/Monthly records")
            print("Press 5 to get Monthly records")
            print("Press 6 to exit ")
            print("================================================================")
            userchoice=int(input("Enter the Choice you want to enter : "))
            if(userchoice==1):
                expense_tracker_object.add_expense()
            elif(userchoice==2):
                expense_tracker_object.view_expenses()
            elif(userchoice==3):
                expense_tracker_object.expense_categories()
            elif(userchoice==4):
                expense_tracker_object.calculate_total_expense()
            elif(userchoice==5):
                expense_tracker_object.monthly_reports()
            elif(userchoice==6):
                break
            else:
                print("Wrong choice entered. try again")
        except:
            print("An error encountered")
    print("Thank you for using the Application")