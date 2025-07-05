import pandas as pd
import os

def load_bottle_data(filepath):
    """Load bottle feeding events and clean data."""
    df = pd.read_excel(filepath)
    df.columns = [col.strip() for col in df.columns]

    # Filter for bottle events
    df = df[df['EventType'].astype(str).str.lower() == 'bottle'].copy()

    # Convert EventDate to datetime (only the date part)
    df['EventDate'] = pd.to_datetime(df['EventDate'], errors='coerce').dt.date

    # Ensure Volume is numeric
    df['Volume(ml)'] = pd.to_numeric(df['Volume(ml)'], errors='coerce')

    return df[['EventDate', 'Volume(ml)']].dropna()

def summarize_bottles(df):
    """Group by date and sum volume."""
    summary = df.groupby('EventDate')['Volume(ml)'].sum().reset_index()
    summary = summary.sort_values('EventDate')
    summary.rename(columns={'EventDate': 'Date', 'Volume(ml)': 'Total Volume (ml)'}, inplace=True)
    return summary

def main(filepath):
    bottle_df = load_bottle_data(filepath)
    summary = summarize_bottles(bottle_df)

    print("\n🍼 Bottle Feeding Summary:")
    print(summary)

    # Save the output
    out_name = os.path.basename(filepath).replace(".xlsx", "_bottle_report.csv")
    out_path = os.path.join(os.path.dirname(filepath), out_name)
    summary.to_csv(out_path, index=False)

    print(f"\n✅ Saved report to: {out_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_bottle_report.py path/to/baby_daybook_log.xlsx")
    else:
        main(sys.argv[1])
