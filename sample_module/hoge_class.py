import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum


@dataclass
class user:
    """ユーザの管理情報

    - name (str): ユーザ名
    - id (int): 社員番号
    """
    name: str
    id: int


class HogeHogeClass:
    def __init__(self):
        """サンプルクラス
        """
        print("コンストラクタ呼ばれた！！")

    def set_user(self, name: str, id: int):
        """ユーザ情報をセットする

        Parameters
        ----------
        name : str
            ユーザ名
        id : int
            社員番号
        """
        self.user = user(name, id)

    def get_user(self) -> user:
        """ユーザ情報を取得する

        Returns
        -------
        user
            ユーザ情報
        """
        return self.user

    def add(self, s_1: int, s_2: int) -> int:
        """足し算をする

        Parameters
        ----------
        s_1 : int
            足し算をする一要素
        s_2 : int
            足し算をするもう一要素

        Returns
        -------
        int
            足し算をした結果
        """
        return s_1 + s_2

    def diff(self, s_1: int, s_2: int) -> int:
        """引き算をする

        Parameters
        ----------
        s_1 : int
            引き算をする一要素
        s_2 : int
            引き算をするもう一要素

        Returns
        -------
        int
            引き算をした結果
        """
        return s_1 - s_2
