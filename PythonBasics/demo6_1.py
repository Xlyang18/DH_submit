import random


def generate_deck():

    suits = ['红桃', '黑桃', '梅花', '方块']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    jokers = ['大王', '小王']

    deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]
    deck += [{'joker': joker} for joker in jokers]

    return deck


def shuffle_deck(deck):
    """
    洗牌
    """
    random.shuffle(deck)


def deal_cards(deck, players=4, cards_per_player=13):
    """
    发牌
    """
    hands = [[] for _ in range(players)]

    for _ in range(cards_per_player):
        for player in range(players):
            card = deck.pop(0)
            hands[player].append(card)

    return hands


def print_hands(hands):
    """
    打印玩家手中的牌
    """
    for i, hand in enumerate(hands, start=1):
        print(f"Player {i}'s hand:")
        for card in hand:
            if 'joker' in card:
                print(f"   {card['joker']}",end="")
            else:
                print(f"   {card['suit']} {card['rank']} ",end="")
        print()


if __name__ == "__main__":
    # 生成一副扑克牌
    deck = generate_deck()

    # 洗牌
    shuffle_deck(deck)

    # 发牌给4个玩家，每人13张牌
    hands = deal_cards(deck, players=4, cards_per_player=13)

    # 打印每个玩家手中的牌
    print_hands(hands)
