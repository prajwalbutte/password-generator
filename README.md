# 🔐 Password Generator (Python Beginner Project)

This is a simple Python project I built while learning how to generate secure passwords. It uses Python’s built-in random and string modules to create strong, random passwords of user-defined length.

---

## ⚙️ How It Works

- The program asks the user to enter the desired *length* of the password.
- If the length is *greater than 5*, it:
  - Combines letters (A-Z, a-z), digits (0-9), and symbols (!@#$...)
  - Randomly selects characters from all of them
  - Displays the generated password
- If the length is too short (≤5), it shows a warning.

---

## 🧠 What I Practiced

- Using random.sample() for random character selection  
- Using string.ascii_letters, string.digits, string.punctuation  
- Taking user input and converting it using int()  
- Conditional checks with if-else  
- Printing formatted output using f-strings

---
## Example Output
Welcome to my Project 'PASSWORD GENERATOR'
Enter length of password: 10

Your secure password is:
&8dJ#Xz@pW
---

