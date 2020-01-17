# -*- coding: utf-8 -*-
from enum import Enum


# 類似属性
class Affinities(Enum):

    # --- 性別 ---
    Male = 1001  # 男
    Female = 1002  # 女

    # --- 武器 ---
    Sword = 2001  # 剣
    Lance = 2002  # 槍
    Axe = 2003  # 斧
    Bow = 2004  # 弓
    Tome = 2005  # 本
    Staff = 2006  # 杖
    Brawl = 2007  # 拳
    Dragonstone = 2008  # 竜石
    Knife = 2009  # 暗器
    Fang = 2010  # 牙

    # --- ユニットタイプ ---
    Armored = 3001  # アーマー
    Flier = 3002  # 飛行
    Beast = 3003  # 馬
    Dragon = 3004  # ドラゴン
    Mirage = 3005  # ミラージュ
    Monster = 3006  # モンスター
