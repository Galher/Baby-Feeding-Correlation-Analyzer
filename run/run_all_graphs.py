import os

def run_all_graphs():
    print("📈 Generating all plots...")

    os.system("python scripts/plot_sleep_vs_bottle.py")
    os.system("python scripts/plot_bottle_vs_diaper.py")
    os.system("python scripts/plot_bottle_per_kg.py")

    print("\n✅ All plots generated!")

if __name__ == "__main__":
    run_all_graphs()
