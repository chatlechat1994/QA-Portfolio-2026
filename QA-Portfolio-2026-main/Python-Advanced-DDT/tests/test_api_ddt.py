import pytest
import pandas as pd
import os

# This finds the "data" folder regardless of where you run the command
def load_test_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_path, 'data', 'test_data.csv')
    return pd.read_csv(csv_path).to_dict(orient='records')

class TestUserAPI:
    @pytest.mark.parametrize("user", load_test_data())
    def test_user_processing(self, user):
        assert user['id'] > 0
        assert "@" in user['email']
        assert user['status'] == "active"