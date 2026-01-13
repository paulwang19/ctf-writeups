# ClockWork Gurdian

## Description

> The Clockwork Sentinels defending Eldoria's Skywatch Spire have gone rogue! You must navigate through the spire, avoiding hostile sentinels and finding the safest path to the exit.
>
> Write an algorithm to find the shortest safe path from the start position (0,0) to the exit ('E'), avoiding the sentinels (1).

### Example

**Grid:**

```text
[
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 'E']
]
```

**Output:**

```text
8
```

> Visualization:
>
> ```text
> Row 0: S   1   X   0   0   X
> Row 1: 0   2   3   4   5   6
> Row 2: 0   0   0   0   0   7
> Row 3: 0   0   X   X   0   E
> ```
>
> Path Length: 8

## Idea

走迷宮，起點在左上角，座標位置(0,0)，計算走到右下角的路徑長。

採用回溯法，每次走到 `0` 時，紀錄已走過「這個位置」，再分別嘗試往上、下、左、右四個方向前進，若四個方向都走不到終點就退回原本位置，否則比較上、下、左、右四個方向中距離走到終點的最短路徑長，將最短路徑長加上 1 即為「這個位置」距離終點的最短路徑長。

## Solution

[Link](../files/clockwork_guardian.py)
