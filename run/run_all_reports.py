import os

def run_all_reports():
    print("▶️ Generating all reports...")

    os.system("python scripts/generate_sleep_report.py data/baby_daybook_log.xlsx")
    os.system("python scripts/generate_bottle_report.py data/baby_daybook_log.xlsx")
    os.system("python scripts/generate_dirty_diaper_report.py data/baby_daybook_log.xlsx")
    os.system("python scripts/generate_weight_report.py data/baby_weight.xlsx")

    print("\n✅ All reports generated!")

if __name__ == "__main__":
    run_all_reports()
