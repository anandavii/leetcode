import os

# ✅ Get the current repo folder (where script lives)
repo_path = os.path.dirname(__file__)
readme_path = os.path.join(repo_path, "README.md")

header = """# 🚀 LeetCode Java Solutions

A curated collection of my Java solutions to LeetCode problems, auto-committed and maintained with helpful metadata and a problem index.

---

## 🧠 About This Repository

This repository contains my personal solutions to algorithm and data structure problems on [LeetCode](https://leetcode.com/), written in **Java**.
Each solution is named after the problem title and includes the original LeetCode problem link as a comment at the top of the file.

The repository auto-commits any changes to `.java` files and also updates this `README.md` with a table of solved problems.

---

## 🚀 Features

- 🔄 Auto-commit and push for each solution
- 📝 Auto-generated README table with problem links
- 📄 Clean solution file organization by problem name
- 💬 Problem links included in code comments

---

## 📂 Folder Structure

_(Auto-generated file paths will be added here in future)_

---

## ✅ Solved Problems

| # | 🧠 Problem | 📄 Java File | 🔗 LeetCode |
|---|------------|--------------|-------------|
"""

rows = []
counter = 1

for root, dirs, files in os.walk(repo_path):
    for file in sorted(files):
        if file.endswith(".java"):
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, repo_path)

            with open(file_path, "r") as f:
                first_line = f.readline().strip()
                if first_line.startswith("// https://leetcode.com/problems/"):
                    link = first_line[3:].strip()
                    file_name = file.replace(".java", "")
                    problem_title = ''.join([' ' + c if c.isupper() else c for c in file_name]).strip().title()
                    row = f"| {counter} | {problem_title} | [{file}]({relative_path}) | [Link]({link}) |"
                    rows.append(row)
                    counter += 1

# Write the README
with open(readme_path, "w") as f:
    f.write(header + "\n".join(rows) + "\n")

print(f"✅ README.md updated with {counter - 1} problems.")
