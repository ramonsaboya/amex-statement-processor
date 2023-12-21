import pandas as pd
import json
import argparse

category_selector = lambda arr: max(arr, key=arr.tolist().count) if len(arr) > 0 else None

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
        dedup = config.get('dedup', {})
        special_replacements = config.get('special_replacements', {})
        category_mapping = config.get('category_mapping', {})

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The CSV file to process')
    parser.add_argument('output_file', help='The CSV file to write the results to')
    args = parser.parse_args()

    # Read the CSV file
    df = pd.read_csv(args.input_file)

    df = df.drop(columns=['Date','Extended Details','Appears On Your Statement As','Address','Town/City','Postcode','Country','Reference'])
    df = df.rename(columns={'Description': 'Item'})
    df = df[df['Amount'] >= 0]
    df['Item'] = df['Item'].str.split('  ').str[0]
    df['Item'] = df['Item'].apply(lambda x: ' '.join(special_replacements.get(word, word) for word in x.split()))
    df['Item'] = df['Item'].apply(lambda x: ''.join(char for char in x if char.isalnum() or char.isspace()))
    df = df.groupby('Item').agg({'Amount': 'sum', 'Category': category_selector}).reset_index()
    df = df.reindex(columns=['Amount', 'Item', 'Category'])
    df['Item'] = df['Item'].str.upper()

    for item in dedup:
        df = agg_items(df, item)

    df['Category'] = df['Category'].apply(lambda x: category_mapping.get(x, x))

    df = df.sort_values(by=['Category','Item'])
    df = df.reset_index(drop=True)

    df.to_csv(args.output_file, index=False)

def agg_items(df, item):
    mask = df['Item'].str.contains(item, case=False)
    grouping = df[mask].groupby(lambda x: item).agg({'Amount': 'sum', 'Category': category_selector}).reset_index()
    grouping = grouping.rename(columns={'index': 'Item'})
    df = pd.concat([df[~mask], grouping], ignore_index=True)
    return df

if __name__ == "__main__":
    main()

