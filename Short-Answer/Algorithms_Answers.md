#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Assume n = 2, it would loop only until a is greater than 8. Then a = 4 the first time, 8 the next time, and 12 the third time. This would mean this only loops twice.

And then let's assume n = 3, it would loop only until a is greater than 27. Then, a = 9 the first time, a = 18 next, then 27. So really it would only loop 3 times.

If we try the same thing with n = 4, it would loop only until a is greater than 64...and so a = 16 on the first pass, a = 32 on the second, a = 48 on the third, and then a = 64 on the fourth. So it would loop only 4 times.

Anyways, the point I'm making is that because it's only looping "n" times, this leads me to believe that this is ultimately O(n).

b) So for this problem, we have a for loop as the outer and a while loop in the inner.
If we start with n = 10, we know for certain that the for loop would only run "n" times. No matter what it's only going to run "n" times so we can safely say the for loop itself is O(n)...but now let's talk about the while loop. Right now, j has been defaulted to 1 and there's always a comparison that it will keep looping for as long as j is less than n. On each while loop pass, that j gets multipled by 2. So regardless of what "n" is, j will always go from 1 -> 2 -> 4 -> 8 -> 16, and so on and so forth.

So in this case, since j is always multiplying by 2, this loop will only run until 4 times for n = 10.

c) The function is calling itself down to the base case. Assume "bunnies" = 10, and since we're subtracting bunnies-1 on each recursive call, it will call itself 10 times when it reaches that base case so this is still pretty linear and thus is O(n).

## Exercise II
