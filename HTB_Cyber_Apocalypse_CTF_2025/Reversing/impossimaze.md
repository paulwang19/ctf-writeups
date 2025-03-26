# Impossimaze

## Description

Elowen has been cursed to roam forever in an inescapable maze. You need to break her curse and set her free.

[Attachment link](../files/rev_impossimaze/main)

## Solution

### Detect the file

I first detect the file by putting it into DIE, and I found that it is ELF64 format. When I run it on Ubuntu, the output shows below.

![image](../files/rev_impossimaze/impossimaze_output.png)

### Analysis decompiled code

I wanted to know the original program flow, so I used IDA to analyze this file. Checking the "main" part of the decompiled code, I found it to be a TUI program made by ncurses, a common Linux library for creating TUIs.
