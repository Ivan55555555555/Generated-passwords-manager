#1. Module imports
import random #For generating passords
import string #For specail symbols and numbers in passwords
import sqlite3 #Database

#2. Database setup / Creating database
connect = sqlite3.connect("Manager-passwords.db")
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
connect.commit()

print("Strong passwords generator")

#3. User input / Variables
app_name = input("What website/service does a password need? (for example, Google): ")
length = int(input("Enter the passwword length (for example, 12): "))
include_numbers = input("Enable numbers? (y/n): ").lower() == "y"
include_symblos = input("Enable special symbols? (y/n): ").lower() == "y"

#4. Character pool informations
chars = string.ascii_letters
#string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
if include_numbers:
    chars += string.digits
if include_symblos:
    chars += string.punctuation

#5. Password generation and saving him in database
password = "".join(random.choice(chars) for s in range(length))
cursor.execute(
    "INSERT INTO credentials (site, password) VALUES (?, ?)", 
    (app_name, password)
)
connect.commit()
connect.close()
print(f"\n[Success] Your strong password for '{app_name}' generated and successly saved in database: ")
print(f"👉 {password}")