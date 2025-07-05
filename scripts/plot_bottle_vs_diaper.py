import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(file_path, date_col):
    df = pd.read_csv(file_path)
    df[date_col] = pd.to_datetime(df[date_col], dayfirst=True)
    return df

def normalize_series(series):
    return (series - series.min()) / (series.max() - series.min())

def plot_bottle_vs_diapers(bottle_csv, diaper_csv):
    bottle_df = load_csv(bottle_csv, 'Date')
    diaper_df = load_csv(diaper_csv, 'EventDate')

    merged = pd.merge(bottle_df, diaper_df, left_on='Date', right_on='EventDate', how='inner')

    # Normalize both series
    merged['Normalized Bottle'] = normalize_series(merged['Total Volume (ml)'])
    merged['Normalized Diapers'] = normalize_series(merged['Dirty Diaper Count'])

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(merged['Date'], merged['Normalized Bottle'], marker='o', label='Bottle Volume (normalized)')
    plt.plot(merged['Date'], merged['Normalized Diapers'], marker='s', label='Dirty Diaper Count (normalized)')
    
    plt.xlabel("Date")
    plt.ylabel("Normalized Value")
    plt.title("Normalized Bottle Volume vs. Dirty Diaper Count per Day")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    output_path = os.path.join("data", "bottle_vs_diaper_normalized_plot.png")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()

    print(f"\n✅ Saved plot to: {output_path}")

def main():
    bottle_csv = "data/baby_daybook_log_bottle_report.csv"
    diaper_csv = "data/baby_daybook_log_dirty_diaper_report.csv"
    plot_bottle_vs_diapers(bottle_csv, diaper_csv)

if __name__ == "__main__":
    main()
