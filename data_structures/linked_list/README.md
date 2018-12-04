# Linked List Insertions
An expansion of a simple linked list module that allows for appending to the end of the list along with inserting before or after a desired node value.

## Challenge
This task must be accomplished by extending the predefined linked list and node classes, which include only limited node traversal and insertion.

## Approach & Efficiency
I thought I had a good handle on how to accomplish these tasks, but when I went to write insert_before, it turned out I wrote insert_after, and I ended up with an infinite loop when I tried to (re)write insert_before. It took a while to figure out what was going wrong, and if I'm being honest, I'm still not sure why the loop requires a return once the node is in place, but I plan to ask about it tomorrow. The return in insert_after was added after the fact for symmetry.

As with other linked list traversals, the append and insertions run in O(N) time, as traversal depends on the size of the list and will, at worst, will have to traverse the entire list before insertion.

## Solution
![]()../../assets/ll_insertions_1.jpeg
![]()../../assets/ll_insertions_2.jpeg

