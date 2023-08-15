#!/usr/bin/env python3
import json
import struct
import sys

try:
    from tqdm import tqdm

    iterate = lambda i: tqdm(range(i))
except ModuleNotFoundError:
    print("Warning: [tqdm] package is not available and you won't be able to see progress.", file=sys.stderr)
    iterate = range

dims = 100
num_vectors = 200_000_000


def to_json(f):
    f.read(4)  # the total number of vectors
    f.read(4)  # the vector dimension

    with open('documents.json', 'w') as f_out:
        for i in range(num_vectors):
            vector = struct.unpack("f" * dims, f.read(dims * 4))
            f_out.write(json.dumps({"vector": vector}, ensure_ascii=False))
            f_out.write("\n")


if len(sys.argv) != 2:
    print(f"Error: No vectors file. Rerun using [{sys.argv[0]} /path/to/vectors.fbin].")
    sys.exit(1)

with open(sys.argv[1], "rb") as f:
    to_json(f)
