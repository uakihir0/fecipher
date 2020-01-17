# -*- coding: utf-8 -*-
from fe_cipher.models.card import Card


# 手札
class Hand:

    # 0 は一番左のカード
    cards: [Card] = []

    def __init__(self):
        pass

    # カードを手札に追加
    def add_card(self, card: Card):
        self.cards.append(card)
