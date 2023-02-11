# About

weights.py is a script that can mangle your prompt. The current implementation contains 2 functions.
It copies the text from the clipboard, splits it up at `,` into `expressions`.
After finishing randomization it will print out the list representation for preview and then create a prompt that is copied back to your clipboard. Further improvements will add a UI where you can interact with the prompt and different randomization methods.

- add (randomly assigns emphasis, deemphasis or no change to the `expresions`)
- remove (removes all weights)

## Installation

You need to have python3 on your system. The script was tested and developed with pyhton 3.10 on a Mac, but it should run fine with some older versions of python as well being cross platform
