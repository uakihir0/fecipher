# -*- coding: utf-8 -*-
from fe_cipher.models.card import Card


# 退避
class Retreat:
    cards: [Card] = []

    def __init__(self):
        pass

    # カードを退避に追加
    def add_card(self, card: Card):
        self.cards.append(card)

    # カードを退避から除外
    def remove_card(self, card: Card) -> Card:
        self.cards.remove(card)
        return card
