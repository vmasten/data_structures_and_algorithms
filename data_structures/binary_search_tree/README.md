# Binary Search Tree

A basic implementation of a binary search tree data structure. It currently allows for instantiation, insertion, and pre-, in-, and post-order depth-first traversals, as well as a breadth-first traversal.

# Breadth-first
Write a breadth-first traversal method which takes a Binary Tree as its unique input.

## Challenge
Do not use any of the built-in methods available to your language.

## Approach & Efficiency
Toby and I basically followed the CF example implementation, using the Queue class we already built to enqueue and dequeue the nodes to enforce the breadth-first order.

The time complexity is O(N), since every node in the tree will be visited. The space complexity is O(log N) since a very full tree will require a lot of space at the bottom level, but progressively less space leading up to that bottom layer.

## Solution
![](../../assets/breadth-first-traversal.jpg)
