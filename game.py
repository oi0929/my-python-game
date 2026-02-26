import random

def guess_number():
    print("🎮 歡迎來到「猜數字」小遊戲！")
    print("系統已經準備好了一個 1 到 100 之間的數字，看看你幾次能猜中！")
    
    answer = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("👉 請輸入你的猜測："))
            attempts += 1
            
            if guess < answer:
                print("太小囉！再往上猜一點。\n")
            elif guess > answer:
                print("太大囉！往下猜一點。\n")
            else:
                print(f"🎉 恭喜答對！答案就是 {answer}。")
                print(f"你總共猜了 {attempts} 次，太厲害了！")
                break
        except ValueError:
            print("⚠️ 格式錯誤：請輸入有效的整數喔！\n")

if __name__ == "__main__":
    guess_number()