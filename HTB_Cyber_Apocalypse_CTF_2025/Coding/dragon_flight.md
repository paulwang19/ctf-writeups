# Dragon Flight

## Description

> In the mystical realm of the Floating Isles, ancient dragons traverse the skies between floating sanctuaries. However, unpredictable winds now pose a dynamic threat!
>
> > **Important:**
> >
> > As a Dragon Flight Master, your mission is to:
> >
> > + Handle both sudden wind changes and challenging flight path queries.
> > + Process update operations that modify the wind effect on any flight segment.
> > + Compute the maximum favorable continuous flight stretch (i.e., the maximum contiguous subarray sum) within a specified range.
>
> Your precise calculations are critical to determine the safest and most efficient route for the dragons. Adapt quickly as wind conditions change, ensuring their journey remains uninterrupted.

### Input Format Explanation

The input provided to the challenge is structured as follows:

+ **First Line:** Two space-separated integers, N and Q.
  + N represents the number of flight segments.
  + Q represents the number of operations to perform.
+ **Second Line:** N space-separated integers representing the initial net wind effects for each flight segment.
  + A **positive** value indicates a tailwind, which helps the dragon travel further.
  + A **negative** value indicates a headwind, which reduces the effective flight distance.
+ **Next Q Lines:** Each line represents an operation that can be one of the following:
  + U i x: An **update** operation where the wind effect on the i-th segment is changed to x.
  + Q l r: A **query** operation requesting the maximum contiguous subarray sum (i.e., the maximum net flight distance) for the segments in the range from l to r (inclusive).

### Flight Example

**Flight Path Input:**

```text
6 6
-10 -7 -1 -4 0 -5
Q 3 3
U 2 9
Q 6 6
U 1 -1
Q 6 6
U 5 -9
```

**Expected Output:**

```text
-1
-5
-5
```

## Idea

## Solution

[Link](../files/dragon_flight.py)
