import argparse
from ast import arg

def main(sum, a,b):
    if sum:
        return a +b

    else:

        return a -b

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--Sum", "-s", default=True)
    args.add_argument("--a",default=10)
    args.add_argument("--b", default=20)
    parsed_args = args.parse_args()
    print(parsed_args)
    print(parsed_args.sum)
    main()
