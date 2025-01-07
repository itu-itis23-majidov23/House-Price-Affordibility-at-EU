import pandas as pd

# Step 1: Load the dataset
file_path = 'unemployment_rate.xlsx'  # Replace with your actual file name
df = pd.read_excel(file_path)  # Assuming the uploaded file is saved as an Excel file

# Step 2: Reshape the data
# Rename the first column to 'Country'
df.rename(columns={df.columns[0]: 'Country'}, inplace=True)

# Use pd.melt to reshape the DataFrame
df_long = pd.melt(df, id_vars=['Country'], var_name='Year', value_name='Value')

# Step 3: Clean the reshaped data
# Convert 'Year' to integers if necessary
df_long['Year'] = df_long['Year'].astype(int)

# Remove rows where 'Value' is NaN or non-numeric
df_long['Value'] = pd.to_numeric(df_long['Value'], errors='coerce')
df_long = df_long.dropna()

# Step 4: Save the cleaned data to a CSV file
output_file = 'unemployment_rate.csv'
df_long.to_csv(output_file, index=False)

print(f"Data reshaped and saved to {output_file}")
