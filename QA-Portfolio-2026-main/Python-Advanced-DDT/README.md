# Python Advanced Data-Driven Testing (DDT)

This project demonstrates an advanced API testing framework using **Pytest** and **Pandas**. 

### Key Features:
- **Dynamic Data Generation:** Uses `Faker` to create 50 unique test records in CSV format.
- **Scalability:** The test suite automatically scales based on the number of rows in the data engine.
- **Professional Reporting:** Generates a self-contained HTML report for audit trails.

### How to Run:
1. Generate data: `python generate_mock_data.py`
2. Run tests: `python -m pytest tests/test_api_ddt.py --html=report.html`