import pandas as pd
import os
from datetime import timedelta

def load_sleep_data(filepath):
    """Load and clean sleep events from the log."""
    df = pd.read_excel(filepath)
    df.columns = [col.strip() for col in df.columns]

    # Filter for sleep events
    df = df[df['EventType'].astype(str).str.lower() == 'sleep'].copy()

    # Convert to datetime
    df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
    df['EndTime'] = pd.to_datetime(df['EndTime'], errors='coerce')

    # Drop invalid rows
    df = df.dropna(subset=['StartTime', 'EndTime'])

    # Fix overnights
    df.loc[df['EndTime'] < df['StartTime'], 'EndTime'] += pd.Timedelta(days=1)

    return df[['StartTime', 'EndTime']]

def expand_sleep_to_days(df):
    """Break sleep sessions into daily contributions."""
    results = []

    for _, row in df.iterrows():
        start = row['StartTime']
        end = row['EndTime']
        current = start

        while current.date() <= end.date():
            day_start = max(current, pd.Timestamp(current.date()))
            day_end = min(end, pd.Timestamp(current.date() + timedelta(days=1)))
            duration = (day_end - day_start).total_seconds() / 3600
            results.append({'Date': current.date(), 'SleepHours': duration})
            current = pd.Timestamp(current.date() + timedelta(days=1))

    return pd.DataFrame(results)

def summarize_sleep(sleep_df):
    """Group by date and sum sleep hours."""
    summary = sleep_df.groupby('Date')['SleepHours'].sum().reset_index()
    summary = summary.sort_values('Date')
    return summary

def main(filepath):
    sleep_df = load_sleep_data(filepath)
    expanded = expand_sleep_to_days(sleep_df)
    summary = summarize_sleep(expanded)

    print("\n🛏️ Sleep Summary (hours per date):")
    print(summary)

    # Save output
    out_name = os.path.basename(filepath).replace(".xlsx", "_sleep_report.csv")
    out_path = os.path.join(os.path.dirname(filepath), out_name)
    summary.to_csv(out_path, index=False)

    print(f"\n✅ Saved summary to: {out_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_sleep_summary.py path/to/baby_daybook_log.xlsx")
    else:
        main(sys.argv[1])
