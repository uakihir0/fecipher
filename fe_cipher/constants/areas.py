# -*- coding: utf-8 -*-
from enum import Enum


# エリア定義
class Areas(Enum):
    # デッキ
    Deck = 1
    # 手札
    Hand = 2
    # 絆
    Bond = 3
    # 前衛
    FrontLine = 4
    # 後衛
    BackLine = 5
    # 退避
    Retreat = 6
    # 支援
    Support = 7
    # オーブ
    Orb = 8
    # 無限
    Mugen = 9
