# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from .match import Match
from .effect.trigger_effect import TriggerEffect
from .effect.ignition_effect import IgnitionEffect
from .effect.support_effect import SupportEffect
from ..constants.affinities import Affinities
from ..constants.symbols import Symbols


# カード情報
class CardInfo(ABCMeta):

    # カード番号
    @abstractmethod
    def code(self) -> str:
        pass

    # ユニットの役職
    @abstractmethod
    def units_title(self) -> str:
        pass

    # キャラクター名
    @abstractmethod
    def units_name(self) -> str:
        pass

    # 出撃コスト
    @abstractmethod
    def deployment_cost(self) -> int:
        pass

    # クラスチェンジコスト
    @abstractmethod
    def class_change_cost(self) -> int:
        pass

    # 射程
    @abstractmethod
    def range(self) -> [int]:
        pass

    # シンボル
    @abstractmethod
    def symbol(self) -> [Symbols]:
        pass

    # アイコン
    @abstractmethod
    def affinities(self) -> [Affinities]:
        pass

    # 攻撃力
    @abstractmethod
    def attack(self, match: Match) -> int:
        pass

    # 防御力
    @abstractmethod
    def defence(self, match: Match) -> int:
        pass

    # サポート
    @abstractmethod
    def support(self, match: Match) -> int:
        pass

    # 起動効果一覧
    def ignition_effects(self) -> [IgnitionEffect]:
        return []

    # 誘発効果一覧
    def trigger_effects(self) -> [TriggerEffect]:
        return []

    # 支援効果一覧
    def support_effects(self) -> [SupportEffect]:
        return []
