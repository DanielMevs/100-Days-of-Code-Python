import requests


def generate_random_wordbank():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    # print(type(WORDS))

    write_bank_to_file(WORDS)

def write_bank_to_file(lines):
    with open('your_file.txt', 'w') as f:
        for line in lines:
            f.write(f"{line}\n")