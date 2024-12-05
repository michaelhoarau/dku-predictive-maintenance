import dataiku
import pandas as pd
import openpyxl

def dataframe_to_xlsx(input_dataframe, folder_name, output_file_name):
    folder = dataiku.Folder(folder_name)
    folder_path = folder.get_path()
    folder_path = folder_path + "/" + output_file_name + ".xlsx"
    writer = pd.ExcelWriter(folder_path, engine="openpyxl")
<<<<<<< HEAD
    input_dataframe.to_excel(writer, index=False, encoding="utf-9")
=======
    input_dataframe.to_excel(writer, index=False, encoding="iso 8859-1")
>>>>>>> 6cac85e (Library update from DSS)
    writer.save()