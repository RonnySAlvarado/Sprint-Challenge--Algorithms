#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

## a)

Assume n = 2, it would loop only until a is greater than 8. Then a = 4 the first time, 8 the next time, and 12 the third time. This would mean this only loops twice.

And then let's assume n = 3, it would loop only until a is greater than 27. Then, a = 9 the first time, a = 18 next, then 27. So really it would only loop 3 times.

If we try the same thing with n = 4, it would loop only until a is greater than 64...and so a = 16 on the first pass, a = 32 on the second, a = 48 on the third, and then a = 64 on the fourth. So it would loop only 4 times.

Anyways, the point I'm making is that because it's only looping "n" times, this leads me to believe that this is ultimately O(n).

## b)

So for this problem, we have a for loop as the outer and a while loop in the inner.
If we start with n = 10, we know for certain that the for loop would only run "n" times. No matter what it's only going to run "n" times so we can safely say the for loop itself is O(n)...but now let's talk about the while loop. Right now, j has been defaulted to 1 and there's always a comparison that it will keep looping for as long as j is less than n. On each while loop pass, that j gets multipled by 2. So regardless of what "n" is, j will always go from 1 -> 2 -> 4 -> 8 -> 16, and so on and so forth.

So in this case, since j is always multiplying by 2, this loop will only run until 4 times for n = 10.

Anyways, since it's O(n) and for the while loop since j is growing extremely slowly, it would be O(logn) which would result this to be O(n) \* O(logn) = O(nlogn)

## c)

The function is calling itself down to the base case. Assume "bunnies" = 10, and since we're subtracting bunnies-1 on each recursive call, it will call itself 10 times when it reaches that base case so this is still pretty linear and thus is O(n).

## Exercise II

For this, let's just give an example numbers...let's assume there are 20 floors. And let's assume for this problem that any eggs dropped above floor 5 breaks, but 5 and below doesn't.

So for this case, I'd probably always want to start at the center...so let's say the 10th floor. In this case, we can say that the current floor is n/2 by default.

Then, we can make some kind of evaluation.

if dropped_egg on this floor == broken egg, we're going to have to adjust the current floor. We could subtract - 1 to the current floor, but that would mean we would always be subtracting down until we find the right floor...which could take a while. In this case, we could just halve it each time. So in this case, we're on the 10th floor. The egg breaks. Let's halve it. Now, the current floor is 5.

Well, in this case, if drop an egg here, the egg doesn't break. So that's good, but now we need to check and see as well that the floor above it doesn't break. So in this case, we could write a case that if the egg dropped on current floor doesn't break and the egg dropped on the current floor + 1 breaks, we have found our "f". If the egg dropped on the current floor + 1 doesn't break...then we might have to adjust the floor a little higher. In this case, let's pretend our "f" was something like 7. Well, now we'd have to try and catch that by adjusting the current floor to basically between 10 and 5. So we could set it to what current floor + (current floor/2). Visualizing it, that would mean 5 + (5/2), which would put this at 8. Evaluate it again. If egg breaks on floor 8, we'll have to adjust again to half of 8 (current floor) and 5 (prev floor)...ultimately, we're essentially running a binary search...where we're basically just always cutting things in half until we find the solution.

This would result in this problem being O(log n)
