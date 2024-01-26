import pandas as pd
#pip install pandas
#pip install openpyxl

def xlsx_to_csv(input_path, output_path):
    # Read the Excel file
    df = pd.read_excel(input_path)

    # Save DataFrame to CSV file
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_excel_file = "Result_2023-Z25501-Eerste_examenkans.xlsx"
    output_csv_file = "Bestand.csv"

    xlsx_to_csv(input_excel_file, output_csv_file)
