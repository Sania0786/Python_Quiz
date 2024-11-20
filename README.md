# Python_Quiz
# Title
Design and Implementation of a Python-based Quiz for sssessing knowledge in DSA, DBMS, and Python using File Handling.

# Abstract
Python_Quiz uses File Handling to store and retrieve questions, store user registration details, add users and check user login credentials. The quiz enables users to test their understanding of core concepts, providing immediate feedback on their performance. This research highlights the importance of file handling techniques for data persistence in software applications, offering an efficient, easy-to-maintain solution for creating educational tools.

# Introduction
Online quizzes have emerged as a popular tool for evaluating knowledge, especially in technical fields such as computer science. This research focuses on the development of a Python-based quiz that covers three important subjects: Data Structures and Algorithms (DSA), Database Management Systems (DBMS), and Python programming.
File handling is a critical component of the system, enabling the storage, retrieval, and modification of quiz questions, user data, and results. The application not only evaluates knowledge but also demonstrates the practical application of file handling in Python for developing educational tools.

# Problem Statement
The goal of this research is to design a Python-based quiz that:

Covers fundamental topics in DSA, DBMS, and Python.
Stores quiz data (questions) in text files for data persistence.
Allows for easy maintenance and modification of questions through file-based storage. The challenge is to efficiently handle file operations while ensuring the system remains user-friendly.
Literature Review
File handling is an essential technique in many educational software systems, especially in scenarios where the data (questions and user details) needs to be persistently stored. Python provides a simple yet powerful interface for file manipulation, which is utilized in this project to handle both structured and unstructured data (such as questions and user details).

# Methodology
DATA STRUCTURES : Data Strcutures such as lists are used to store answers to quiz questions.
FILE HANDLING : The File Handling component is the backbone of the system. The quiz reads questions from text files and writes the user details in text files to store it.
• Question bank file - Three files containing questions of each DBMS, DSA and Python.
• User details - A file storing user credentials during registration.
IMPLEMENTATION : The quiz is implemented in Python, utilizing file operations such as reading (open(), read(), readlines()) and writing (write(), writelines()) to interact with text files. Key functions implemented include:
‣ register() - To register user and his/her details.
‣ login() - To check login credentials of user.
‣ attemptquiz() - To attempt quiz.
‣ showresult() - To calculate quiz result.
‣ exit() - To exit from quiz.
# Conclusion
In conclusion, this research demonstrates the utility of file handling in building an interactive, scalable quiz system for evaluating knowledge in computer science subjects. By using Python’s built-in file handling capabilities, the system offers a simple yet effective solution for storing and retrieving quiz data.

Future Scope
There is no as such future scope of this quiz but enhances our file handling concepts and problem solving skills.

