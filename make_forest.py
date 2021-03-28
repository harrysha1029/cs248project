import drawSvg as draw
import src.compile as comp
import random
from pathlib import Path

things = [
    ("lsystems/leaf.json", 6)
    , ("lsystems/leaf.json", 7)
    , ("lsystems/leaf.json", 8) , ("lsystems/bush1.json", 4) , ("lsystems/bush1.json", 5) , ("lsystems/bush2.json", 4) , ("lsystems/bush2.json", 5)
          , ("lsystems/bush3.json", 4)
    , ("lsystems/bush3.json", 5)
    , ("lsystems/bush4.json", 4)
    , ("lsystems/bush5.json", 6)
    , ("lsystems/bush5.json", 7)
    , ("lsystems/bush5.json", 8)
]

fnames_png = [comp.compile(l, n, True, "figs/" + Path(l).stem + "_transparent") for l, n in things]
PATHS = [Path(x).with_suffix('.svg') for x in fnames_png]

N_TREES = 50


forest = draw.Drawing(1000,1000)

forest.append(
    draw.Rectangle(0,0,1000,1000,fill='white')
)

for _ in range(N_TREES):
    x = random.randint(0, 1000)
    y = random.randint(0, 500)
    p = random.choice(PATHS)
    im = draw.Image(x, y, width=200, height=200, path=p, embed=True)
    forest.append(im)

forest.saveSvg("figs/forest.svg")
