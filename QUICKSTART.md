# Quick Start Guide

## Setup (2 minutes)

1. **Install Python package:**
   ```bash
   pip install requests
   ```

2. **Run the basic script:**
   ```bash
   python usaspending_api.py
   ```

That's it! You'll get two files:
- `usaspending_awards.json` - Full data with metadata
- `usaspending_awards.csv` - Table format (open in Excel)

## Next Steps

### Try Examples
```bash
python examples.py
```

This will generate sample data files showing different ways to filter the data.

### Customize for Your Needs

Edit `usaspending_api.py` and modify the filters in the `main()` function:

```python
# Example: Get contracts over $1M from 2024
filters = {
    "award_type_codes": ["10"],  # Contracts
    "award_amounts": [{"lower_bound": 1000000.00}],
    "time_period": [{
        "start_date": "2024-01-01",
        "end_date": "2024-12-31"
    }]
}

data = fetch_spending_data(filters=filters, limit=100)
```

## Common Award Type Codes

- `"10"` - Contracts
- `"02"` - Grants
- `"03"` - Direct Payments
- `"04"` - Loans
- `"05"` - Other Financial Assistance
- `"06"` - Insurance
- `"07"` - Other
- `"08"` - Other
- `"09"` - Other
- `"11"` - IDV (Indefinite Delivery Vehicle)

## Common Agency Names

- "Department of Defense"
- "Department of Health and Human Services"
- "Department of Education"
- "Department of Transportation"
- "Department of Energy"
- "National Aeronautics and Space Administration"
- "Environmental Protection Agency"
- "Social Security Administration"

## Getting Help

- Full documentation: See `README.md`
- API docs: https://api.usaspending.gov/docs/endpoints
- Code examples: See `examples.py`

## Troubleshooting

**"No module named 'requests'"**
- Run: `pip install requests`

**"No results found"**
- Your filters might be too restrictive
- Try removing some filters or broadening date ranges

**"Connection error"**
- Check your internet connection
- The API might be temporarily down (rare)

