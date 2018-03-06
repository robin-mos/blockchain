#!/usr/bin/env python

# encoding: utf-8

'''
@license:  LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: Block.py
@time: 2018/3/6 0006 下午 4:37
@description: 区块信息
'''


import hashlib as hasher


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashBlock()

    # 生成hash值
    def hashBlock(self):
        sha = hasher.sha256()
        sha.update(str(str(self.index)+
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf8'))
        return sha.hexdigest()

    # 生成md5值
    def md5Block(self):
        m = hasher.md5()
        m.update(str(str(self.index)+
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash)).encode('utf8'))
        return m.hexdigest()
