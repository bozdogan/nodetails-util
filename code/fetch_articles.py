import os.path as osp
from download_pdfs import download_pdfs
from parse_text import parse_text
from scrap_arxiv_links import scrap_arxiv_links


if __name__ == "__main__":
    download_dir = osp.join(osp.dirname(__file__),
                            "..", "data", "articles_pdf")
    parse_dir =  osp.join(osp.dirname(__file__),
                          "..", "data", "articles_text")

    pdf_links = scrap_arxiv_links(category='physics:cond-mat')

    with open(osp.join("data","pdf_links.txt"), "w") as f:
        f.write("\n".join(pdf_links))

    print("Download dir:", download_dir)
    download_pdfs(pdf_links, download_dir)
    
    print("Parse dir:", parse_dir)
    parse_text(download_dir, parse_dir)

# END OF fetch_articles.py
