import pandas as pd
import os
import json

def json_to_csv(json_file_path, csv_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Convert JSON data to a DataFrame
    df = pd.DataFrame(data)
    
    # Save DataFrame to CSV
    df.to_csv(csv_file_path, index=False)

def main():
    # Define file paths

    # parent_folder is the path to the parent folder where the json file is located
    parent_folder = os.path.expanduser('path/to/parent/')
    # json_file_path is the name of the json file in the parent folder
    json_file_path = os.path.join(parent_folder, 'json_file_name.json')
    # csv_file_path is the name of the csv file you want to save in the parent folder
    csv_file_path = os.path.join(parent_folder, 'csv_file_name.csv')
    
    # Convert JSON to CSV
    json_to_csv(json_file_path, csv_file_path)
    print(f"CSV file has been saved to {csv_file_path}")

if __name__ == '__main__':
    main()
