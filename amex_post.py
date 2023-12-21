import pandas as pd
import math
import argparse

def main():
    args = argparse.ArgumentParser()
    args.add_argument('file', type=str, help='Path to the CSV file')
    args.add_argument('months', type=int, help='Number of months')
    args = args.parse_args()

    df = pd.read_csv(args.file)
    print(df.groupby('Category').agg({'Amount': lambda x: math.ceil(x.sum() / args.months)}).reset_index())  # Divide sum of amounts by the number of months

if __name__ == '__main__':
    main()
