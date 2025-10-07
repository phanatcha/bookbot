# 📚 BookBot

Welcome to **BookBot** — your first full Python project (and maybe your first Boot.dev adventure)! 🎉
This program analyzes text from classic novels and prints a report showing word and character statistics.
It’s a fun way to start thinking like a real software developer — not just running snippets, but building a full working project.

---

## 🧠 Learning Goals

By completing BookBot, you’ll:

* 🛠️ Set up a **professional Python environment** on your local machine
* 🧩 Build a **complete project from scratch**
* 🐙 **Push and manage your project on GitHub**
* 💻 Get comfortable with **VS Code** and professional development workflows

---

## 🚀 How It Works

BookBot reads `.txt` files, analyzes their contents, and prints a report with insights such as:

* Total number of words in the book
* Frequency of each character
* Sorted statistics for easy reading

Example output:

```
============ BOOKBOT ============
Analyzing book found at ./books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1

```

---

## 🧩 Project Structure

```
bookbot/
│
├── __pycache__/               
│   └── stats.cpython-313.pyc
│
├── books/                   
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
│
├── .gitignore                 
├── main.py                   
├── stats.py                   
└── README.md                 
```

---

## ⚙️ How to Run

Make sure you have **Python 3** installed on your system.
Then, in your terminal:

```bash
python3 main.py <path_to_book>
```

You’ll see a report printed in your terminal for the selected book.

---

## 🧠 How It’s Organized

* `main.py` — the main driver that runs your program
* `stats.py` — contains helper functions for counting and sorting text data
* `books/` — folder where your `.txt` books live 

---
