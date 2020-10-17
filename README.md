# Cointoss probability

This script was written in the course Logic and Maths for Computing/Computer science.
The task was to write a script that would calculate the probability of getting **X** heads in **X** tosses.

The given requirements was:
Formula to abide to

![Equation](https://render.githubusercontent.com/render/math?math=P(n%2Ck)%20%3D%20%5Cleft(%5Cfrac%7Bk%7D%7Bn%7D%5Cright%20)%5Cleft(%5Cfrac%7B1%7D%7B2%7D%5Cright%20)%5E%7Bn%7D%5Cleft(1-%5Cfrac%7B1%7D%7B2%7D%5Cright%20)%5E%7Bk-n%7D%0A)

The program should run through all possible combinations of heads and tails, let the total numbers of combinations be N. If n of theese combinations have a maximum out of 4, then the probability of getting 4 in a row is n/N.
Example: 4 heads in a row in 4 tosses (probability 0.0625)
Formula
![Formula](https://render.githubusercontent.com/render/math?math=P(4%2C4)%20%3D%20%5Cleft(%5Cfrac%7B4%7D%7B4%7D%5Cright%20)%5Cleft(%5Cfrac%7B1%7D%7B2%7D%5Cright%20)%5E%7B4%7D%5Cleft(1-%5Cfrac%7B1%7D%7B2%7D%5Cright%20)%5E%7B4-4%7D%3D%5Cfrac%7B1%7D%7B16%7D%0A)
Check the validity of the result at [WolframAlpha - Computational Intelligence](https://www.wolframalpha.com/input/?i=P%28n%2Ck%29+%3D+%5Cleft%28%5Cfrac%7B4%7D%7B4%7D%5Cright+%29%5Cleft%28%5Cfrac%7B1%7D%7B2%7D%5Cright+%29%5E%7B4%7D%5Cleft%281-%5Cfrac%7B1%7D%7B2%7D%5Cright+%29%5E%7B4-4%7D)

I must warn that this script is not the best example of following standard naming conventions but I will blame it on being a student and not knowing better :-)

### Run the script
The script is interactive and will ask runtime questions.
```python
$ python toss.py
```

# Remember

  - This was a school assignment during my time studying IT-Security and Software testing - this is not guaranteed to work 100%.
  - Do not copy and use this in your school assignments, instead learn from it and improve it.
  - This will not be maintained by me, this is uploaded for safekeeping online.

License
----

MIT


**Free Software, Hell Yeah!**
