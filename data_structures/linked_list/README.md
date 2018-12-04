# kth from the end of a Linked List
An exercise to extend the existing linked list module that allows for finding the element at the kth node from the end of the list.

## Challenge
This task must be accomplished by extending the predefined linked list and node classes, and may not use the __len__ function.

## Approach & Efficiency
Joyce came up with the idea of using a lookahead variable to create an offset between the head of the list and the number of elements from the end we're looking for. Matt and I interrogated and refined the method to deal with edge cases and coalesce the concept into working code.

As usual, the runtime will be O(N), because even though the lookahead is found before the result is calculated, the lookahead variable will only ever do as many traversals as the size of the list because of how it's set in place.

## Solution
![]()../../assets/ll_kth_from_end.jpg
