# ACIT2911 Agile Project - ExpendAware
This is an agile development project for the ACIT2911 agile development course. Our group is named "One Byte" and our project is a mobile expense tracker application. 
## Functionality
ExpendAware allows users to keep track of their expenses by organizing them into different categories. Each category can have multiple budgets and it is up to the user to decide. The user can add expenses to each budget, and the app will keep track of the expenses and let the user know of when they have gone over budget. 

The user is able to log in to their own account and keep their expenses to themselves. On the homepage, they are able to see their total budgets and expenses overall, their most recent transactions, and a summary of their categories. Users can view their categories by going to the category page. There, they can see a list of all their categories and the total budget for each category. They can see their budgets within each category and can click on a budget to view their expenses for that budget. They can see a list of all their expenses they've added as well as a remaining amount. The user can also transfer between budgets to take away from one budget and add to the other. 

## Requirements
### Software Requirements
* Python 3.7 or newer
* Flask Web Framework

### Hardware Requirements
* Any modern computer (Windows, Mac, Linux) or mobile device with internet access

## Configuring the App

**Note:**
* The following configuration instructions are for deploying a local development
version of the app. The configuration steps for the app below assume the user is
using Visual Studio Code as the editor.

**To configure the app**

1. Download the ExpendAware project files from this GitHub Repository:
https://github.com/KodyMillar/ACIT2911.git
2. Launch the command prompt or terminal.
3. Navigate to the location of the downloaded files via "cd".
4. Create a virtual environment in your editor (eg. python -m venv venv).
5. Ensure the virtual environment is activated (eg. on Windows:
.\venv\Scripts\activate, on Mac/Linux: source venv/bin/activate).
6. Install necessary dependencies using pip. Type the following commands into
your command prompt or terminal:
* pip install flask
* pip install flask-login
Note: To run pytests, install pytest with: pip install pytest and run tests using:
pytest test_main.py
7. Launch the application by typing the command flask run in your terminal or
command prompt or run python main.py (with an active virtual environment)
8. Navigate to the local server address displayed (usually http://127.0.0.1:5000/)
in a web browser to use the application
