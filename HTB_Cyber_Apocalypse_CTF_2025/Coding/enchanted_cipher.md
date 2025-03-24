# Enchanted Cipher

## Description

> The Grand Arcane Codex has been corrupted, altering historical records. Each entry has been encoded with an enchanted shifting cipher that encrypts a plaintext composed of 3–7 randomly generated words.
>
> The cipher operates as follows:
>
> + Alphabetical characters are processed in groups of 5 (ignoring non-alphabetical characters).
> + For each group, a random shift between 1 and 25 is chosen and applied to every letter in that group.
> + After the encoded message, an additional line indicates the total number of shift groups, followed by another line listing the random shift values used for each group.
>
> Your quest is to decode the given input and restore the original plaintext.

### Example

**Input:**

```text
ibeqtsl
2
[4, 7]
```

**Output:**

```text
example
```

## Idea

給定凱薩加密字串，將其還原成原文，本題較特別的是，原文字串是以每 5 個字母為一組 (非字母字元不算)，分組為整段字串加密的，因此還原時，需考慮存在非字母字元情況下，取得一組 5 個字母字元的子字串。

流程:

1. `for` 迴圈給定 key 列表，取得下一個 key
2. 從加密字串取得下一組子字串
3. 將該字串依據 key 凱薩解密成原始字串

## Solution

[Link](../files/enchanted_cipher.py)
