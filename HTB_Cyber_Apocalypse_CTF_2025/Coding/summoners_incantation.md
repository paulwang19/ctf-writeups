# Summoners Incantation

## Description

> Deep within the ancient halls lies the secret of the Dragon's Heart—a power that can only be unlocked by combining magical tokens in just the right way. The tokens are delicate: if you combine two adjacent tokens, their energy dissipates into the void.
>
> Your quest is to determine the maximum amount of energy that can be harnessed by selecting tokens such that no two selected tokens are adjacent. This challenge is equivalent to finding the maximum sum of non-adjacent numbers from a list.

### Your Quest

**Input Format:**

```text
A single line containing a Python-style list of integers representing token energies.
Example: [3, 2, 5, 10, 7]
```

**Output Format:**

```text
A single integer that is the maximum energy obtainable by summing non-adjacent tokens.
```

### Example

**Input:**

```text
[3, 2, 5, 10, 7]
```

**Output:**

```text
25
```

> Explanation: The best choice is to select 18 and 7 (tokens at positions 2 and 4) for a total of 18 + 7 = 25.

## Idea

這是經典 House Robber 問題，取 n 個不相鄰數，使其總和為最大的取法。

用動態規劃解題，`dp` 陣列中索引 `i` 值表示 list 前 `i` 個數總和的最大值。

對於每個位置 `i`，有兩個可能:

+ 選擇當前數字，則不可選第 `i-1` 個數字，總和為 `dp[i-2]` 加上當前數字
+ 不選當前數字，則當前總和為 `dp[i-1]`

## Solution

[Link](../files/summoners_incantation.py)
