# 📱 Social Media Profile Analyzer

A Python-based data parsing project that converts unstructured social media profile information into structured Python dictionaries and JSON format.

This project demonstrates text parsing, data cleaning, exception handling, and basic data preprocessing techniques.

---

## 🚀 Features

- Parse raw social media profile data from a text file.
- Extract key profile information:
  - Username
  - Number of posts
  - Number of followers
  - Number of following
  - Display name
  - Page type
  - Bio
- Handle profiles with missing page types.
- Skip empty profile blocks to avoid parsing errors.
- Generate clean, structured data for further analysis

---

## ⚙️ How It Works

1. Reads raw profile data from `initialdata.txt`.
2. Splits the data into individual profile blocks.
3. Parses each profile into a Python dictionary.
4. Handles missing fields and empty records gracefully.
5. Stores the cleaned data for further analysis.

---
## 📄 Sample Output

```python
{
    "username": "pointaglobal",
    "no_of_posts": "1,946 posts",
    "no_of_followers": "6,851 followers",
    "no_of_following": "262 following",
    "name": "INTA",
    "type_of_page": "Nonprofit organization",
    "bio": "The association of ™ professionals.\ninta.campsite.bio"
}
```

---

## 🛠️ Technologies Used

- Python 3
- JSON
- File Handling
- Exception Handling

---

## 💡 Skills Demonstrated

- Python Programming
- String Manipulation
- Text Parsing
- Data Cleaning
- File Handling
- Exception Handling
- Working with Lists and Dictionaries
- JSON Processing

---

## 👩‍💻 Author

Developed as a Python practice project to strengthen skills in data parsing, preprocessing, and structured data handling.
