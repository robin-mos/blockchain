#!/usr/bin/env python

# encoding: utf-8

'''
@license:  LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: BlockFactory.py
@time: 2018/3/6 0006 下午 4:46
@description: 区块创建
'''

import datetime as date
from Block import Block


def createGenesisBlock():
    return Block(0, date.datetime.now(), 'Genesis Block', '0')


# 创建下一个
def nextBlock(lastBlock = Block):
    index = lastBlock.index + 1
    timestamp = date.datetime.now()
    data = 'block data ' + str(index)
    hash = lastBlock.hash
    return Block(index, timestamp, data, hash)
