import os
from pathlib import Path

gifs = os.listdir("gifs")
names = [Path(x).stem for x in gifs if '.gif' in x]

content = ""

for name in names:
    gif_path = f"gifs/{name}.gif"
    l_path = f"lsystems/{name}.json"
    content += name + "<br>"
    with open(l_path, 'r') as f:
        content += "<pre><code>" + f.read() + "</code></pre>"
    content += "<br>"
    content += f'\n <img src="{gif_path}">\n'
    content += "<br>"*2
    content += "<hr>"
    content += "<br>"*2

with open("template.html", 'r') as f:
    template = f.read()

with open('index.html', 'w') as f:
    f.write(template.format(content = content))






