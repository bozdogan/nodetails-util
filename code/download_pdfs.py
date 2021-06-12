import os
import os.path as osp
import time
import requests
from progress_line import progress_line

def download_pdfs(pdf_links, download_dir):
    os.makedirs(download_dir, exist_ok=True)

    print("\nDownloading. . .")
    progress_line(0, 0)
    for i, it in enumerate(pdf_links):
        r = requests.get(it, allow_redirects=True)
        with open(osp.join(download_dir, osp.basename(it)), "wb") as f:
            f.write(r.content)

        time.sleep(1)
        progress_line(i + 1, len(pdf_links))
