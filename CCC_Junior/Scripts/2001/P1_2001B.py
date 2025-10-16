"""
Created by Thomas Hu on 2025-10-14 at 9:57 a.m.
"""
import logging
from pathlib import Path

def main():
    height = 5
    line_str = ""
    for i in range(height):
        for j in range(height):
            line_str+="*"


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
