# -*- coding: utf-8 -*-
__author__ = 'xinhua.sun'

from .Player import Player


class Game(object):

    def __init__(self):
        '''
        描述一局游戏的类，用于记录本局的级数、主花色等
        :return:
        '''
        pass


class WholeGame(object):

    def __init__(self):
        '''
        描述一盘游戏的类
        :return:
        '''
        self.player_list = []
        for i in range(3):
            self.player_list.append(Player())
