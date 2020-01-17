# -*- coding: utf-8 -*-
from fe_cipher.models.areas.deck import Deck
from fe_cipher.models.areas.hand import Hand
from fe_cipher.models.areas.line import Line


# フィールド (プレイヤー分)
class Field:

    deck: Deck = Deck()  # デッキ
    hand: Hand = Hand()  # 手札

    front_line: Line = Line(is_front=True)  # 前衛
    back_line: Line = Line(is_front=False)  # 後衛


    def __init__(self):
        pass

