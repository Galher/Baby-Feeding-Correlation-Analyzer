import pandas as pd
import matplotlib.pyplot as plt
import os

def load_csv(path, date_col='Date'):
    df = pd.read_csv(path)
    df[date_col] = pd.to_datetime(df[date_col])  # Uses default ISO format YYYY-MM-DD
    return df

def plot_bottle_per_kg(bottle_csv, weight_csv):
    bottle_df = load_csv(bottle_csv)
    weight_df = load_csv(weight_csv)

    # Merge on Date
    merged = pd.merge(bottle_df, weight_df, on='Date', how='inner')

    # Normalize
    merged['BottlePerKg'] = merged['Total Volume (ml)'] / merged['Estimated Weight']

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(merged['Date'], merged['BottlePerKg'], marker='o', linestyle='-', color='teal')
    plt.title("📈 Bottle Volume per Body Weight (ml/kg)")
    plt.xlabel("Date")
    plt.ylabel("Bottle Volume (ml) per kg")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)

    # Save the plot
    output_path = os.path.join("data", "bottle_per_kg_plot.png")
    plt.savefig(output_path)
    plt.show()

    print(f"\n✅ Plot saved to: {output_path}")

def main():
    bottle_csv = "data/baby_daybook_log_bottle_report.csv"
    weight_csv = "data/baby_weight_report.csv"
    plot_bottle_per_kg(bottle_csv, weight_csv)

if __name__ == "__main__":
    main()
