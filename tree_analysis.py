#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 17:14:27 2019

@author: yaman
"""

# Binary search tree for orders and dependencies
import helpr

class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        					
    def insert(self, orders, depend = None):
        #If currently at node of the order 
        if self.value == orders:
            #Pass the dependency value to insert it in the tree
            if self.leftChild:
                self.rightChild = Node(depend)
            else:
                self.leftChild = Node(depend)
        else:	
            #This call is called more than once via the recursion, poor/inefficient, could be replaced by a vector eventually/restructure.
            found, left, right = self.find(orders) 
            if found == True:
                if self.leftChild and self.rightChild:
                    if left == True:
                        self.leftChild.insert(orders, depend)
                    elif right == True:
                        self.rightChild.insert(orders, depend)                    
                elif self.leftChild:
                    self.rightChild = Node(depend)
                else:
                    self.leftChild = Node(depend)
            else:
            #
                new_tree = Tree()
                new_tree.insert(orders,depend)                
                return new_tree
                    
    def find(self, data):
        found = None
        left = None
        right = None
        if(self.value == data):
            return True
        else:
            if self:
                if self.leftChild:
                    found = self.leftChild.find(data)
                    if found == True:
                        left = True
                if found is not True:
                    if self.rightChild:
                        found = self.rightChild.find(data)
                        if found == True:
                            right = True
                if found is not True:
                    found = False
        return found, left, right                                

    def depth_tree_order(self, tab = ""):
        if self: 
            #Probably could use order.text instead of retyping
            line =tab+ "Id:"+ str(self.value)+","+ " Order Name: "+str(self.value)+"\n"
            helpr.write_end_file("output.txt",line) 
            if self.leftChild:
                line = tab+"Dependencies"+"\n"
                helpr.write_end_file("output.txt",line) 
                tab += "\t"
                self.leftChild.depth_tree_order(tab)
            if self.rightChild:
                self.rightChild.depth_tree_order(tab)

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data, depend):
		if self.root:
			return self.root.insert(data, depend)
		else:
			self.root = Node(data)
			return self.root.insert(data, depend)

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False
				
	def depth_tree_order(self):
		if self.root is not None:
			self.root.depth_tree_order()
		

