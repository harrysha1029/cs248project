from collections.abc import Iterable
import src.lsystem as L
from src.turtle import CONSTS, CHAR_TO_DRAW_FN
import json
import numbers

import imageio



from pathlib import Path

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def check_types(params):
    pairs = [
          ("symbols", list)
        , ("start", str)
        , ("production_rules", dict)
        , ("pos" , tuple)
        , ("angle" , numbers.Number)
        , ("turning_angle" , numbers.Number)
        , ("length_scale_factor" , numbers.Number)
        , ("swap_plus_minus" , bool)
    ]
    for v, t in pairs:
        if v in params:
            val = params[v]
            assert isinstance(val, t), f"The LSystem parameter {v} has type {type(val)} it should have type {t}"


def check_valid(params):

    assert 'start' in params.keys(), "There must be a start attribute"
    assert 'production_rules' in params.keys(), "There must be a production_results attribute"

    check_types(params)

    symbols = list(set(params['symbols']) | set(CONSTS))

    # ======= Check valid start symbol =======
    for c in params["start"]:
        assert c in symbols, "start string must use a subset of the defined symbols"

    # ======= Check outputs of production rules are valid =======
    for k, v in params['production_rules'].items():
        for vi in v:
            assert (
                vi in symbols
            ), f"production rule {k} -> {v} contains undefined symbol {vi}"
    
    print("Valid LSystem!")


def advance_lsystem_string(lsystem, string):
    new_string = ""
    for char in string:
        if char in lsystem.production_rules.keys():
            new_string += lsystem.production_rules[char]
        else:
            new_string += char
    return new_string


def compute_lsystem_string(lsystem, n):
    s = lsystem.start
    for _ in range(n):
        s = advance_lsystem_string(lsystem, s)
    return s

def compile(path, n, transparent=False, fname_no_ext=None):
    lsystem_params = load_json(path)
    check_valid(lsystem_params)

    lsystem = L.LSystem(**lsystem_params, transparent=transparent)
    string_to_draw = compute_lsystem_string(lsystem, n)

    lsystem.turtle.draw(string_to_draw)

    if fname_no_ext is None:
        name = "figs/"+ Path(path).stem
    else:
        name = fname_no_ext
        
    out_path = name + f"_{n}.svg"
    lsystem.save(out_path)
    out_path = name + f"_{n}.png"
    lsystem.save(out_path)
    return out_path

def compile_range(path, start, end, transparent=False):
    filenames = [compile(path, n, transparent) for n in range(start, end)]
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    print(len(images))

    imageio.mimsave('gifs/' + Path(path).stem + '.gif', images, duration=0.4)




