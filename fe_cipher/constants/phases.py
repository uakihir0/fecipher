# -*- coding: utf-8 -*-
from enum import Enum


# フェーズ定義
class Phases(Enum):
    # 開始フェーズ
    Beginning = 1
    # 絆フェーズ
    Bond = 2
    # 出撃フェーズ
    Deployment = 3
    # 行動フェーズ
    Action = 4
