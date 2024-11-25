from PIL import Image
import pytesseract
import pandas as pd
import re

# Path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read the image using PIL
print("Enter your input filename:")
inpFile = "D:/Aditya/College files/Year4Sem1/AD/AD-1/"+input()
image = Image.open(inpFile)

# Perform OCR using pytesseract
text_data = pytesseract.image_to_string(image)

# Split the text data into rows and columns
rows = text_data.strip().split('\n')

# Detect and use the best separator (tab, comma, etc.) for columns
separator = None
for row in rows:
    if '\t' in row:
        separator = '\t'
        break
    elif ',' in row:
        separator = ','
        break

if separator:
    table_data = [re.split(f'{separator}+', row.strip()) for row in rows]
else:
    # Use a default split (assuming space) if no separator is found
    table_data = [row.split() for row in rows]

# Remove empty rows and columns
table_data = [row for row in table_data if any(cell.strip() for cell in row)]
table_data = [list(filter(None, row)) for row in table_data]

# Create a DataFrame
df = pd.DataFrame(table_data)
name = input("please enter the output filename: ")
filename = name+".csv"
# Change the output file path to a directory where you have write permissions
output_path = 'D:/Aditya/College files/Year4Sem1/AD/AD-1/'+filename
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Display the entire DataFrame
# print(df)
# Save the DataFrame to a CSV file
df.to_csv(output_path, index=False, header=False)  # Avoid writing headers if not needed
