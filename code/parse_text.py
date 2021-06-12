import os
import os.path as osp
import tika.parser

def parse_text(download_dir, parse_dir):
    os.makedirs(parse_dir, exist_ok=True)

    for it in os.dir(download_dir):
        name, ext = osp.splitext(it)
        if ext == ".pdf":
            raw = tika.parser.from_file(osp.join(download_dir, it))
            with open(osp.join(parse_dir, f"{name}.txt"), "w", encoding="utf-8") as f:
                f.write(raw["content"])

if __name__ == "__main__":
    download_dir = osp.join(osp.dirname(__file__), "..", "data", "articles_pdf")
    parse_dir =  osp.join(osp.dirname(__file__), "..", "data", "articles_text")
    
    parse_pdf(download_dir, parse_dir)
