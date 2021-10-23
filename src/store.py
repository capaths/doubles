import os
import glob
import argparse
from string import ascii_uppercase, digits
import secrets
from storage import Storage

from typing import Dict


def compile():
    codes: Dict[str, ] = {}
    for filepath in glob.glob('./codes/*.txt'):
        filename, _ = os.path.splitext(os.path.basename(filepath))
        with open(filepath, 'r') as f:
            codes[filename] = [l.strip() for l in f.readlines()]
    print(f"Found services: {', '.join(list(codes.keys()))}")
    return Storage(codes)

def generate_random_string(length: int = 8) -> str:
    return ''.join(secrets.choice(ascii_uppercase + digits) for _ in range(length))

def generate_random_code() -> str:
    return generate_random_string(length=3) + '-' + generate_random_string(length=3)

def main(n_passwords: int):
    compiled = compile()

    passwords = [generate_random_code() for _ in range(n_passwords)]
    print("While your codes are being encrypted. Store your master passwords:\n")
    print('\n'.join(passwords))
    print("\nStore them safely. Maybe each one in different places.")
    print("And remember, the order is important")

    filename = './2fa-rc2s.store'
    with open(filename, 'wb') as f:
        f.write(compiled.encrypt(passwords))
    print(f"The store can be found at {filename}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encode 2FA codes')
    parser.add_argument('-n', '--n-passwords', help='How many passwords to generate', default=6, type=int)
    args = parser.parse_args()
    n_passwords: int = args.n_passwords

    main(n_passwords)
