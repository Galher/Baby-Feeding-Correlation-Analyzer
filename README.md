# 🍼 Baby Feeding Correlation Analyzer

📘 **Project Overview:**


Many new parents in Israel use tracking apps such as Baby Daybook to monitor their baby’s routine — including feeding, sleep, diapers, and weight. While these apps provide basic visualizations, they don’t offer deeper analysis tools for parents facing feeding difficulties or suspected eating disorders in their babies.

This project aims to help those parents by offering a tool that analyzes the exported data from the app and looks for correlations between feeding behavior and other daily factors — such as sleep, diaper activity, or weight trends. It’s designed to support better decision-making and communication with health professionals.
<br>
<br>

👶 **What This Project Does:**


This tool receives structured data exported from the Baby Daybook app (in Excel format), and returns summarized metrics and correlations focused on feeding problems.

Specifically, it will:

- Calculate daily feeding volume per body weight (ml/kg) — a standard metric used in pediatric nutrition (e.g., 120–150 ml/kg/day).

  *Disclaimer- since babies are not weighed daily, we’ll estimate weight between two known weights by assuming a linear gain. This is a simplification, as weight gain in       babies is not always linear — and this will be clearly stated.

- Check the correlation between sleep and feeding volume, to see if tiredness or poor sleep is linked to appetite or feeding behavior.

- Analyze the time gaps between feedings vs. volume, to examine whether babies tend to eat more after longer breaks.

- Check daily number of feedings vs. total volume, to see if increased frequency results in more or less food intake.

- Investigate the relationship between dirty diapers and feeding volume, to explore whether signs of digestive discomfort are related to lower intake (possibly indicating an   underlying issue).

These insights can help parents spot possible causes or patterns related to their baby’s eating difficulties.  
<br>
<br>


📥 **Input and 📤 Output
Input:**

An Excel file exported from the Baby Daybook app, which includes logs of:

- Feeding volumes and times

- Sleep times/durations

- Diaper changes (wet/dirty)

- Weight entries

(Optional: medications, food type)

Output:

- A summary of daily feeding per body weight

- Key correlation insights between feeding and other parameters (e.g., sleep, diapers)

<br>
<br>



⚙️ **Technical Details:**  


The script will take the exported Excel file and process it.

Calculations and correlations will be presented in simple summary form.

The tool will be designed to remain flexible — implementation choices (e.g., libraries or interfaces) will be finalized during development.  
<br>
<br>

🏃‍♂️ **How to Run:**  


1. Export the Excel file from the Baby Daybook app.

2. Place the file (e.g., baby_data.xlsx) in the project folder.

3. Run the main script to receive analysis results.  
<br>
<br>



✅ **Testing:**
Basic tests will be included to ensure the data is parsed correctly and calculations are robust, even with missing or inconsistent data.
<br>
<br>
** This proposal was written as part of a python course- https://github.com/code-Maven/wis-python-course-2025-03?tab=readme-ov-file
