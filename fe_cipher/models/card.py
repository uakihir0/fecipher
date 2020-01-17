# -*- coding: utf-8 -*-
from .cardinfo import CardInfo
from .player import Player


# カード
class Card:

    # 公開情報かどうか？
    is_pubic = False

    # 横になっているかどうか？
    is_tapped = False

    def __init__(self, player: Player, info: CardInfo):
        self.player = player
        self.info = info
