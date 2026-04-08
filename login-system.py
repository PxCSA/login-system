#!/usr/bin/env python3
# =======================================
# Secure Login System by SHIVAMxCSA
# For educational purposes only
# =======================================

import hashlib
import json
import os

DB_FILE = "users.json"

def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(users):
    print("\n==================================================")
    print("                  REGISTER")
    print("==================================================")
    username = input("  Enter username: ")
    if username in users:
        print("  [!] Username already exists!")
        return
    password = input("  Enter password: ")
    if len(password) < 6:
        print("  [!] Password must be at least 6 characters!")
        return
    users[username] = hash_password(password)
    save_users(users)
    print(f"  [+] User '{username}' registered successfully!")

def login(users):
    print("\n==================================================")
    print("                   LOGIN")
    print("==================================================")
    username = input("  Enter username: ")
    if username not in users:
        print("  [!] Username not found!")
        return
    password = input("  Enter password: ")
    if users[username] == hash_password(password):
        print(f"  [+] Welcome back, {username}! Login successful! ✅")
    else:
        print("  [!] Incorrect password! Access denied! ❌")

def main():
    users = load_users()
    print("==================================================")
    print("       Secure Login System by SHIVAMxCSA")
    print("==================================================")

    while True:
        print("\nWhat do you want to do?")
        print("  1. Register")
        print("  2. Login")
        print("  3. Quit")

        choice = input("\n  Enter choice (1/2/3): ")

        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            print("\n  Goodbye! Stay secure! 🔐")
            break
        else:
            print("\n  [!] Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()