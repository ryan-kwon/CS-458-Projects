import csv

input_file = 'Electric_Vehicle_Population_Data_Nodes.csv'
output_file = 'output.csv'

def assign_ids(rows, column_index):
    id_map = {}
    id_counter = 1

    for row in rows:
        key = row[column_index]
        if key not in id_map:
            id_map[key] = id_counter
            id_counter += 1
        row.append(id_map[key])
    
    return rows, id_map

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    headers = next(reader)
    headers.extend(['City_ID', 'Make_ID', 'Electric_Vehicle_Type_ID'])
    writer.writerow(headers)

    rows = list(reader)
    
    # Assign City_IDs
    city_column_index = headers.index('City')
    rows, city_id_map = assign_ids(rows, city_column_index)

    # Assign Make_IDs
    make_column_index = headers.index('Make')
    rows, make_id_map = assign_ids(rows, make_column_index)

    # Assign Electric_Vehicle_Type_IDs
    ev_type_column_index = headers.index('Electric Vehicle Type')
    rows, ev_type_id_map = assign_ids(rows, ev_type_column_index)

    for row in rows:
        writer.writerow(row)

print(f"Processed data with City_IDs, Make_IDs, and Electric_Vehicle_Type_IDs has been written to {output_file}")