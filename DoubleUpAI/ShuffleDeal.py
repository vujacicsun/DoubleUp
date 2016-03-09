# -*- coding: utf-8 -*-
__author__ = 'xinhua.sun'
import random
from .Utils import all_card

cards_dict = {}

def shuffle_deal():
    '''
    随机发牌程序
    :return: 四个list of tuple，表示四个玩家可以拿到的手牌
    '''

