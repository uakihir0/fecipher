# -*- coding: utf-8 -*-
import random
from fe_cipher.models.card import Card


class Deck:

    # 0 が一番下のカードと扱う
    cards: [Card] = []

    def __init__(self):
        pass

    # 一番上にカードを追加
    def add_card_to_top(self, card: Card):
        self.cards.append(card)

    # 一番下にカードを追加
    def add_card_to_bottom(self, card: Card):
        self.cards.insert(0, card)

    # デッキシャッフル
    def shuffle(self):
        random.shuffle(self.cards)

    # デッキの先頭のカードを取得
    def pop_top_card(self) -> Card:
        if len(self.cards) > 0:
            card = self.cards[-1]
            self.cards.remove(card)
            return card
        raise Exception
