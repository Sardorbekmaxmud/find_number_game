def random_number_game():
    import random

    print("NUMBER GAME\nXush kelibsiz!")

    rm_num = random.randint(1,101)

    guesses_soni = 0

    while True:
        guesses_soni+=1
        guess = input("son kiriting: ")
        if str(guess).isdigit() and len(guess)<4 and int(guess)>0:
            guess=int(guess)
            if guess==rm_num:
                print("🎉Tabriklaymiz, Siz Yutdingiz!🎉")
                break
            elif guess < rm_num:
                print("♻️  Siz taxmin qilgan son kichik 🔽")
                continue
            elif guess > rm_num:
                print("♻️  Siz taxmin qilgan son katta 🔼")
                continue
        else:
            print("❗Faqat 1 dan 100 gacha bo'lgan sonlar qabul qilinadi")

    print(f"{guesses_soni} ta urunishda yutdingiz")
    return "TAMOM"
