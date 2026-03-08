import os

from Utilities import excel_operations as EXCEL

# Added a comment to explain the purpose of this function
# This function reads test data from an Excel sheet and returns it as a list of lists.

def get_data(sheet_name):
    cwd = os.getcwd()
    if cwd.endswith("PageObjectModelFramework"):
        read_file_path = 'Excel\\testdata.xlsx'
    else:
        read_file_path = "..\\Excel\\testdata.xlsx"
    row_count = EXCEL.get_row_count(read_file_path, sheet_name)
    column_count = EXCEL.get_column_count(read_file_path, sheet_name)
    user_list = []

    for row in range(2, row_count+1):
        user = []
        for column in range(1, column_count+1):
            user.append(EXCEL.get_cell_value(read_file_path, sheet_name, row, column))
        user_list.append(user)

    return user_list