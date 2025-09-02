import argparse
from pathlib import Path

def main(cmd: list[str] | None = None):
    args = parse_args(cmd)
    summ = 0
    with open(args.data_path) as f:
        for line in f.readlines():
            summ += int(line.strip('\n'))
    print(summ)
    prod = 1
    with open(args.data_path) as f:
        for line in f.readlines():
            prod *= int(line.strip('\n'))
    print(prod)


def parse_args(cmd: list[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('data_path', type=Path)
    return parser.parse_args(cmd)

if __name__ == '__main__':
    main()