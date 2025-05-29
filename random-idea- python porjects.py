import random  # import random module to genrate random ideas
ideas = [

    "Simple Calculator (Addition, Subtraction, Multiplication, Division)",
    "Number Guessing Game",
    "Rock, Paper, Scissors Game (Player vs. Computer)",
    "Dice Rolling Simulator",
    "Temperature Converter (Celsius to Fahrenheit and vice-versa)",
    "Unit Converter (e.g., Kilometers to Miles, Kilograms to Pounds)",
    "Basic To-Do List (Console-based, add, view, remove tasks)",
    "Palindrome Checker",
    "Word Counter (Counts words in a given string or text file)",
    "Vowel and Consonant Counter in a String",
    "Simple Interest Calculator",
    "Countdown Timer (Console-based)",
    "Email Slicer (Extract username and domain from an email address)",
    "Story Generator (Mad Libs style)",
    "BMI (Body Mass Index) Calculator",
    "Even or Odd Number Checker",
    "Leap Year Checker",
    "Simple Password Generator (random characters, specified length)",
    "Find the Largest/Smallest Number in a List",
    "Basic Contact Book (Store name and number in a dictionary, console I/O)",
    "Text File Reverser (Reads a file, writes its content in reverse to another)",
    "FizzBuzz Game Implementation",
    "Fibonacci Sequence Generator (up to N numbers)",
    "Prime Number Checker",
    "Character Frequency Counter in a String",
    "Simple Alarm Clock (Prints a message at a set time, console)",
    "Heads or Tails Coin Flip Simulator",
    "Basic Quiz Game (Questions and answers stored in lists/dictionaries)",
    "Digital Clock (Console, updates every second)",
    "File Line Counter",
    "Text-based Adventure Game (Very simple, 2-3 rooms)",
    "Tip Calculator",
    "Area and Perimeter Calculator for Shapes (Square, Rectangle, Circle)",
    "To-Do List with File Persistence (Save/Load tasks from JSON/CSV)",
    "Contact Book with Search/Edit/Delete (Save/Load from JSON/CSV)",
    "Web Scraper (e.g., Scrape headlines from a news website using BeautifulSoup)",
    "API Client (e.g., Get weather data from OpenWeatherMap API)",
    "URL Shortener (In-memory or simple file-based storage)",
    "Simple Chatbot (Rule-based responses)",
    "Hangman Game (Console or basic GUI with Tkinter)",
    "Tic-Tac-Toe Game (Console or basic GUI with Tkinter, Player vs. Player or Player vs. AI)",
    "Basic Image Editor (e.g., Resize, convert to grayscale using Pillow)",
    "Markdown to HTML Converter (Basic tags)",
    "Pomodoro Timer with GUI (Tkinter/PyQt)",
    "File Organizer (Sorts files in a directory into subfolders based on extension)",
    "Password Manager (Console-based, with basic encryption like Fernet)",
    "Sudoku Solver (Using backtracking algorithm)",
    "Music Player (Console-based, plays local MP3 files using a library like `playsound` or `pygame.mixer`)",
    "Typing Speed Test Application (Console or GUI)",
    "Plagiarism Checker (Compares two text files for similarity)",
    "Expense Tracker (Console or basic GUI, saves data to CSV/JSON)",
    "Simple Blog System (Console-based, posts stored as text files)",
    "Random Quote Generator with API and GUI Display",
    "Minesweeper Game (Console or basic GUI)",
    "Conway's Game of Life (Console or basic GUI)",
    "Weather Application with GUI (using Tkinter and an weather API)",
    "Basic Stock Price Tracker (Using an API like Alpha Vantage or Yahoo Finance)",
    "Regex Query Tool (GUI to test regular expressions against text)",
    "Simple Web Server (Using Python's `http.server` module to serve local files)",
    "Barcode/QR Code Generator and Reader",
    "Folder Synchronizer (One-way sync between two folders)",
    "Snake Game (Using Pygame)",
    "PDF Merger/Splitter (Using a library like PyPDF2)",
    "Simple Spell Checker (Using a dictionary file)",
    "Language Flashcard Application (Console or basic GUI)",
    "Text Editor (Basic GUI with Tkinter - open, save, edit text files)",
    "Automated Email Sender (Using `smtplib` to send emails)",
    "Password Strength Checker",
    "Bulk File Renamer (Based on patterns or metadata)",
    "Simple Data Visualization (e.g., plot CSV data using Matplotlib)",
    "Full-Stack Web Application (e.g., Blog with Django/Flask, Database, User Authentication)",
    "E-commerce Site Backend (Product management, orders, users, payment gateway stubs)",
    "Real-time Chat Application (Using Sockets or WebSockets with Flask/Django)",
    "Web Crawler (Using Scrapy or BeautifulSoup with advanced logic for multiple pages/sites)",
    "Data Analysis and Visualization Dashboard (Pandas, Matplotlib/Seaborn, Plotly/Dash or Flask)",
    "Machine Learning Model Deployment (e.g., Flask API for a Scikit-learn model)",
    "Sentiment Analysis Tool for Social Media (Using NLTK/spaCy and Twitter/Reddit API)",
    "Recommendation System (Content-based or basic collaborative filtering)",
    "Algorithmic Trading Bot (Simulation, basic strategies, API integration with a broker)",
    "Face Detection/Recognition Application (Using OpenCV)",
    "Optical Character Recognition (OCR) Tool (Using Tesseract via pytesseract)",
    "Network Packet Sniffer (Using Scapy)",
    "Distributed Task Queue (Implementing a simple version of Celery/RQ with Redis/RabbitMQ)",
    "Microservice Architecture (e.g., User Authentication Service, Product Service communicating via REST/gRPC)",
    "Content Aggregator (Collects data from various RSS feeds, APIs, websites and displays it)",
    "Custom ORM (Object-Relational Mapper) - simplified version",
    "Build a Simple Programming Language Interpreter or Transpiler",
    "Version Control System (Simplified Git-like functionality for local files)",
    "Search Engine for Local Files (Indexing and searching content)",
    "Automated Testing Framework (Build a small framework to run tests and report results)",
    "Personal Finance Manager with Bank API integration (e.g., using Plaid API)",
    "AI Game Player (e.g., for Chess, Go - using Minimax, Alpha-Beta Pruning, or Reinforcement Learning)",
    "Live Twitter Stream Analyzer (Track keywords, perform sentiment analysis in real-time)",
    "Secure File Transfer Protocol (SFTP) Client/Server",
    "Blockchain Implementation (Simplified version of a cryptocurrency)",
    "Vulnerability Scanner (Basic web application security scanner for common vulnerabilities like XSS, SQLi)",
    "API Gateway (A simple implementation to route requests to microservices)",
    "Log Analysis Tool (Process and visualize server logs to identify patterns or errors)",
    "Peer-to-Peer File Sharing Application",
    "Desktop Automation Tool (Using PyAutoGUI for complex GUI interaction tasks)",
]


class IdeaGnerator:  #
    def __init__(self, ideas):
        self.ideas_now = set(ideas)

    def get_idea(self):
        if not self.ideas_now:
            return None
        idea = random.choice(list(self.ideas_now))
        self.ideas_now.remove(idea)

        return idea


generator = IdeaGnerator(ideas)

while True:
    print("Do you want an idea (yes/no)")
    enter = input("yes or no:")
    if enter.lower() == 'no':
        print("Exit.")
        break

    ideas = generator.get_idea()
    if ideas is None:
        print("No more ideas 🎉")
        break
    else:
        print(f"👉 {ideas}")
