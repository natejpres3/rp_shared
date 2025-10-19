"""
Example Use Cases for USAspending API

This file contains practical examples of how to fetch different types of data
from the USAspending API.
"""

from usaspending_api import fetch_spending_data, save_to_json, save_to_csv


def example_1_recent_large_contracts():
    """Fetch recent contracts over $5 million."""
    print("\n" + "="*60)
    print("Example 1: Recent Large Contracts (over $5M)")
    print("="*60)
    
    filters = {
        "award_type_codes": ["10"],  # Contracts only
        "award_amounts": [
            {
                "lower_bound": 5000000.00  # $5 million minimum
            }
        ],
        "time_period": [
            {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }
        ]
    }
    
    data = fetch_spending_data(filters=filters, limit=25)
    if data:
        save_to_csv(data, "large_contracts.csv")
        print(f"Found {data.get('page_metadata', {}).get('total', 0):,} total records")


def example_2_grants_by_year():
    """Fetch all grants from fiscal year 2024."""
    print("\n" + "="*60)
    print("Example 2: Grants from Fiscal Year 2024")
    print("="*60)
    
    filters = {
        "award_type_codes": ["02", "03", "04", "05"],  # Various grant types
        "time_period": [
            {
                "start_date": "2023-10-01",  # FY2024 starts Oct 1, 2023
                "end_date": "2024-09-30"     # FY2024 ends Sep 30, 2024
            }
        ]
    }
    
    data = fetch_spending_data(filters=filters, limit=50)
    if data:
        save_to_csv(data, "grants_fy2024.csv")
        print(f"Found {data.get('page_metadata', {}).get('total', 0):,} total records")


def example_3_specific_agency():
    """Fetch awards from a specific agency."""
    print("\n" + "="*60)
    print("Example 3: Department of Health and Human Services Awards")
    print("="*60)
    
    filters = {
        "agencies": [
            {
                "type": "awarding",
                "tier": "toptier",
                "name": "Department of Health and Human Services"
            }
        ],
        "time_period": [
            {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }
        ]
    }
    
    data = fetch_spending_data(filters=filters, limit=50)
    if data:
        save_to_csv(data, "hhs_awards_2024.csv")
        print(f"Found {data.get('page_metadata', {}).get('total', 0):,} total records")


def example_4_fetch_multiple_pages():
    """Fetch multiple pages of results to get more data."""
    print("\n" + "="*60)
    print("Example 4: Fetching Multiple Pages (300 records)")
    print("="*60)
    
    filters = {
        "award_type_codes": ["10"],  # Contracts
        "time_period": [
            {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }
        ]
    }
    
    all_results = []
    
    # Fetch 3 pages of 100 results each
    for page_num in range(1, 4):
        data = fetch_spending_data(filters=filters, limit=100, page=page_num)
        if data and 'results' in data:
            all_results.extend(data.get('results', []))
            print(f"  Fetched page {page_num}: {len(data.get('results', []))} records")
    
    # Create a combined result
    combined_data = {
        'results': all_results,
        'page_metadata': {
            'total': len(all_results),
            'pages': 3
        }
    }
    
    save_to_csv(combined_data, "multiple_pages_contracts.csv")
    print(f"Total records fetched: {len(all_results)}")


def example_5_specific_recipient():
    """Search for awards to a specific recipient (by ID)."""
    print("\n" + "="*60)
    print("Example 5: Awards to a Specific Recipient")
    print("="*60)
    
    # Note: You would need to know the recipient ID first
    # This is just an example showing the structure
    filters = {
        "recipient_search_text": ["university"],  # Search by name
        "award_type_codes": ["02", "03", "04", "05"],  # Grants
        "time_period": [
            {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }
        ]
    }
    
    data = fetch_spending_data(filters=filters, limit=25)
    if data:
        save_to_csv(data, "university_grants.csv")
        print(f"Found {data.get('page_metadata', {}).get('total', 0):,} total records")


def example_6_custom_fields():
    """Fetch data with specific fields only."""
    print("\n" + "="*60)
    print("Example 6: Custom Fields Selection")
    print("="*60)
    
    # Specify exactly which fields you want
    custom_fields = [
        "Award ID",
        "Recipient Name",
        "Award Amount",
        "Awarding Agency",
        "Description"
    ]
    
    filters = {
        "award_amounts": [
            {
                "lower_bound": 10000000.00  # $10 million minimum
            }
        ],
        "time_period": [
            {
                "start_date": "2024-01-01",
                "end_date": "2024-12-31"
            }
        ]
    }
    
    data = fetch_spending_data(filters=filters, fields=custom_fields, limit=20)
    if data:
        save_to_csv(data, "custom_fields_awards.csv")
        print(f"Found {data.get('page_metadata', {}).get('total', 0):,} total records")


def main():
    """Run all examples."""
    print("="*60)
    print("USAspending API - Example Use Cases")
    print("="*60)
    print("\nThis script demonstrates various ways to use the API.")
    print("Uncomment the examples you want to run in the main() function.")
    print()
    
    # Uncomment the examples you want to run:
    
    example_1_recent_large_contracts()
    # example_2_grants_by_year()
    # example_3_specific_agency()
    # example_4_fetch_multiple_pages()
    # example_5_specific_recipient()
    # example_6_custom_fields()
    
    print("\n" + "="*60)
    print("Examples complete! Check the generated CSV files.")
    print("="*60)


if __name__ == "__main__":
    main()

