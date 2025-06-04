import os
import pandas as pd

# Get current directory (where the script and Excel files are)
folder_path = os.path.dirname(os.path.abspath(__file__))

# Output filenames
combined_sheets_file = os.path.join(folder_path, 'Combined_Sheets.xlsx')
appended_data_file = os.path.join(folder_path, 'Appended_Data.xlsx')

# Initialize ExcelWriter for separate sheets
combined_writer = pd.ExcelWriter(combined_sheets_file, engine='openpyxl')

# List to hold all data for the appended file
all_data = []

# Process each Excel file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') and filename not in ['Combined_Sheets.xlsx', 'Appended_Data.xlsx']:
        file_path = os.path.join(folder_path, filename)
        try:
            df = pd.read_excel(file_path)

            # Write to separate sheet
            sheet_name = os.path.splitext(filename)[0][:31]  # Sheet name max length = 31
            df.to_excel(combined_writer, sheet_name=sheet_name, index=False)

            # Add filename column and collect for appending
            df['Source_File'] = filename
            all_data.append(df)

        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Save the combined sheets file
combined_writer.close()

# Save the appended data to one file
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_excel(appended_data_file, index=False)

print("Processing complete.")
