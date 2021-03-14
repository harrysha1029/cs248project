from collections.abc import Iterable
import src.lsystem as L
from src.turtle import CONSTS, CHAR_TO_DRAW_FN
import json
import numbers

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
        , ("turning_angle_increment" , numbers.Number)
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
    # TODO
    pass


def compute_lsystem_string(lsystem, n):
    s = lsystem.start
    for _ in range(n):
        s = advance_lsystem_string(lsystem, s)
    return s


N = 5  # TODO make n a variable

def compile(path):
    lsystem_params = load_json(path)
    check_valid(lsystem_params)
    lsystem = L.LSystem(**lsystem_params)

    string_to_draw = compute_lsystem_string(lsystem, N)
    lsystem.turtle.draw(string_to_draw)

    out_path = "figs/" + Path(path).stem + ".svg"

    lsystem.save(out_path)