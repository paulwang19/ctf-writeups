# Dragon Fury

## Description

> In the epic battle against Malakar's dark forces, the ancient dragons must unleash a series of precise attacks. Each attack round offers several potential damage values—but only one combination of attacks will sum up exactly to the damage required to vanquish the enemy.

### Your Task

Read a single string that represents a list of subarrays. Each subarray contains possible damage values for one round.

**Example:**

```text
[[13, 15, 27, 17], [24, 15, 28, 6, 15, 16], [7, 25, 10, 14, 11], [23, 30, 14, 10]]
```

Read an integer T that represents the target total damage required. Pick exactly one number from each subarray so that their sum equals T. It is guaranteed that there is exactly one valid solution.

Output the valid combination (as a list) that meets the target damage.

### Example

**Input:**

```text
[[13, 15, 27, 17], [24, 15, 28, 6, 15, 16], [7, 25, 10, 14, 11], [23, 30, 14, 10]]
77
```

**Output:**

```text
[13, 24, 10, 30] 
```

> Explanation:
>
> The input represents 4 rounds of attacks, each with a list of possible damage values. The unique valid solution is the combination
>
> ```text
> [13, 24, 10, 30]
> ```
>
> which sums exactly to 77.

## Idea

從 n 個給定的 list，各挑出 1 個數字，使 n 個數字總和為給定目標值。

採用動態規劃解題，以一個 `dp` 陣列來儲存，以索引 `i` 值表示目前挑選數字總和為 `i` 的組合，例如: `dp[20] = [4, 2, 11, 3]`，表示目前總和為 20 的組合方法為從 4 個 list 中分別挑出 4, 2, 11, 3。

流程:

1. 從給定 n 個 list 中的第一個開始，將其元素值存入 `dp` 對應索引的元素 list
2. 處理剩餘 n-1 個 list，每個 list 中每個元素，分別與目前 `dp` 已存在組合，加上該元素，得出新目標值索引，將組合存入 `new_dp` 目標值索引。
    假設 `dp` 存在目標值 `prev_target`，當前處理 list 元素值為 `current_round_value`，則

    ```python
    new_dp[prev_target + current_round_value] = dp[prev_target] + [current_round_value]
    ```

### 注意

+ list 的 copy 要採用 deep copy，否則造成錯誤

## Solution

[Link](../files/dragon_fury.py)
