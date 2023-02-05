# import requests
# import random



#WORD_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"


# def generate_random_wordbank():
#     response = requests.get(WORD_SITE)
#     WORDS = response.content.splitlines()
#     # print(type(WORDS))
#     write_bank_to_file(WORDS)



# def write_bank_to_file(lines):
#     with open('your_file.txt', 'w') as f:
#         for line in lines:
#             f.write(f"{line}\n")


# def get_word():
#     return random.choice(open("your_file.txt").readline().split())



# def main():
    # generate_random_wordbank()
    # random_word = get_word()


# if __name__ == '__main__':
#     main()