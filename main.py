"""
This program is designed to generate an unknown password and a sha3 256 hash.


# Purpose:

The goal is to minimize social media usage, by generating a random unknown password of a fixed length that the user can set as his
password for social media apps. The user will only get the corresponding sha3 256 hash.
To find out the password, the user has to "crack" the hash by using some tool like `hashcat` or a self written program.

# Reason:

The reason behind is that no matter how hard humans try to fight their social media addiction it usually does not work.
That is because most social media apps are very addicting and to fight it people often try to block the app or use some app blocker apps.

## The problem:

The main problem is that setting an app password often doesnt work, because the user knows the password or the user can disable the app blocker.
Most of the time this leads to a spiral, where you only make your access to social media a bit harder due to the extra steps of disabling the password or blocker.

## The solution:
By setting a unknown, randomized password it is impossible for the user to reset the app blockage, (exept he implements some password reset...) and because
of the sha3 256 hash, the user is able to find out his password, by "cracking" the hash. It is a basic "proof of work" concept.
The user cannot find out the password without putting in compute power and by adjusting the length of the password the user can set his "timer".
The whole process is limited by hardware and time, so there is no way for the user to "cheat" by finding out the password by using some other method.
"""

import argparse
import random
import hashlib

PASSW_FILE_NAME = "passwd.txt"
HASH_FILE_NAME = "hash.txt"
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate_passwd(length: int) -> str:
    """Generate the random password."""
    password: str = ""

    for _ in range(length):
        random_char = random.choice(CHARS)
        password += random_char

    return password


def generate_hash(passwd: str) -> str:
    """Generate the sha3 256 hash."""
    return hashlib.sha3_256(passwd.encode("utf-8")).hexdigest()


def write_to_file(inp: str, file_name: str) -> None:
    """Write the string to a file."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(inp)
    except (OSError, IOError) as err:
        print(err)


def main():
    """This is the main function. It starts the program."""

    parser = argparse.ArgumentParser(
        prog="pass_hash_generator",
    )

    parser.add_argument("length", type=int, help="lenght of the password.")

    args = parser.parse_args()

    length: int = args.length
    password: str = generate_passwd(length)

    passwd_hash = generate_hash(password)

    write_to_file(password, PASSW_FILE_NAME)
    write_to_file(passwd_hash, HASH_FILE_NAME)

    print(passwd_hash)


if __name__ == "__main__":
    main()
