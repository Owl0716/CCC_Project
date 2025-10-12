"""
Created by Thomas Hu on 2025-10-12 at 12:30 p.m.
"""
import logging
from pathlib import Path
from Common.CommonFunction import *
def main():
    lines = read_file("input/brooks.in")
    line_index = 0
    num_stream = int(lines[0])
    line_index+=1
    streams = []
    for i in range(num_stream):
        streams.append(int(lines[i+1]))
        line_index+=1
    logging.debug(streams)

    while len(lines)>line_index:
        instruction = int(lines[line_index])
        # logging.debug(instruction)
        line_index+=1
        if instruction==99:
            stream_no = int(lines[line_index])-1
            percentage = int(lines[line_index+1])-1
            volume = streams[stream_no]
            streams[stream_no]= round(volume*(100-percentage)/100)
            streams.insert(stream_no,round((volume*percentage)/100))
            line_index+=2
            # logging.debug(streams)
        if instruction == 88:
            stream_no = int(lines[line_index])-1
            volumn =streams[stream_no]+streams[stream_no+1]
            streams[stream_no] = volumn
            streams.pop(stream_no+1)
            line_index+=1
            # logging.debug(streams)
            # logging.debug(f"length: {len(lines)} line: {line_index}")
        if instruction == 77:
            break

    print(streams)

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
