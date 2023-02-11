#!/usr/bin/env python
# %%
from dataclasses import dataclass
from enum import Enum
import pyperclip
import random
import typer
from rich import print
from rich.pretty import pprint

app = typer.Typer()

class Kind(Enum):
    none = 0,
    emphasis = 1,
    deemphasis = 2


@dataclass
class Expression:
    text: str
    weight: float
    kind: Kind

@app.command()
def add(text:str="", min:float=0.001, max:float=1.400):
    if len(text) == 0:
        text = pyperclip.paste()
    items = parse(text)
    result = []
    for item in [*items]:
        item.weight = random.uniform(min, max)
        if item.kind == Kind.none:
            item.kind = random.choice(list(Kind))
        result.append(item)
    copy(result)
    return result

@app.command()
def remove():
    items = parse(pyperclip.paste())
    result = [ Expression(x.text, 0, Kind.none) for x in items]
    copy(result)


def parse(prompt:str=""):
    text_parts = prompt.split(',')
    result = [format(text) for text in text_parts]
    copy(result)
    return result

def format(input:str):
    characters=""
    kind = Kind.none
    
    if '(' in input: 
        kind = Kind.emphasis
        characters = '()'
    elif '[' in input:
        kind = Kind.deemphasis
        characters = '[]' 
    elif ':' in input:
        kind = Kind.emphasis

    input = input.strip()

    if len(characters)>0:
        input = input.strip(characters)

    parsed = input.split(":")

    return Expression(
        text = parsed[0],
        weight = float(parsed[1]) if len(parsed) > 1 else 0,
        kind = kind
    )

def copy(result:list[Expression], precission=2):
    open=""
    close=""
    
    parts: list[str] = []
    for x in result:
        text = x.text
        if x.kind == Kind.emphasis:
            open = "("
            close = ")"
        elif x.kind == Kind.deemphasis:
            open= "["
            close="]"

        if x.weight > 0:
            text = f'{open}{x.text}:{round(x.weight, precission)}{close}'
        parts.append(text)
    
    print(parts)
    pyperclip.copy(", ".join(parts))



if __name__ == '__main__':
    app()
