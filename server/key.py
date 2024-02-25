#!/usr/bin/python3
import os
import secrets

# Generate a random 32-byte hexadecimal string
secret_key = secrets.token_hex(32)

# Write the secret key to a .env file
with open('.env', 'w') as f:
    f.write(f'SECRET_KEY={secret_key}\n')
