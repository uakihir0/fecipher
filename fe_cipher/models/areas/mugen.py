# -*- coding: utf-8 -*-
from fe_cipher.models.card import Card


# 無限エリア
class Mugen:
    cards: [Card] = []

    def __init__(self):
        pass

    # カードを無限エリアに追加
    def add_card(self, card: Card):
        self.cards.append(card)

    # カードを無限エリアから除外
    def remove_card(self, card: Card) -> Card:
        if card in self.cards:
            self.cards.remove(card)
            return card
        raise Exception
