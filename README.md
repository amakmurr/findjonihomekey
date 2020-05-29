[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Find Joni's Home Key
This code is solution to find how many `.` (dot) become the possibility to find Joni's key from below board.
<pre>
# # # # # # # #	
# . . . . . . #	
# . # # # . . #	
# . . . # . # #	
# X # . . . . #	
# # # # # # # #
</pre>
To find his home key there's rules to be followed, there are:
1. Walk to the north `A` step(s).
2. Then walk to the east `B` step(s).
3. Last, walk to the south `C` step(s).

If:

`A`, `B`, `C` are the missing step.

`.` (dot) is available floor where Joni can walk and where’s the key kept.

`#` (hashtag) is unavailable floor where Jony’s prohibited to walk it.

`X` is Joni current position.

So how many `.` (dot) become the possibility to find Joni’s key, if the missing number is positive integers?

## How to find out
```
python main.py
```

## Known Issue
1. There's taken steps does not make sense on output
2. Not tested yet on other board configuration
