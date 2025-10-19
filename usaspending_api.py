"""
USAspending API - Spending by Award Data Fetcher

This script fetches data from the USAspending API's spending_by_award endpoint
and saves it to a JSON file for your use.

Documentation: https://api.usaspending.gov/docs/intro-tutorial
"""

import requests
import json
from datetime import datetime


def fetch_spending_data(filters=None, fields=None, limit=100, page=1):
    """
    Fetch spending by award data from the USAspending API.
    
    Args:
        filters (dict): Optional filters to apply to the search
        fields (list): List of fields to return in the response
        limit (int): Number of results per page (default: 100, max: 500)
        page (int): Page number for pagination (default: 1)
    
    Returns:
        dict: API response containing award data
    """
    
    # API endpoint
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    
    # Default fields to retrieve if none specified
    if fields is None:
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
            "Funding Sub Agency"
        ]
    
    # Default filters - you can customize these!
    if filters is None:
        # Default: Get recent awards from the past year
        filters = {
            "time_period": [
                {
                    "start_date": "2024-01-01",
                    "end_date": "2024-12-31"
                }
            ]
            # Additional filter examples (uncomment to use):
            # "award_type_codes": ["10"],  # 10 = Contract, 02 = Grant, etc.
            # "award_amounts": [{"lower_bound": 1000000.00}],  # Minimum $1M
        }
    
    # Build the request payload
    payload = {
        "filters": filters,
        "fields": fields,
        "limit": limit,
        "page": page,
        "sort": "Award Amount",
        "order": "desc"
    }
    
    # Make the POST request
    print(f"Fetching data from USAspending API (page {page})...")
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad status codes
        
        data = response.json()
        print(f"✓ Successfully fetched {len(data.get('results', []))} records")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching data: {e}")
        # Try to get more details from the response
        try:
            if hasattr(e.response, 'text'):
                error_detail = e.response.json() if e.response.text else {}
                if error_detail:
                    print(f"   API Error Details: {error_detail}")
        except:
            pass
        return None


def save_to_json(data, filename=None):
    """Save the API response to a JSON file."""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"usaspending_data_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Data saved to {filename}")
    return filename


def save_to_csv(data, filename=None):
    """Save the API response to a CSV file."""
    import csv
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"usaspending_data_{timestamp}.csv"
    
    results = data.get('results', [])
    if not results:
        print("No results to save")
        return None
    
    # Get all unique keys from all results
    fieldnames = list(results[0].keys())
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print(f"✓ Data saved to {filename}")
    return filename


def main():
    """Main function to demonstrate API usage."""
    
    print("=" * 60)
    print("USAspending API - Spending by Award Data Fetcher")
    print("=" * 60)
    print()
    
    # Example 1: Basic request with default filters
    print("Example 1: Fetching recent award data...")
    data = fetch_spending_data(limit=50)
    
    if data:
        # Display summary information
        print(f"\nTotal results available: {data.get('page_metadata', {}).get('total', 0):,}")
        print(f"Current page: {data.get('page_metadata', {}).get('page', 1)}")
        print(f"Results on this page: {len(data.get('results', []))}")
        
        # Save the data
        print("\nSaving data...")
        save_to_json(data, "usaspending_awards.json")
        save_to_csv(data, "usaspending_awards.csv")
        
        # Display first few results
        print("\n" + "=" * 60)
        print("Sample of results:")
        print("=" * 60)
        for i, result in enumerate(data.get('results', [])[:3], 1):
            print(f"\nAward {i}:")
            print(f"  Recipient: {result.get('Recipient Name', 'N/A')}")
            print(f"  Amount: ${result.get('Award Amount', 0):,.2f}")
            print(f"  Agency: {result.get('Awarding Agency', 'N/A')}")
            print(f"  Type: {result.get('Award Type', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("Done! You can now customize the filters in this script.")
    print("=" * 60)


if __name__ == "__main__":
    main()

