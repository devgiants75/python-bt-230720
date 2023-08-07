### 클래스 생성, 생성자, 소멸자 예제 ###

class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strenght = strength
        print(f'캐릭터 {self.name}이(가) 생성되었습니다. 체력은 {self.hp}, 힘은 {self.strenght} 입니다.')

    def attack(self, other_character):
        print(f'{self.name}이(가) {other_character.name}을(를) 공격합니다!')
        other_character.hp -= self.strenght

    # def __del__(self):
    #     print(f'{self.name}이(가) 게임에서 사라졌습니다.')

    def remove_from_game(self):
        print(f'{self.name}이(가) 게임에서 사라졌습니다.')

Naymar = Character('Naymar', 300, 50)
Son = Character('Son', 400, 150)

Son.attack(Naymar)
print(f'네이마르의 남은 체력은 {Naymar.hp}입니다.')

Naymar.attack(Son)
print(f'손흥민의 남은 체력은 {Son.hp}입니다.')

Son.attack(Naymar)
print(f'네이마르의 남은 체력은 {Naymar.hp}입니다.')

# 네이마르 캐릭터의 체력이 0이 되면 제거
if Naymar.hp <= 0:
    Naymar.remove_from_game()
    del Naymar

#? 파이썬 소멸자 사용 시 주의사항
# : 소멸자(__del__메서드)는 객체가 메모리에서 제거될 때 호출
# : 소멸자의 삭제 시점을 프로그래머가 명확하게 지정할 수 없음.
# : 파이썬의 가비지 컬렉션이 언제 동작할지 불분명.