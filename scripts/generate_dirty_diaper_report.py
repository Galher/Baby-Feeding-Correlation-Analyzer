import pandas as pd
import os

def load_dirty_diaper_data(filepath):
    """Load and filter dirty diaper events."""
    df = pd.read_excel(filepath)
    df.columns = [col.strip() for col in df.columns]

    # Normalize types and values
    df['EventType'] = df['EventType'].astype(str).str.lower()
    df['Dirty'] = df['Dirty'].astype(str).str.strip().str.upper()

    # Convert EventDate to datetime (just the date part)
    df['EventDate'] = pd.to_datetime(df['EventDate'], errors='coerce').dt.date

    # Filter for dirty diaper rows
    dirty_df = df[(df['EventType'] == 'diaper') & (df['Dirty'] == 'YES')]

    return dirty_df[['EventDate']]

def summarize_dirty_diapers(dirty_df):
    """Count dirty diapers per date."""
    summary = dirty_df.groupby('EventDate').size().reset_index(name='Dirty Diaper Count')
    summary = summary.sort_values('EventDate')
    return summary

def main(filepath):
    dirty_df = load_dirty_diaper_data(filepath)
    summary = summarize_dirty_diapers(dirty_df)

    print("\n💩 Dirty Diaper Summary:")
    print(summary)

    # Save to CSV
    basename = os.path.basename(filepath).replace(".xlsx", "_dirty_diaper_report.csv")
    output_path = os.path.join(os.path.dirname(filepath), basename)
    summary.to_csv(output_path, index=False)

    print(f"\n✅ Report saved to: {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_dirty_diaper_report.py path/to/baby_daybook_log.xlsx")
    else:
        main(sys.argv[1])
