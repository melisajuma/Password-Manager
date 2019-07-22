# Password-Manager

Password-Manager is a python CLI (command line interface) application that manages passwords for different accounts and relieves the user of the burden of managing very many passwords. Password manager enables one to: generate a randomn password(s), delete or view existing passwords or simply have a display of all the stored passwords.

## Author
Melisa JUma™ (9/07/2019)


## User Stories

These are the behaviours/features that the application implements:

As a user I would like to:

***Create an account with my details i.e log in and password
***Store my existing login credentials
***Generate a password for a new credential/account

# BDD

|Behaviour                     | input example       |  output example    |
| :---------------------------:|--------------------:| ------------------:|
| Sign up                      | input account       | select option      |
| generate a password          | input gen           | password created   |
| add an existing password     | input add           | password added     |
| view passwords | input view  | input view          | password list      |
| delete password password     | input del           | password deleted   |
| exit to leave :( password    | input exit          | Please stay, Bye   |



## SetUp / Installation Requirements
You Need to Install the Following in order for the application to work

*python3.6
*pip
*pyperclip

# Cloning
In your terminal:

*** $ git clone https://github.com/melisajuma/Password-Manager.git

*** $ cd Password-Manager

Running the Application

# To run the application, in your terminal:

*** $ chmod +x run.py
*** $ ./run.py

# Testing the Application

To run the tests for the class file:

$ python3.6 Password_Locker_test.py

## Technologies Used
Python3.6
License
MIT ©2019 Melisa JUma

Melisa JUma