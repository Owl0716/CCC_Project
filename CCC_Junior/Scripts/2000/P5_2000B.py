"""
Created by Thomas Hu on 2025-10-12 at 3:43 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *

links = {}

def getURLs(content):
    urls = []
    parts = content.split('HREF="')
    for p in parts[1:]:
        url = p.split('"')[0]
        urls.append(url)
    return urls

def read_html(lines, line_index):
    content = ""
    url = lines[0]
    for line in lines[1:]:
        line_index+=1
        if line=="</HTML>":
            content +=line
            break
        content +=line.strip()+" "
    urls = getURLs(content)
    links[url]= urls
    logging.debug(urls)
    logging.debug(f"line_index: {line_index}: content: {content}")
    return line_index+1

def check_links(from_link, to_link):
    link_list = links.get(from_link,None)
    if link_list:
        return to_link in link_list
    else:
        return False

def main():
    lines = read_file("input/surf.in")
    line_index = 1
    num_html = int(lines[0])
    for i in range(num_html):
        line_index = read_html(lines[line_index:], line_index)
    while(True):
        line = lines[line_index]
        if line=="The End":
            break
        from_link = lines[line_index]
        to_link = lines[line_index+1]
        logging.debug(f"from link:{from_link} to link: {to_link}")
        logging.debug(f"{links}")
        if check_links(from_link,to_link):
            print(f"Can surf from {from_link} to {to_link}")
        else:
            print(f"Can't surf from {from_link}")
        line_index+=2


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        handlers=[
            logging.StreamHandler()  # log to console
        ],
        force=True,
    )
    logging.info("Started")
    main()
    logging.info("Finished Successfully")
