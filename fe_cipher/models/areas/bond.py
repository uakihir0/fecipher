# -*- coding: utf-8 -*-
from typing import Set
from fe_cipher.models.card import Card
from fe_cipher.constants.symbols import Symbols


# 絆
class Bond:
    cards: [Card] = []

    def __init__(self):
        pass

    # カードを追加
    def add_card(self, card: Card):
        self.cards.append(card)

    # カードを取得
    def remove_card(self, card: Card) -> Card:
        self.cards.remove(card)
        return card

    # 出撃可能かどうか？
    def can_deploy_card(self, card: Card) -> bool:

        # シンボルが存在しない場合は出撃可能
        if len(card.info.symbol()) == 0:
            return True

        # 許容されるシンボルのリストを生成
        allowed_symbols: Set[Symbols] = set([])
        for bond_card in self.cards:
            for symbol in bond_card.info.symbol():
                allowed_symbols.add(symbol)

        # そのカードの全てのシンボルが絆に存在するか？
        for symbol in card.info.symbol():
            if symbol not in allowed_symbols:
                return False
        return True




