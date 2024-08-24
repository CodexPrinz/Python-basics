import pandas as pd
import calendar
from datetime import datetime

# Create a DataFrame to store the dates
df = pd.DataFrame(columns=["Month", "Day"])

# Get the current year
current_year = datetime.now().year

# Create a list of months
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Use a list to store rows before creating the DataFrame
rows = []

# Iterate over each month
for month_idx, month in enumerate(months, start=1):
    # Get the number of days in the month
    num_days = calendar.monthrange(current_year, month_idx)[1]
    
    # Add each day to the list
    for day in range(1, num_days + 1):
        rows.append({"Month": month, "Day": day})

# Create the DataFrame from the list of rows
df = pd.DataFrame(rows)

# Save the DataFrame to an Excel file
df.to_excel("months_and_days.xlsx", index=False)

# Print a success message
print("Excel file 'months_and_days.xlsx' created successfully.")