# Merge two Linked Lists
Write a function called merge_lists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Challenge
Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.


## Approach & Efficiency
I initially thought that this would be best accomlished by a while loop, as seen in the whiteboarding with Joyce and Toby, but when it came time to implement it, for loops worked better, because I was working with already-made lists with a size, which made a good range for a loop. I used a series of if statements to test whether one or the other list is empty, and to compensate for one list being larger than the other.

I don't think my additions run in O(1) time, because the length of the loop (and therefore runtime) is determined by the size of the larger list being passed in. I'm not sure how I could've refactored to be more efficient.

## Solution
![](../../ll_merge.jpeg)
