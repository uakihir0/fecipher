# -*- coding: utf-8 -*-
from fe_cipher.models.unit import Unit


# 戦線
class Line:
    is_front = False  # 前
    is_back = False  # 後

    # ユニット (0 が一番左)
    units: [Unit] = []

    def __init__(self, is_front: bool):
        self.is_front = is_front
        self.is_back = not is_front

    # ユニットを追加
    def add_unit(self, unit: Unit):
        self.units.append(unit)

    # ユニットを除外
    def remove_unit(self, unit: Unit) -> Unit:
        if unit in self.units:
            self.units.remove(unit)
            return unit
        raise Exception
