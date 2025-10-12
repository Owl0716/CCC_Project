"""
Created by Thomas Hu on 2025-10-12 at 9:41 a.m.
"""
import logging
from pathlib import Path


def is_mirror_number(num):
    mirror_map = {'0':'0','1': '1', '6': '9', '8': '8', '9': '6'}
    s = str(num)

    # Build the mirrored reversed string
    mirrored = ""
    for ch in reversed(s):
        if ch not in mirror_map:
            return False
        mirrored += mirror_map[ch]
    return mirrored == s

def main():
    start_number = 1
    end_number = 100000
    results = []
    for i in range (start_number,end_number+1):
        if is_mirror_number(i):
            results.append(i)
    print(results)


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
