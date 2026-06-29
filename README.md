# 🔐 Generated password manager

This project generates passwords and saves them to a database with a name of your choice. This helps eliminate the use of repetitive passwords and prevents issues with forgetting or losing them.

---

## 🔥 Why I Built This & Features

* **Genuinely Secure:** Generates unpredictable, randomized passwords based on your own rules.
* **100% Local & Safe:** Everything runs completely offline on your computer. Your passwords never touch the internet, so your data stays yours.
* **Auto-Save:** No more messy text files — it automatically logs your passwords into a local SQLite database.

---
## 🛠 Behind the Scenes (Code Structure)

Here is a quick look at how the script is organized and what happens under the hood:

1. **Module Imports:** Grabs Python's built-in libraries (`random`, `string`, and `sqlite3`) to power the script without needing any external installations.
2. **Database Setup:** Automatically checks for a local database file and sets up the `credentials` table if it doesn't exist yet.
3. **User Input / Variables:** Interactively asks you for the website name, password length, and your security preferences (numbers/symbols).
4. **Character Pool Formation:** Dynamically builds a custom "pool" of characters based on the preferences you selected in the previous step.
5. **Password Generation & Saving:** Randomly picks characters from the pool to generate your password, logs it into the database with the website name, and shows it on your screen.

---

## 🚀 How to Run It

### Prerequisites
You only need Python 3 installed. No extra packages required!

### Running the Script
1. Download or clone the script into a folder.
2. Open your terminal (or Command Prompt) in that folder.
3. Run the following command:

```bash
python generator.py

## 📈 What's Next? (Roadmap)

This is just the first version! Here are some cool features I'm planning to add next to make this tool even better:

* [ ] **View Menu:** Add an option at startup to actually read and search your saved passwords directly from the terminal.
* [ ] **Auto-Copy to Clipboard:** Automatically copy the newly generated password so you can just press `Ctrl+V` on the website.
* [ ] **Password Encryption:** Scramble the passwords inside the `passwords.db` file using the `cryptography` library so they aren't stored in plain text.
* [ ] **Modern GUI:** Move away from the command line and build a clean, modern desktop window using `customtkinter`.