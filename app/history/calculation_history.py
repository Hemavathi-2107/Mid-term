import pandas as pd
import os

HISTORY_FILE = "data/calculation_history.csv"

def save_history(expression, result):
    """Save the expression and result to history."""
    
    # Format result: truncate or round to 6 decimal places, then remove trailing zeros
    if isinstance(result, float):
        result_str = f"{result:.6f}".rstrip('0').rstrip('.')  # Removes unnecessary zeros
    else:
        result_str = str(result)  # In case it's already an integer or a string
    
    # Load the existing history, or create an empty dataframe if it doesn't exist
    df = load_history()
    
    # Append new record to the history
    new_entry = pd.DataFrame([{"Expression": expression, "Result": result_str}])
    df = pd.concat([df, new_entry], ignore_index=True)
    
    # Save the updated history to the CSV
    df.to_csv(HISTORY_FILE, index=False)
    print(f"Calculation '{expression} = {result_str}' saved!")

def load_history():
    """Load calculation history from a CSV file."""
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    else:
        return pd.DataFrame(columns=["Expression", "Result"])

def display_history():
    """Display the saved calculation history."""
    df = load_history()
    if df.empty:
        print("No history found.")
    else:
        print("\nHistory of calculations:")
        print(df.to_string(index=False))

def clear_history():
    """Clear the saved calculation history."""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print("Calculation history cleared.")
    else:
        print("No history to clear.")

def delete_record(index):
    """Delete a specific record by index."""
    df = load_history()
    if not df.empty and 0 <= index < len(df):
        df = df.drop(index).reset_index(drop=True)
        df.to_csv(HISTORY_FILE, index=False)
        print(f"Deleted record at index {index}.")
    else:
        print("Invalid index or empty history.")
