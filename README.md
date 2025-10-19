# USAspending API Data Fetcher

This project helps you fetch federal spending data from the [USAspending.gov API](https://api.usaspending.gov/docs/intro-tutorial).

## Getting Started

### 1. Install Python Dependencies

First, make sure you have Python installed (Python 3.7 or higher). Then install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Run the Script

```bash
python usaspending_api.py
```

This will fetch data from the API and save it to both JSON and CSV files.

## Understanding the Code

### Basic Usage

The script fetches data from the `/api/v2/search/spending_by_award/` endpoint. By default, it:
- Fetches the 50 most recent awards
- Sorts by award amount (highest first)
- Saves data to both JSON and CSV formats

### Customizing Filters

You can customize the `filters` parameter in the `fetch_spending_data()` function. Here are some examples:

#### Filter by Award Type
```python
filters = {
    "award_type_codes": ["10"]  # 10 = Contracts, 02 = Grants, 03 = Direct Payments
}
```

#### Filter by Date Range
```python
filters = {
    "time_period": [
        {
            "start_date": "2023-10-01",
            "end_date": "2024-09-30"
        }
    ]
}
```

#### Filter by Award Amount
```python
filters = {
    "award_amounts": [
        {
            "lower_bound": 1000000.00,   # $1 million minimum
            "upper_bound": 10000000.00   # $10 million maximum
        }
    ]
}
```

#### Filter by Agency
```python
filters = {
    "agencies": [
        {
            "type": "awarding",
            "tier": "toptier",
            "name": "Department of Defense"
        }
    ]
}
```

#### Combine Multiple Filters
```python
filters = {
    "award_type_codes": ["10"],  # Contracts only
    "time_period": [{"start_date": "2024-01-01", "end_date": "2024-12-31"}],
    "award_amounts": [{"lower_bound": 1000000.00}]  # $1M or more
}
```

### Available Fields

You can customize which fields are returned by modifying the `fields` parameter:

```python
fields = [
    "Award ID",
    "Recipient Name",
    "Start Date",
    "End Date",
    "Award Amount",
    "Total Outlays",
    "Awarding Agency",
    "Awarding Sub Agency",
    "Award Type",
    "Funding Agency",
    "Funding Sub Agency",
    "Contract Award Type",
    "Period of Performance Start Date",
    "Period of Performance Current End Date"
]
```

### Handling Pagination

The API returns data in pages. To fetch multiple pages:

```python
# Fetch first 3 pages
all_results = []
for page in range(1, 4):
    data = fetch_spending_data(page=page, limit=100)
    if data:
        all_results.extend(data.get('results', []))
```

## Example: Fetching Department of Defense Contracts

```python
filters = {
    "award_type_codes": ["10"],  # Contracts
    "agencies": [
        {
            "type": "awarding",
            "tier": "toptier",
            "name": "Department of Defense"
        }
    ],
    "time_period": [
        {
            "start_date": "2024-01-01",
            "end_date": "2024-12-31"
        }
    ]
}

data = fetch_spending_data(filters=filters, limit=100)
save_to_json(data, "dod_contracts_2024.json")
save_to_csv(data, "dod_contracts_2024.csv")
```

## Resources

- [USAspending API Documentation](https://api.usaspending.gov/docs/intro-tutorial)
- [Full API Endpoints](https://api.usaspending.gov/docs/endpoints)
- [USAspending.gov Website](https://www.usaspending.gov)

## Output Files

The script generates two types of files:

1. **JSON files** (`*.json`) - Full API response including metadata
2. **CSV files** (`*.csv`) - Tabular data that can be opened in Excel or imported into databases

## Need Help?

If you're getting errors or unexpected results, check:
1. Your internet connection is working
2. The API endpoint is accessible: https://api.usaspending.gov
3. Your filter values are valid (check the API documentation)
4. You haven't exceeded any rate limits (the API is public and shouldn't have strict limits)

