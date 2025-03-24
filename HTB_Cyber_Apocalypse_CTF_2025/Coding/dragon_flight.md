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

本題為尋找連續子陣列的最大總和，想法為從左至右遍歷一次陣列，遇到新元素時，計算從第一個元素到目前元素的子陣列最大總和。

假設 `num` 陣列紀錄陣列元素，當目前遇到 `num[i]` 時，有兩種可能:

1. 開始一個新的子陣列，將 `num[i]` 視為新子陣列第一項
2. 將 `num[i]` 接在前一個元素的最大總和子陣列後面

這表示，針對遇到 `num[i]` 的子陣列最大總和，公式為 *max(到 `num[i-1]` 時子陣列的最大總和 + `num[i]`, `num[i]`)*

## Solution

[Link](../files/dragon_flight.py)
