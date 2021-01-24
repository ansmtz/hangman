import random
import art
import words
words.parse_words()
word_list = words.get_words()

random_choice = random.choice(word_list)

# тест
# print(random_choice)

blanks = []
for blank in range(len(random_choice)):
    blanks.append("_")

print(''.join(blanks))
print('Привет. Я загадал для тебя слово. Попробуй отгадать')
used_letters = []
lives = 6
while "_" in blanks:
    user_choice = input('Буква: ').lower()
    if user_choice in used_letters:
        print("Ты уже загадывал эту букву")
    elif user_choice not in random_choice:
        used_letters.append(user_choice)
        print(f"Использованные буквы: {', '.join(used_letters)}")
        lives -= 1
        print("Нет такой буквы")
    else:
        used_letters.append(user_choice)
        print(f"Использованные буквы: {', '.join(used_letters)}")
        for position in range(len(random_choice)):
            if user_choice == random_choice[position]:
                blanks[position] = user_choice
    print("".join(blanks))
    print(art.stages[lives])
    if "_" not in blanks:
        print("Ура! Ты победил!")
        break
    if lives == 0:
        print('Ты проиграл :(')
        print(f"Я загадал слово {random_choice}")
        break





