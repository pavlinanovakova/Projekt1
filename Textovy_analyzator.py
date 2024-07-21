"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavlína Nováková
email: spiki15@seznam.cz
discord: Pavlína Nováková (pavlinanovakova)
"""

# text
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
reegistrovaní uživatelépresent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


# Registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

oddelovac = "+------+-------------+"



# tabulka uživatelů
for index, data in enumerate(users.items()):
    if index == 0:
        print(oddelovac, "| user |  password   |", oddelovac, sep="\n")
    print(f"| {data[0]: ^4} | {data[1]: ^11} |", sep= "\n")
print(oddelovac)



# ověření uživatele
user = input("username: ")
password = input("password: ")
print("----------------------------------------")

if (user, password) in users.items():
    print(f"Welcome to the app, {user}")
    print(f"We have 3 texts to be analyzed.")
    print("----------------------------------------")

else:
    print("Unregistered user, terminating the program..")
    exit()




# výběr textu
text_number = input(f"Enter a number btw. 1 and 3 to select:")

if int(text_number) not in range(1,(len(TEXTS) + 1)):
        print("Wrong input, terminating the program.. ")
        exit()
else:
    text = TEXTS[int(text_number) - 1]



# práce s textem
preselect_text = [word.strip(".,?!-%+/*()§\"") for word in text.split()]

sum_words = len(preselect_text)
titlecase = []
uppercase = []
lowercase = []

numbers = [int(word) for word in text.split() if word.isnumeric()]
number_count = len(numbers)
number_sum = sum(numbers)


for word in preselect_text:
    if word[0].istitle():
        titlecase.append(word)
    if word.isupper() and word.isalpha():
        uppercase.append(word)
    if word.islower() and word.isalpha():
        lowercase.append(word)


sum_titlecase = len(titlecase)
sum_uppercase = len(uppercase)
sum_lowercase = len(lowercase)
num_words = len(numbers)
number_sum = sum(numbers)


print("----------------------------------------")
print(f"There are {sum_words} words in the selected text.")
print(f"There are {sum_titlecase} titlecase words.")
print(f"There are {sum_uppercase} uppercase words.")
print(f"There are {sum_lowercase} lowercase words.")
print(f"There are {num_words} numeric strings.")
print(f"The sum of all the numbers {number_sum}")
print("----------------------------------------")



# graf 
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

lenghts_word = [len(word) for word in preselect_text]
longest_word = max(lenghts_word)
len_counts = {length: lenghts_word.count(length) for length in range(1, longest_word + 1)}


for length in range(1, longest_word+ 1):
    print(f"{length:>3}|{'*' * len_counts.get(length, 0):<14}|{len_counts.get(length, 0)}")