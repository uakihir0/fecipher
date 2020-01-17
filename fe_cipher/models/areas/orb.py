# -*- coding: utf-8 -*-
from fe_cipher.models.card import Card


# オーブ
class Orb:
    cards: [Card] = []

    def __init__(self):
        pass

    # カードをオーブに追加
    def add_card(self, card: Card):
        self.cards.append(card)

    # カードをオーブから除外
    def remove_card(self, card: Card) -> Card:
        self.cards.remove(card)
        return card
