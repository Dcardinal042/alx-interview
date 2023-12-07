# 0x01-lockboxes

## Lockboxes Problem

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and may contain keys to other boxes. A key with the same number as a box can open that box. The goal is to determine if all boxes can be opened, starting with the initially unlocked box.

## Function: `canUnlockAll`

The repository contains a Python script (`0-lockboxes.py`) that implements a function called `canUnlockAll`. The function takes a list of lists (`boxes`) as input and returns `True` if all boxes can be opened, otherwise `False`.

### Prototype:

```python
def canUnlockAll(boxes)

