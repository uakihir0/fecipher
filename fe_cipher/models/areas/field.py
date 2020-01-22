# -*- coding: utf-8 -*-
# フィールド (プレイヤー分)
from fe_cipher.models.areas.bond import Bond
from fe_cipher.models.areas.deck import Deck
from fe_cipher.models.areas.hand import Hand
from fe_cipher.models.areas.line import Line
from fe_cipher.models.areas.mugen import Mugen
from fe_cipher.models.areas.orb import Orb
from fe_cipher.models.areas.retreat import Retreat
from fe_cipher.models.areas.support import Support


class Field:

    deck: Deck = Deck()  # デッキ
    hand: Hand = Hand()  # 手札
    bond: Bond = Bond()  # 絆

    front_line: Line = Line(is_front=True)  # 前衛
    back_line: Line = Line(is_front=False)  # 後衛

    orb: Orb = Orb()  # オーブ
    support: Support = Support()  # 支援
    retreat: Retreat = Retreat()  # 退避
    mugen: Mugen = Mugen()  # 無限

    def __init__(self):
        pass

    def draw(self, count: int = 1):
        for i in range(count):
            card = self.deck.pop_top_card()
            self.hand.add_card(card)
