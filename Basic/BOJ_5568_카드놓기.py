from itertools import permutations

n = int(input())
k = int(input())
cards = []

for _ in range(n):
    card = input()
    cards.append(card)

result = set()

for i in permutations(cards, k):
    result.add(''.join(i))

print(len(result))

# # 총 카드 숫자
# totalCardsNum = int(input())
# # 선택할 카드 숫자
# 선택해야하는카드수 = int(input())
# # 카드들 모음
# cards = []
# # 완성된 숫자모음(set으로 중복제거)
# resultNumbers = set()
# # 중복제외용

# def makeNumber(cards, 만들어진조합, 선택카드인덱스, 선택해야하는카드수):
#   # 만약 선택 안해도 되면
#   if(선택해야하는카드수 == 0):
#       resultNumbers.add(만들어진조합)
#       return
#   for i, card in enumerate(cards):
#     if i not in 선택카드인덱스 :
#       makeNumber(cards, 만들어진조합+card, 선택카드인덱스 + [i], 선택해야하는카드수 -1)
# # 데이터 받기
# for _ in range(totalCardsNum) :
#     cards.append(input())
# makeNumber(cards, "", [], 선택해야하는카드수)
# print(len(resultNumbers))