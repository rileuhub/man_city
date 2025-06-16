# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'man_city'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Manchester City Premier League 24/25 season database\n\n'
                        'Type the letter for the information you want from players that have appeared at a game this season:\n'
                        'A: All information about each player\n'
                        'B: Goals from players with atleast one\n'
                        'C: Goals and shots from strikers\n'
                        'D: Saves from goal keepers\n'
                        'E: Appearences and where they are from\n'
                        'F: Stats for players under 30\n'
                        'G: Midfielder contribution\n'
                        'H: '
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all')
    if menu_choice == 'B':
        print_query('all goals')
    if menu_choice == 'C':
        print_query('strikers g/s') 
    if menu_choice == 'D':
        print_query('goalkeeper saves')
    if menu_choice == 'E':
        print_query('apps and nationality')
    if menu_choice == 'F':
        print_query('under 30 stats')
    if menu_choice == 'G':
        print_query('midfielder contribution')