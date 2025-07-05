import pandas as pd
import matplotlib.pyplot as plt
import os

def load_report(file_path, date_col, value_col):
    df = pd.read_csv(file_path)
    df[date_col] = pd.to_datetime(df[date_col])
    return df[[date_col, value_col]]

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

def plot_sleep_vs_bottle(sleep_csv, bottle_csv):
    sleep_df = load_report(sleep_csv, 'Date', 'SleepHours')
    bottle_df = load_report(bottle_csv, 'Date', 'Total Volume (ml)')

    # Merge on Date
    merged = pd.merge(sleep_df, bottle_df, on='Date', how='inner')

    # Normalize both series
    merged['Normalized Sleep'] = normalize(merged['SleepHours'])
    merged['Normalized Bottle Volume'] = normalize(merged['Total Volume (ml)'])

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(merged['Date'], merged['Normalized Sleep'], marker='o', label='Normalized Sleep Hours')
    plt.plot(merged['Date'], merged['Normalized Bottle Volume'], marker='o', label='Normalized Bottle Volume')

    plt.title("Normalized Sleep Hours vs Bottle Volume")
    plt.xlabel("Date")
    plt.ylabel("Normalized Value (0–1)")
    plt.legend()
    plt.grid(True)

    # Save to data folder
    output_path = os.path.join("data", "sleep_vs_bottle_normalized.png")
    plt.savefig(output_path)
    print(f"\n✅ Normalized plot saved to: {output_path}")
    plt.close()

def main():
    sleep_csv = "data/baby_daybook_log_sleep_report.csv"
    bottle_csv = "data/baby_daybook_log_bottle_report.csv"
    plot_sleep_vs_bottle(sleep_csv, bottle_csv)

if __name__ == "__main__":
    main()
