# Secure Login System 🔑

A secure login system with SHA-256 password hashing built in Python.

## Features
- User registration with hashed passwords
- Secure login with password verification
- Passwords stored as SHA-256 hashes — never in plain text
- Simple menu driven interface

## Usage
```bash
python login_system.py
```

## Example
[+] User 'shivam' registered successfully!
[+] Welcome back, shivam! Login successful! ✅
[!] Incorrect password! Access denied! ❌

## What is SHA-256?
SHA-256 is a cryptographic hash function used by real websites
and applications to store passwords securely. Even if the
database is leaked, passwords cannot be reversed.

## Tech
- Python 3
- Hashlib module
- JSON for storage

## Disclaimer
This tool is for educational purposes only.
