# -*- coding: utf-8 -*-
__author__ = 'xinhua.sun'

color = ['heart', 'spade', 'club', 'diamond']
card_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

all_card = []

for c in color:
    for card in card_list:
        all_card.append((c, card))

all_card.append('BigJoker')
all_card.append('SmallJoker')
