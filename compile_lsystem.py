from src.turtle import TurtleDrawing
import src.compile as comp
import argparse

parser = argparse.ArgumentParser(description='Compiles LSystem')
parser.add_argument('path', type=str, help='path containing LSystem')
parser.add_argument('-n', type=int, help='iteration depth', default=4)
parser.add_argument('-r', '--range', help='range of depths to run', type=int, nargs=2, default=(0,0))
parser.add_argument('-t', '--transparent', action="store_true", help='transparent', default=False)
args = parser.parse_args()


if args.range[0] != 0 or args.range[1] != 0:
    comp.compile_range(args.path, args.range[0], args.range[1], args.transparent)
else:
    comp.compile(args.path, args.n, args.transparent)