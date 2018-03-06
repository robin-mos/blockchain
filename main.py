#!/usr/bin/env python

# encoding: utf-8

'''
@license:  LiXiangping
@version:
@release:
@author: LiXiangping
@email: 752070569@qq.com
@file: main.py
@time: 2018/3/6 0006 下午 5:07
@description:区块链管理
'''
import BlockFactory


class BlockChain:

    def __init__(self):
        self.blockChain = [BlockFactory.createGenesisBlock()]
        self.previousBlock = self.blockChain[0]

    def addBlocks(self, count):
        for i in range(0, count):
            blockNew = BlockFactory.nextBlock(self.previousBlock)
            self.blockChain.append(blockNew)
            self.previousBlock = blockNew

    def showBlocks(self):
        for block in self.blockChain:
            print(block.index)
            print(block.timestamp)
            print(block.data)
            print(block.hash)


if __name__ == '__main__':
    blockChain = BlockChain()
    blockChain.addBlocks(10)
    blockChain.showBlocks()
