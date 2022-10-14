import random
from xml.etree.ElementTree import TreeBuilder

random_number = random.randint(1,100)

#print(random_number)

game_count = 1

while True:
    
    my_number = int(input("1-100사이의 숫자를 입력하세요: "))
    
    if my_number > random_number:
        print("Down!!")

    elif my_number < random_number:
        print("Up!!")
    
    elif my_number == random_number:
        print(f"Correct! {game_count}번만에 맞추셨습니다")
        break
    game_count += 1