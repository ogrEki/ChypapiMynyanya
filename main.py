import random
import time
code_list = ["Free_coins", "coins2024", "terraria", "1", "qwertyuiopasdfghjklzxcvbnm", "Velikiy Ilia Cergiovic"]
def generate_priclad():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        c_answer = num1 + num2
    elif operation == '-':
        c_answer = num1 - num2
    elif operation == '*':
        c_answer = num1 * num2
    question = f"{num1} {operation} {num2} = ?"
    return question, c_answer
def play_game(coins, time_limit):
    print("Вітаємо у грі! Відповідайте на математичні питання за обмежений час, щоб заробити монети.")
    print(f"У вас є {time_limit} секунд на кожне питання!")
    while True:
        question, correct_answer = generate_priclad()
        print("\nЗадача:", question)
        start_time = time.time()
        try:
            user_answer = float(input("Ваша відповідь: "))
        except ValueError:
            print("Будь ласка, введіть число!")
            continue
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time > time_limit:
            print(f"Час вичерпано! Ви не встигли відповісти за {time_limit} секунд.")
            print(f"Ви заробили {coins} монет. Гра завершена.")
            break
        if abs(user_answer - correct_answer) < 0.01:
            coins += 1
            print(f"Правильно! Ви заробили 1 монету. У вас тепер {coins} монет.")
            # Увеличиваем время на ответ за каждые 5 монет
            if coins % 5 == 0:
                time_limit += 1
                print(f"Вітаємо! Час на питання збільшено. Тепер у вас {time_limit} секунд.")
        else:
            print(f"Неправильно. Правильна відповідь: {correct_answer}.")
        continue_game = input("Хочете продовжити? (так/ні): ").strip().lower()
        if continue_game != "так":
            print(f"Гра завершена. Ви заробили {coins} монет.")
            break
    return coins, time_limit
def redeem_code(coins, time_limit):
    code_inp = input("Введіть код: ").strip()
    if code_inp in code_list:
        coins += 1000
        print(f"Код активовано! Ви отримали 1000 монет. У вас тепер {coins} монет.")
        # Увеличиваем время на ответ за каждые 5 монет
        additional_time = (coins // 5) - (time_limit - 5)
        if additional_time > 0:
            time_limit += additional_time
            print(f"Час на питання збільшено на {additional_time} секунд. Тепер у вас {time_limit} секунд.")
    else:
        print("Невірний код. Спробуйте ще раз.")
    return coins, time_limit
def main():
    coins = 0
    time_limit = 5
    print("Вітаємо у грі!")
    while True:
        start_game = input("Бажаєте почати гру чи активувати код? (гра/код/вихід): ").strip().lower()
        if start_game == "гра":
            coins, time_limit = play_game(coins, time_limit)
        elif start_game == "код":
            coins, time_limit = redeem_code(coins, time_limit)
        elif start_game == "вихід":
            print("Дякуємо за гру! До зустрічі.")
            break
        else:
            print("Невірна команда. Спробуйте ще раз.")
if __name__ == "__main__":
    main()

