# python1
Binary Seach:
Given a list L of n elements with values or records L0, L1, …, Ln-1, sorted in ascending order, and given value/target is K, binary search is used to find the index of K in L
Set a variable start = 0 and another variable end = n-1(size of the list from the user)
if start > end break.
calculate: mid as (start + end)/2
if the value is:
equal to mid, the search is done return position of mid
greater than mid, set start to mid + 1 and repeat from step 2
less than mid, set end to mid — 1 and repeat from step 2
