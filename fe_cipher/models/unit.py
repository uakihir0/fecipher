# -*- coding: utf-8 -*-
from .card import Card


# ユニット情報
class Unit:
    cards: [Card] = []

    # 主人公かどうか？
    is_hero = False

    def __init__(self, card: Card):
        self.cards.append(card)

    # タップ
    def set_tapped(self, is_tapped: bool):
        for card in self.cards:
            card.is_tapped = is_tapped
