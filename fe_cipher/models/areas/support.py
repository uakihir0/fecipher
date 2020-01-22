# -*- coding: utf-8 -*-
from typing import Union
from fe_cipher.models.card import Card


# 支援
class Support:
    card: Union[Card, None] = None

    def __init__(self):
        pass

    # カードをセット
    def set_card(self, card: Card):
        self.card = card

    # カードを取る
    def take_card(self) -> Card:
        if self.card is not None:
            card = self.card
            self.card = None
            return card
        raise Exception
