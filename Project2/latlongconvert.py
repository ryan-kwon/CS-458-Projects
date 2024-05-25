import csv

input_file = 'input.csv'
output_file = 'output.csv'
column_to_clean = 0  # index of the column to clean, starting from 0

def clean_column_value(value):
    if ' ' in value:
        parts = value.split(' ')
        if len(parts) > 1:
            cleaned_value = parts[1].replace(')', '')  # Remove the closing parenthesis
            return cleaned_value
    return ''  # Return an empty string if the format is unexpected

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        if row:  # Check if the row is not empty
            row[column_to_clean] = clean_column_value(row[column_to_clean])
        writer.writerow(row)

print(f"Processed data has been written to {output_file}")
