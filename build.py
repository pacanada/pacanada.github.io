import os
import markdown

class Page:
    def __init__(self, filepath):
        self.filepath = filepath
        self.title = 
        self.subtitle = 
    def parse_doc(self):
        


def create_index(l: list):
    links = ""
    for a in l:
        links+=f"""<p><a href="{a}">{a}</a></p>\n"""

    output = f"""<!DOCTYPE html>
    <body>
        {links}
    </body>
    """
    with open("docs/index.html", "w") as f:
        f.write(output)

def get_markdown_files():
    return os.listdir("entries/")



a = get_markdown_files()
create_index(a)

for md in a:

    markdown.markdownFromFile(
        input=f"entries/{md}",
        output=f"docs/{md[:-3]}.html",
        encoding="utf8",
    )