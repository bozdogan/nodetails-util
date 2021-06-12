import os.path as osp
from arxivscraper import Scraper

def scrap_arxiv_links(*args, **kwargs):
    scraper = Scraper(*args, **kwargs)

    article_data = scraper.scrape()
    pdf_links = ["https://arxiv.org/pdf/%s.pdf" % it["id"] for it in article_data]
    
    return pdf_links


if __name__ == "__main__":
    outfile = osp.join(osp.dirname(__file__), "..", "data", "pdf_links.txt")
    
    links = scrap_arxiv_links(category='physics:cond-mat',
                              date_from='2017-05-27',
                              date_until='2017-06-07')
    
    with open(osp.join("..", "data", outfile), "w") as f:
        f.write("\n".join(links))
    