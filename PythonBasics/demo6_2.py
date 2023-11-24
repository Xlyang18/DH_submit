import random

# 创建一副扑克牌
suits = ['♠', '♥', '♣', '♦']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# 计算牌面点数
def calculate_points(hand):
    total = 0
    for card in hand:
        rank = card['rank']
        if rank.isdigit():
            total += int(rank)
        elif rank in ['J', 'Q', 'K']:
            total += 10
        else:
            total += 1  # 将A算作1点
    return total

# 发牌
def deal(deck, num_cards=2):
    hand = []
    for _ in range(num_cards):
        card = deck.pop(random.randint(0, len(deck) - 1))
        hand.append(card)
    return hand

# 展示手牌
def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        print("暗牌: 🎴", end=' ')
        for card in hand[1:]:
            print(f"{card['rank']}{card['suit']}", end=' ')
    else:
        for card in hand:
            print(f"{card['rank']}{card['suit']}", end=' ')
    print()

# 游戏逻辑
def blackjack_game():
    player_hand = deal(deck)
    dealer_hand = deal(deck)

    # 显示玩家一张明牌和一张暗牌
    print("玩家手牌:")
    display_hand(player_hand, hide_first_card=True)

    # 显示庄家一张明牌和一张暗牌
    print("庄家手牌:")
    display_hand(dealer_hand, hide_first_card=True)

    # 玩家回合
    while True:
        choice = input("要牌？(y/n): ").lower()
        if choice == 'y':
            player_hand.extend(deal(deck, num_cards=1))
            print("玩家手牌:")
            display_hand(player_hand, hide_first_card=True)
            if calculate_points(player_hand) > 21:
                print("玩家爆牌！")
                return False
        else:
            break

    # 庄家回合
    while calculate_points(dealer_hand) < 18:
        dealer_hand.extend(deal(deck, num_cards=1))

    print("庄家手牌:")
    display_hand(dealer_hand)

    player_points = calculate_points(player_hand)
    dealer_points = calculate_points(dealer_hand)

    print(f"玩家点数: {player_points}")
    print(f"庄家点数: {dealer_points}")

    if player_points > 21:
        return False
    elif dealer_points > 21:
        return True
    else:
        return player_points > dealer_points

# 开始游戏
result = blackjack_game()
if result:
    print("玩家胜利！")
else:
    print("庄家胜利！")
