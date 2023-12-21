# AMEX Statement Processor

This project provides scripts to process your AMEX statement. It helps you categorize your expenses and calculate your average monthly spend per category.

## Prerequisites

- Python 3
- Pipenv

## Setup

1. Clone this repository.
2. Install the dependencies using Pipenv: `pipenv install`
3. Copy `config_TEMPLATE.json` to `config.json`: `cp config_TEMPLATE.json config.json`

## Usage

1. Access your AMEX account on the web (the mobile version doesn't support downloading the statement in the required format). Select a date range and download the statement as a CSV file, making sure to check the box to include all information.
2. Run the preprocessor script: `pipenv run python amex_pre.py activity.csv processed.csv`
3. Check the output, adjust `config.json` as needed, and re-run the preprocessor.
4. Manually review the output of the preprocessor script and correct any categorization errors or remove any unnecessary entries.
5. Run the postprocessor script, passing in the processed file and the number of months that the statement represents: `pipenv run python amex_post.py processed.csv <num_months>`

## Configuration

You can customize the behavior of the scripts by modifying `config.json`. Run the preprocessor script once to see how it categorizes your expenses, then adjust `config.json` as needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)