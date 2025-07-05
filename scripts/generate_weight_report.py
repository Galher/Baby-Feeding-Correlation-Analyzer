import pandas as pd
import numpy as np
import os

def load_weight_data(filepath):
    df = pd.read_excel(filepath)
    df.columns = [col.strip() for col in df.columns]
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df = df.sort_values('Date').reset_index(drop=True)
    return df

def interpolate_weights(df):
    interpolated = []

    for i in range(len(df) - 1):
        row_start = df.iloc[i]
        row_end = df.iloc[i + 1]

        start_date = row_start['Date']
        end_date = row_end['Date']
        start_weight = row_start['Weight']
        end_weight = row_end['Weight']

        num_days = (end_date - start_date).days
        for d in range(num_days + 1):
            date = start_date + pd.Timedelta(days=d)
            weight = start_weight + (end_weight - start_weight) * d / num_days
            interpolated.append({'Date': date, 'Estimated Weight': round(weight, 3)})

    return pd.DataFrame(interpolated)

def main(filepath):
    df = load_weight_data(filepath)
    interpolated_df = interpolate_weights(df)

    output_path = os.path.join("data", "baby_weight_report.csv")
    interpolated_df.to_csv(output_path, index=False)

    print("\n🍼 Estimated Daily Baby Weight Report:")
    print(interpolated_df.head())
    print(f"\n✅ Report saved to: {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python scripts/generate_weight_report.py data/baby_weight.xlsx")
    else:
        main(sys.argv[1])
