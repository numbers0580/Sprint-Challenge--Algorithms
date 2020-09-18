#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime for this is O(n). As a matter of fact, it's exactly O(n) and not a generalization of something like O(2n), O(3n), or O(1.2n).
The loop literally says we're going to keep adding n^2 until we go from 0 to n^3. Which takes n iterations.


b) This code's runtime is O(n^2). The first clue is the nested loop structure (for, while, do-while, all loops). The outer loop establishes
O(n), and the inner loop multiplies the number of operations by n, giving you O(n * n) = O(n^2). Had there been yet another nested loop, then it would've become O(n^3)


c) The runtime is O(C). The number of operations that needs to run is completely independent of the value passed in to the function.

## Exercise II

I would view a multi-floor building like a sorted list (unless there's some building whose floors are, in this order: 3, 14, 8, 29, 35, 5, 11, 26, 2, etc).

Since my building, and thus this list, is normal and sorted, I would use a Binary Search algorithm to minimize the eggs needed to find the sweet spot.

I would start halfway up the building that has a broken elevator forcing me to use the stairs. Once I get to the n // 2 floor, being properly exhausted
and upset about the elevator, I'd look out the window specifically to target employees to be unwitting assistants to this test... Bombs Away!

If the egg broke, then I would treat this current floor as the highest I needed to ascend and recalculate the halfway floor from the ground level to
the current floor I'm on.
If the egg didn't break, that means (ughhh...) I have more floors to climb. I would treat the current floor I'm on as the new base level and recalculate
the halfway floor from it and the top floor.
Once I get to the new halfway floor, I would repeat the test until I narrow in on one floor. At this point, I would know the egg didn't break while on
the immediate floor below me and the egg broke from the immediate floor above me. So if the egg breaks while on this floor, the answer would be the floor
below me, else it's this floor that I got to after log n iterations.

code:
```
def dodo_eggs(ground=0, top=1658, elevator="Broken"):
    # Happy climbing!
    test_floor = (ground + top) // 2
    if egg == broken:
        if test_floor - ground > 1:
            dodo_eggs(ground, test_floor - 1)
        else:
            return ground
    else:
        if top - test_floor > 1:
            dodo_eggs(test_floor + 1, top)
        else:
            return test_floor
```

As you can clearly see from the code above, the runtime would be O(log n), since while it looks like a lot of floors will be tested, we'll never actually test ALL floors
for buildings > 2 floors