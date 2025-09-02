import argparse
from pathlib import Path

summ = 0

def main(cmd: list[str] | None = None):
    args = parse_args(cmd)
    with open(args.data_path) as f:
        for line in f.readlines():
            summ += int(line.strip('\n'))
    print(summ)


def parse_args(cmd: list[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('data_path', type=Path)
    return parser.parse_args(cmd)

if __name__ == '__main__':
    main()