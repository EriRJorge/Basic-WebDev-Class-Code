"""
========================================
CYBERSECURITY PROJECT — PASSWORD ANALYZER
========================================

PROJECT GOAL:
You will create a Python program that:
1. Lets a user enter a password
2. Checks the password for common security rules
   (length, uppercase, lowercase, number, special character)
3. Gives a rating: WEAK, MEDIUM, or STRONG
4. Suggests improvements for weak passwords
5. Simulates “updating a website” (just prints a message)

This project is designed for students **who do not know Python**, so follow instructions carefully.

-------------------------------------------------
STEP 0: SET UP PYTHON
-------------------------------------------------
1. Go to https://www.python.org/downloads/
2. Download the version labeled **Python 3.x**
3. Install it with all default options
4. Open a terminal or command prompt
5. Test installation by typing:
    python --version
   You should see a version number, e.g., Python 3.11.x
6. If using Mac or Linux, try:
    python3 --version

-------------------------------------------------
STEP 1: CREATE YOUR FILE
-------------------------------------------------
1. Create a folder for this project (e.g., PasswordAnalyzer)
2. Inside that folder, create a new file called:
    analyzer.py
3. Open the file in a code editor (VS Code, PyCharm, or even Notepad)

-------------------------------------------------
STEP 2: UNDERSTAND THE TASK
-------------------------------------------------
Your program will:
- Ask the user to type a password
- Check for 5 rules:
  1. At least 8 characters
  2. At least 1 uppercase letter
  3. At least 1 lowercase letter
  4. At least 1 number
  5. At least 1 special character (e.g., !@#$%)
- Count how many rules are satisfied
- Give a rating:
  - 5 rules → STRONG
  - 3–4 rules → MEDIUM
  - 0–2 rules → WEAK
- Suggest improvements if the password is weak
- Print a message simulating a “website update”

-------------------------------------------------
STEP 3: BREAK TASK INTO SMALL PIECES
-------------------------------------------------
Even if you don’t know Python yet, you can plan:

1. INPUT
   - Ask the user to type a password
   - Use: input("Enter a password: ")

2. CHECK RULES
   - Check each rule separately
   - Example (pseudocode):
       if length >= 8: good
       if contains uppercase letter: good
       etc.

3. COUNT RULES PASSED
   - Add 1 point for each rule passed
   - Total score = 0 to 5

4. RATING
   - If score = 5 → STRONG
   - If score 3–4 → MEDIUM
   - Else → WEAK

5. SUGGESTIONS
   - For each rule not met, print a suggestion

6. SIMULATED WEBSITE UPDATE
   - Print: "Simulated update: your password would be updated on the website"

-------------------------------------------------
STEP 4: RUNNING THE PROGRAM
-------------------------------------------------
1. Open terminal
2. Navigate to your project folder:
   - Windows: cd path\to\PasswordAnalyzer
   - Mac/Linux: cd /path/to/PasswordAnalyzer
3. Run your program:
   python analyzer.py
4. Type a password when prompted
5. See the rating, suggestions, and simulated update

-------------------------------------------------
STEP 5: RESOURCES FOR BEGINNERS
-------------------------------------------------
Python Basics:
- https://www.w3schools.com/python/
- https://www.learnpython.org/

User Input:
- https://www.w3schools.com/python/ref_func_input.asp

If Statements:
- https://www.w3schools.com/python/python_conditions.asp

Strings and Text:
- https://www.w3schools.com/python/python_strings.asp

Loops (optional for advanced):
- https://www.w3schools.com/python/python_for_loops.asp

Regular Expressions (optional):
- https://www.w3schools.com/python/python_regex.asp

-------------------------------------------------
STEP 6: OPTIONAL CHALLENGES
-------------------------------------------------
- Let the user test multiple passwords in a loop
- Store tested passwords in a text file
- Check against a list of common passwords (from the internet)
- Color the output using print statements for fun

-------------------------------------------------
IMPORTANT NOTES
-------------------------------------------------
- Never attempt to change a real website’s password. 
  The “update website” step is only a print message.
- Focus on Python basics first:
  - Input, output, conditions, variables, functions
- Comment your code to explain what each part does
- Test your program with different types of passwords
"""
