# EndlessCycle

## Description

The elves have whispered to Elowen that the key to the Dragon's Heart is never directly visible; instead, there are clues in all the sounds and movements hidden in the world

[Attachment link](../files/rev_endlesscycle/challenge)

## Solution

### 檢測檔案

拿到檔案後，將他丟進 DIE 檢測，發現是個 ELF64 檔案。將他放進 Ubuntu 執行，他請使用者輸入一個 flag，隨意輸入 "123" 後，他輸出 "The mysteries of the universe remain closed to you..."，看起來是錯誤的意思。

```shell
$ ./challenge
What is the flag? 123
The mysteries of the universe remain closed to you...
```

### 分析程式主邏輯

使用 IDA 分析這個檔案，直接進入反編譯的 main 函式部分。

```C
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  unsigned __int64 i; // [rsp+0h] [rbp-20h]
  unsigned __int64 j; // [rsp+8h] [rbp-18h]
  unsigned int (*v6)(void); // [rsp+10h] [rbp-10h]

  v6 = (unsigned int (*)(void))mmap(0LL, 0x9EuLL, 7, 33, -1, 0LL);
  srand(seed);
  for ( i = 0LL; i <= 0x9D; ++i )
  {
    for ( j = 0LL; j < dword_4040[i]; ++j )
      rand();
    *((_BYTE *)v6 + i) = rand();
  }
  if ( v6() == 1 )
    puts("You catch a brief glimpse of the Dragon's Heart - the truth has been revealed to you");
  else
    puts("The mysteries of the universe remain closed to you...");
  return 0LL;
}
```

關鍵部分為 `v6() == 1`，看起來 `v6` 經過前面部分的處理後，指到了一個函式，這個函式執行完若回傳 `1` 表示正確。

在 main 函式中我沒看到有關讓使用者 input 的邏輯，因此可以猜測，`v6` 內應該包含讓使用者輸入的邏輯。

由於 `v6` 是個動態函式，所以我直接在執行處下斷點，動態執行起來再透過 `step into` 進到 `v6` 查看。

進到 `v6` 後，再繼續往下執行幾步，發現讓使用者輸入字串的 syscall。

```asm
zero:00007F3395745034 sub     rsp, 100h
zero:00007F339574503B mov     r12, rsp
zero:00007F339574503E xor     eax, eax
zero:00007F3395745040 xor     edi, edi
zero:00007F3395745042 xor     edx, edx
zero:00007F3395745044 mov     dh, 1
zero:00007F3395745046 mov     rsi, r12
zero:00007F3395745049 syscall            ; LINUX - sys_read
```

`sub rsp, 100h` 在 stack 上分配 100 bytes 空間，`mov r12, rsp` 讓 `r12` 指向這個空間。

> `syscall`：執行 Linux 系統呼叫，根據 Linux x86-64 系統呼叫的約定
>
> - rax : 系統呼叫號碼。
> - rdi：第一個參數，檔案描述符（fd）
> - rsi：第二個參數，寫入緩衝區位址（buf）
> - rdx：第三個參數，讀取的位元組數（count）

以上這個系統呼叫執行的是

```C
read(0, r12, 256);
```

表示將使用者輸入讀進 r12。

### 分析檢測邏輯

接著繼續往下執行。

```asm
zero:00007F339574504B test    rax, rax
zero:00007F339574504E jle     short locret_7F3395745082
zero:00007F3395745050 push    1Ah
zero:00007F3395745052 pop     rax
zero:00007F3395745053 mov     rcx, r12
zero:00007F3395745056 add     rax, rcx
```

首先 `test rax, rax` 對 `rax` 做 xor 運算，以其結果修改 `ZF` flag 及 `SF` flag，再透過 `jle short locret_7F3395745082` 比較是否小於等於（檢查 `ZF` 及 `SF`），決定是否跳轉，以上語意等同於檢測 `rax` 是否小於等於 0。

`rax` 為前面 `sys_read` 的回傳值，`sys_read` 會回傳使用者輸入的 bytes 數，因此若使用者輸入失敗（回傳小於 0）或沒輸入內容（回傳 0），則跳轉至 `locret_7F3395745082`。

> 簡單看一下 `locret_7F3395745082` 會離開函式，看起來不是我們要的。
>
> ```asm
> zero:00007F3395745082 leave
> zero:00007F3395745083 retn
> ```

回到程式碼，若使用者正常輸入，將讓 `rcx` 指向 `r12` 緩衝區起始位址，再讓 `rax` 指向 `r12` 緩衝區偏移 26 bytes 的位置（`r12` + 26）。

```asm
zero:00007F3395745059 loc_7F3395745059:
zero:00007F3395745059 xor     dword ptr [rcx], 0h
zero:00007F339574505F add     rcx, 4
zero:00007F3395745063 cmp     rcx, rax
zero:00007F3395745066 jb      short loc_7F3395745059
```

這邊是個迴圈，將使用者的輸入，每 4 個 bytes 與 `0xBEEFCAFE` 做 xor 運算並存回，總共處理 28 bytes （大於 `rax` 的 `r12` + 12 後停止）。

```asm
zero:00007F3395745068 mov     rdi, r12
zero:00007F339574506B lea     rsi, unk_7F3395745084
zero:00007F3395745072 mov     rcx, 1Ah
zero:00007F3395745079 cld
zero:00007F339574507A repe cmpsb
zero:00007F339574507C setz    al
zero:00007F339574507F movzx   eax, al
```

> `repe cmpsb` 是個組合而成的字串比較指令
>
> - `cmpsb`：比較 `rdi` 和 `rsi` 指向的位元組，並根據結果設置旗標。
> - `repe`：重複執行 `cmpsb`，直到 `rcx` 為 0 或發現不相等的位元組（`ZF` = `0`）。
> - 總共比較 26 位元組（`rcx` = `0x1A`）。

以上比較使用者輸入的 26 個位元組經過前面 xor 運算後，是否與 `unk_7F3395745084` 的 26 個位元組一致。

若完全一致，則 `ZF` 將會是 `1`，再透過最後兩行指令，設定函式回傳值為 1。

### 還原正確輸入

$M\oplus K=C$ 可由逆運算 $M=C\oplus K$ 得到原始內容，因此提取 `unk_7F3395745084` 的 26 個位元組內容，每 4 個 bytes 與 `0xBEEFCAFE` 做 xor 運算，即可還原出正確輸入。

提取 `unk_7F3395745084` 的 26 個 bytes 如下

```text
B6 9E AD C5 92 FA DF D5 A1 A8 DC C7 CE A4 8B E1 8A A2 DC E1 89 FA 9D D2 9A B7
```

利用 LLM 尋求逆運算，轉換成字元後即得到正確輸入結果如下:

```text
HTB{l00k_b3y0nd_th3_w0rld}
```

### 驗證

執行程式，驗證輸入

```shell
$ ./challenge 
What is the flag? HTB{l00k_b3y0nd_th3_w0rld}
You catch a brief glimpse of the Dragon's Heart - the truth has been revealed to you
```
