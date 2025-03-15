'''test file to check calculation history'''
import os
import pytest
from app.history.calculation_history import save_history, load_history, display_history, clear_history, delete_record

HISTORY_FILE = "data/calculation_history.csv"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Setup and teardown for each test to ensure a clean history file."""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)  # Clean up before each test
    yield
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)  # Clean up after each test

class TestCalculationHistory:
    '''test class'''
    def test_save_history(self):
        """Test saving a history entry."""
        save_history("5 + 3", 8)
        # Load the history from the CSV file
        df = load_history()
        # Assert the history has been saved correctly
        assert not df.empty
        assert df.iloc[-1]["Expression"] == "5 + 3"
        assert str(df.iloc[-1]["Result"]) == "8"  # Compare as string

    def test_load_history_existing(self):
        """Test loading existing history."""
        save_history("7 * 2", 14)
        # Load the history and check its contents
        df = load_history()
        assert not df.empty
        assert df.iloc[-1]["Expression"] == "7 * 2"
        assert str(df.iloc[-1]["Result"]) == "14"  # Compare as string

    def test_load_history_empty(self):
        """Test loading history when the history is empty."""
        df = load_history()
        assert df.empty
        assert df.shape[0] == 0

    def test_display_history(self, monkeypatch):
        """Test the display_history function."""
        save_history("9 / 3", 3)
        # Capture printed output using monkeypatching
        captured_output = []
        monkeypatch.setattr("builtins.print",  captured_output.append)
        # Call display_history and ensure it prints the correct content
        display_history()
        # Check if the relevant content is in the output
        output = "\n".join(captured_output)  # Join the captured output list into a single string
        assert "Expression" in output
        assert "Result" in output
        assert "9 / 3" in output
        assert "3" in output

    def test_clear_history(self):
        """Test clearing history."""
        save_history("5 + 3", 8)
        clear_history()
        df = load_history()
        assert df.empty

    def test_delete_record(self):
        """Test deleting a specific record."""
        save_history("8 + 2", 10)
        df = load_history()
        # Check that the history has one entry
        assert len(df) == 1
        # Delete the first record
        delete_record(0)
        # Ensure the history is empty after deletion
        df_after = load_history()
        assert df_after.empty

    def test_delete_record_invalid_index(self):
        """Test attempting to delete a record with an invalid index."""
        save_history("8 + 2", 10)
        df = load_history()
        # Try to delete an invalid index (index 5 is out of bounds)
        delete_record(5)
        # Ensure the history wasn't modified
        df_after = load_history()
        # Check if the history length is the same
        assert len(df_after) == len(df)
        # Ensure the first record is still the same (after deletion attempt)
        assert str(df_after.iloc[0]["Expression"]) == "8 + 2"
    def test_save_multiple_entries(self):
        """Test saving multiple history entries."""
        save_history("2 + 2", 4)
        save_history("3 + 3", 6)
        df = load_history()
        # Ensure both entries are saved
        assert len(df) == 2
        assert str(df.iloc[0]["Expression"]) == "2 + 2"
        assert str(df.iloc[1]["Expression"]) == "3 + 3"
        assert str(df.iloc[0]["Result"]) == "4"
        assert str(df.iloc[1]["Result"]) == "6"

    def test_clear_history_no_history(self):
        """Test clearing history when there is no history."""
        clear_history()
        df = load_history()
        assert df.empty
