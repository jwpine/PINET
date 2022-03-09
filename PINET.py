import pandas as pd
import requests
import tkinter as tk
import webbrowser
import os.path
from tkinter import filedialog
from configparser import ConfigParser

# to build version use pyinstaller PINET.py -w --icon=pinetree.ico -n PINET  be sure to copy the icon to the directory before
# zipping and posting
# version
version = 'v2.0'

# Config Section
config_exists = os.path.exists('config.ini')
if config_exists:
    print('found config file')
else:
    config_file = ConfigParser()
    config_file["DEFAULT"] = {"api_key": "Enter API Key Here"}
    config_file["HSCODES"] = {"commodity_hs_1": "10-digit, no period", "commodity_hs_2": "10-digit, no period",
                              "commodity_hs_3": "10-digit, no period", "commodity_hs_4": "10-digit, no period",
                              "commodity_hs_5": "10-digit, no period", "commodity_hs_6": "10-digit, no period",
                              "commodity_hs_7": "10-digit, no period", "commodity_hs_8": "10-digit, no period",
                              "commodity_hs_9": "10-digit, no period", "commodity_hs_10": "10-digit, no period",
                              "commodity_hs_11": "10-digit, no period", "commodity_hs_12": "10-digit, no period",
                              "commodity_hs_13": "10-digit, no period", "commodity_hs_14": "10-digit, no period",
                              "commodity_hs_15": "10-digit, no period", "commodity_hs_16": "10-digit, no period",
                              "commodity_hs_17": "10-digit, no period", "commodity_hs_18": "10-digit, no period",
                              "commodity_hs_19": "10-digit, no period", "commodity_hs_20": "10-digit, no period"}
    config_file["HSNAMES"] = {"commodity_name_1": "enter custom label", "commodity_name_2": "enter custom label",
                              "commodity_name_3": "enter custom label", "commodity_name_4": "enter custom label",
                              "commodity_name_5": "enter custom label", "commodity_name_6": "enter custom label",
                              "commodity_name_7": "enter custom label", "commodity_name_8": "enter custom label",
                              "commodity_name_9": "enter custom label", "commodity_name_10": "enter custom label",
                              "commodity_name_11": "enter custom label", "commodity_name_12": "enter custom label",
                              "commodity_name_13": "enter custom label", "commodity_name_14": "enter custom label",
                              "commodity_name_15": "enter custom label", "commodity_name_16": "enter custom label",
                              "commodity_name_17": "enter custom label", "commodity_name_18": "enter custom label",
                              "commodity_name_19": "enter custom label", "commodity_name_20": "enter custom label"}
    with open('config.ini', "w") as file_object:
        config_file.write(file_object)
        file_object.close()

config = ConfigParser()
config.read('config.ini')
api_key = config['DEFAULT'].get('api_key')
custom1_hs = config['HSCODES'].get('commodity_hs_1')
custom1_name = config['HSNAMES'].get('commodity_name_1')
custom2_hs = config['HSCODES'].get('commodity_hs_2')
custom2_name = config['HSNAMES'].get('commodity_name_2')
custom3_hs = config['HSCODES'].get('commodity_hs_3')
custom3_name = config['HSNAMES'].get('commodity_name_3')
custom4_hs = config['HSCODES'].get('commodity_hs_4')
custom4_name = config['HSNAMES'].get('commodity_name_4')
custom5_hs = config['HSCODES'].get('commodity_hs_5')
custom5_name = config['HSNAMES'].get('commodity_name_5')
custom6_hs = config['HSCODES'].get('commodity_hs_6')
custom6_name = config['HSNAMES'].get('commodity_name_6')
custom7_hs = config['HSCODES'].get('commodity_hs_7')
custom7_name = config['HSNAMES'].get('commodity_name_7')
custom8_hs = config['HSCODES'].get('commodity_hs_8')
custom8_name = config['HSNAMES'].get('commodity_name_8')
custom9_hs = config['HSCODES'].get('commodity_hs_9')
custom9_name = config['HSNAMES'].get('commodity_name_9')
custom10_hs = config['HSCODES'].get('commodity_hs_10')
custom10_name = config['HSNAMES'].get('commodity_name_10')
custom11_hs = config['HSCODES'].get('commodity_hs_11')
custom11_name = config['HSNAMES'].get('commodity_name_11')
custom12_hs = config['HSCODES'].get('commodity_hs_12')
custom12_name = config['HSNAMES'].get('commodity_name_12')
custom13_hs = config['HSCODES'].get('commodity_hs_13')
custom13_name = config['HSNAMES'].get('commodity_name_13')
custom14_hs = config['HSCODES'].get('commodity_hs_14')
custom14_name = config['HSNAMES'].get('commodity_name_14')
custom15_hs = config['HSCODES'].get('commodity_hs_15')
custom15_name = config['HSNAMES'].get('commodity_name_15')
custom16_hs = config['HSCODES'].get('commodity_hs_16')
custom16_name = config['HSNAMES'].get('commodity_name_16')
custom17_hs = config['HSCODES'].get('commodity_hs_17')
custom17_name = config['HSNAMES'].get('commodity_name_17')
custom18_hs = config['HSCODES'].get('commodity_hs_18')
custom18_name = config['HSNAMES'].get('commodity_name_18')
custom19_hs = config['HSCODES'].get('commodity_hs_19')
custom19_name = config['HSNAMES'].get('commodity_name_19')
custom20_hs = config['HSCODES'].get('commodity_hs_20')
custom20_name = config['HSNAMES'].get('commodity_name_20')
print('api key =', api_key)


# Make API Key a clickable link
def callback(event):
    webbrowser.open_new_tab(r"https://api.census.gov/data/key_signup.html")


# Put all window elements in between this statement and the root.mainloop() statement
root = tk.Tk()
root.title("Product Imports 'N Exports Tool")
root.iconbitmap("pinetree.ico")

# Setting up the framework of the window.
canvas = tk.Canvas(root, width=700, height=475)

# Change this to change the number of columns in the window. Makes it easier to set up GUI
canvas.grid(columnspan=10, rowspan=100)
canvas.columnconfigure(0, weight=1)
canvas.columnconfigure(1, weight=3)
canvas.columnconfigure(3, weight=1)
canvas.columnconfigure(4, weight=1)
canvas.columnconfigure(5, weight=1)
canvas.columnconfigure(6, weight=1)
canvas.columnconfigure(7, weight=1)
canvas.columnconfigure(8, weight=1)
canvas.columnconfigure(9, weight=1)


# Status Reset
def reset_status():
    status_txt.set("Status: Waiting for input")


# Query Code
def run_query():
    if direction.get() == "EXPORT":
        # Variable Storage
        status_txt.set('Status: Something went wrong. Check Inputs.')
        custom1 = custom1_entry.get()
        custom2 = custom2_entry.get()
        custom3 = custom3_entry.get()
        custom4 = custom4_entry.get()
        custom5 = custom5_entry.get()
        custom6 = custom6_entry.get()
        custom7 = custom7_entry.get()
        custom8 = custom8_entry.get()
        custom9 = custom9_entry.get()
        custom10 = custom10_entry.get()
        custom11 = custom11_entry.get()
        custom12 = custom12_entry.get()
        custom13 = custom13_entry.get()
        custom14 = custom14_entry.get()
        custom15 = custom15_entry.get()
        custom16 = custom16_entry.get()
        custom17 = custom17_entry.get()
        custom18 = custom18_entry.get()
        custom19 = custom19_entry.get()
        custom20 = custom20_entry.get()
        filtered_list = []
        api_key1 = api_key_entry.get()
        api_key = '&key='+api_key1
        start_date = from_date.get()
        end_date = to_date.get()
        date_range = '&time=from' + start_date + '+to+' + end_date
        base_url = 'https://api.census.gov/data/timeseries/intltrade/exports/hs?get='
        base_columns = 'YEAR,MONTH,E_COMMODITY_LDESC,DIST_NAME,DISTRICT,CTY_NAME,CTY_CODE,QTY_1_MO,QTY_1_MO_FLAG'
        extra_bits = '&DF=1&SUMMARY_LVL=DET'
        save_loc = dir_location.get()
        direction.get()

        # Build the filtered list of commodities
        if custom_check1.get() == 1:
            filtered_list.append(custom1)
        if custom_check2.get() == 1:
            filtered_list.append(custom2)
        if custom_check3.get() == 1:
            filtered_list.append(custom3)
        if custom_check4.get() == 1:
            filtered_list.append(custom4)
        if custom_check5.get() == 1:
            filtered_list.append(custom5)
        if custom_check6.get() == 1:
            filtered_list.append(custom6)
        if custom_check7.get() == 1:
            filtered_list.append(custom7)
        if custom_check8.get() == 1:
            filtered_list.append(custom8)
        if custom_check9.get() == 1:
            filtered_list.append(custom9)
        if custom_check10.get() == 1:
            filtered_list.append(custom10)
        if custom_check11.get() == 1:
            filtered_list.append(custom11)
        if custom_check12.get() == 1:
            filtered_list.append(custom12)
        if custom_check13.get() == 1:
            filtered_list.append(custom13)
        if custom_check14.get() == 1:
            filtered_list.append(custom14)
        if custom_check15.get() == 1:
            filtered_list.append(custom15)
        if custom_check16.get() == 1:
            filtered_list.append(custom16)
        if custom_check17.get() == 1:
            filtered_list.append(custom17)
        if custom_check18.get() == 1:
            filtered_list.append(custom18)
        if custom_check19.get() == 1:
            filtered_list.append(custom19)
        if custom_check20.get() == 1:
            filtered_list.append(custom20)
        # Set starter combined dataframe
        com_df = pd.DataFrame(columns=['YEAR', 'MONTH', 'E_COMMODITY_LDESC', 'DIST_NAME', 'DISTRICT', 'CTY_NAME', 'CTY_CODE', 'QTY_1_MO', 'QTY_1_MO_FLAG', 'E_COMMODITY', 'DF', 'SUMMARY_LVL'])

        # Error Check and Status Update
        print(filtered_list)

        for x in filtered_list:
            hs_code = x
            # Builds HS Code formatting for API call
            hs_code_call = '&E_COMMODITY=' + hs_code
            # Build the URL for the API
            api_call = base_url + base_columns + api_key + hs_code_call + date_range + extra_bits
            # Run the API
            api_results = requests.get(api_call).json()
            # Put the results in a dataframe
            df1 = pd.DataFrame(api_results)
            # Set Column Names
            new_header = df1.iloc[0]
            df2 = df1[1:]
            df2.columns = new_header
            # Filter out the totals rows
            df2 = df2[(df2.DISTRICT != '-') & (df2.CTY_CODE != '-')]
            # Put the results in a combined dataframe
            com_df = com_df.append(df2)

        # Drop columns we dont want in the final product
        com_df = com_df.drop(['DF', 'SUMMARY_LVL'], axis=1)
        # Rearrange Columns
        com_df = com_df[['time', 'YEAR', 'MONTH', 'E_COMMODITY', 'E_COMMODITY_LDESC', 'DIST_NAME', 'DISTRICT', 'CTY_NAME', 'CTY_CODE', 'QTY_1_MO', 'QTY_1_MO_FLAG']]
        # Add a calculated column for Short tons then round since we don't have KGs
        com_df['QTY_1_MO'] = com_df['QTY_1_MO'].astype(int)
        com_df['SHIPMENT_IN_ST'] = com_df.QTY_1_MO * 1.102311
        com_df['SHIPMENT_IN_ST'] = com_df.SHIPMENT_IN_ST.round(1)
        # Rename Columns For Final Product
        com_df.columns = ['DATE', 'YEAR', 'MONTH', 'HS CODE', 'COMMODITY DESCRIPTION', 'US PORT DISTRICT', 'US DIST CODE',
                          'DEST COUNTRY', 'DEST COUNTRY CODE', 'SHIPMENT IN MT', 'VALUE MISSING?', 'SHIPMENT IN ST']

        # Print Dataframe to CSV
        com_df.to_csv(save_loc+'/com_export_data.csv', index=False, header=True)
        status_txt.set('Status: Finished. Go Check File.')

    else:
        # Variable Storage
        status_txt.set('Status: Something went wrong. Check Inputs.')
        custom1 = custom1_entry.get()
        custom2 = custom2_entry.get()
        custom3 = custom3_entry.get()
        custom4 = custom4_entry.get()
        custom5 = custom5_entry.get()
        custom6 = custom6_entry.get()
        custom7 = custom7_entry.get()
        custom8 = custom8_entry.get()
        custom9 = custom9_entry.get()
        custom10 = custom10_entry.get()
        custom11 = custom11_entry.get()
        custom12 = custom12_entry.get()
        custom13 = custom13_entry.get()
        custom14 = custom14_entry.get()
        custom15 = custom15_entry.get()
        custom16 = custom16_entry.get()
        custom17 = custom17_entry.get()
        custom18 = custom18_entry.get()
        custom19 = custom19_entry.get()
        custom20 = custom20_entry.get()
        filtered_list = []
        api_key1 = api_key_entry.get()
        api_key = '&key='+api_key1
        start_date = from_date.get()
        end_date = to_date.get()
        date_range = '&time=from' + start_date + '+to+' + end_date
        base_url = 'https://api.census.gov/data/timeseries/intltrade/imports/hs?get='
        base_columns = 'YEAR,MONTH,I_COMMODITY_LDESC,DIST_NAME,DISTRICT,CTY_NAME,CTY_CODE,GEN_QY1_MO,GEN_QY1_MO_FLAG'
        extra_bits = '&SUMMARY_LVL=DET'
        save_loc = dir_location.get()
        direction.get()

        # Build the filtered list of commodities
        if custom_check1.get() == 1:
            filtered_list.append(custom1)
        if custom_check2.get() == 1:
            filtered_list.append(custom2)
        if custom_check3.get() == 1:
            filtered_list.append(custom3)
        if custom_check4.get() == 1:
            filtered_list.append(custom4)
        if custom_check5.get() == 1:
            filtered_list.append(custom5)
        if custom_check6.get() == 1:
            filtered_list.append(custom6)
        if custom_check7.get() == 1:
            filtered_list.append(custom7)
        if custom_check8.get() == 1:
            filtered_list.append(custom8)
        if custom_check9.get() == 1:
            filtered_list.append(custom9)
        if custom_check10.get() == 1:
            filtered_list.append(custom10)
        if custom_check11.get() == 1:
            filtered_list.append(custom11)
        if custom_check12.get() == 1:
            filtered_list.append(custom12)
        if custom_check13.get() == 1:
            filtered_list.append(custom13)
        if custom_check14.get() == 1:
            filtered_list.append(custom14)
        if custom_check15.get() == 1:
            filtered_list.append(custom15)
        if custom_check16.get() == 1:
            filtered_list.append(custom16)
        if custom_check17.get() == 1:
            filtered_list.append(custom17)
        if custom_check18.get() == 1:
            filtered_list.append(custom18)
        if custom_check19.get() == 1:
            filtered_list.append(custom19)
        if custom_check20.get() == 1:
            filtered_list.append(custom20)
        # Set starter combined dataframe
        com_df = pd.DataFrame(
            columns=['YEAR', 'MONTH', 'I_COMMODITY_LDESC', 'DIST_NAME', 'DISTRICT', 'CTY_NAME', 'CTY_CODE',
                     'GEN_QY1_MO', 'GEN_QY1_MO_FLAG', 'I_COMMODITY', 'SUMMARY_LVL'])

        for x in filtered_list:
            hs_code = x
            # Builds HS Code formatting for API call
            hs_code_call = '&I_COMMODITY=' + hs_code
            # Build the URL for the API
            api_call = base_url + base_columns + api_key + hs_code_call + date_range + extra_bits
            # Run the API
            api_results = requests.get(api_call).json()
            # Put the results in a dataframe
            df1 = pd.DataFrame(api_results)
            # Set Column Names
            new_header = df1.iloc[0]
            df2 = df1[1:]
            df2.columns = new_header
            # Filter out the totals rows
            df2 = df2[(df2.DISTRICT != '-') & (df2.CTY_CODE != '-')]
            # Put the results in a combined dataframe
            com_df = com_df.append(df2)

        # Drop columns we dont want in the final product
        com_df = com_df.drop(['SUMMARY_LVL'], axis=1)
        # Rearrange Columns
        com_df = com_df[['time', 'YEAR', 'MONTH', 'I_COMMODITY', 'I_COMMODITY_LDESC', 'DIST_NAME', 'DISTRICT', 'CTY_NAME', 'CTY_CODE', 'GEN_QY1_MO', 'GEN_QY1_MO_FLAG']]
        # Add a calculated column for Short tons then round since we don't have KGs
        com_df['GEN_QY1_MO'] = com_df['GEN_QY1_MO'].astype(int)
        com_df['SHIPMENT_IN_ST'] = com_df.GEN_QY1_MO * 1.102311
        com_df['SHIPMENT_IN_ST'] = com_df.SHIPMENT_IN_ST.round(1)
        # Rename Columns For Final Product
        com_df.columns = ['DATE', 'YEAR', 'MONTH', 'HS CODE', 'COMMODITY DESCRIPTION', 'US PORT DISTRICT',
                          'US DIST CODE', 'ORIGIN COUNTRY', 'ORIGIN COUNTRY CODE', 'SHIPMENT IN MT', 'VALUE MISSING?',
                          'SHIPMENT IN ST']

        # Print Dataframe to CSV
        com_df.to_csv(save_loc+'/com_import_data.csv', index=False, header=True)
        status_txt.set('Status: Finished. Go Check File.')


#  Welcome Message
welcome = tk.Label(root, text="Product Import 'N Export Tool", font=("bold",16))
welcome.grid(columnspan=10, column=0, row=0, sticky=tk.N, pady=5)
getakey = tk.Label(root, text="Get an API key from here:")
getakey.grid(columnspan=1, column=0, row=1, sticky=tk.NE, pady=5)
link_to_key = tk.Label(root, text="https://api.census.gov/data/key_signup.html", fg="blue", cursor="hand2")
link_to_key.grid(columnspan=1, column=1, row=1, sticky=tk.NW, pady=5)
link_to_key.bind("<Button-1>", callback)


def direction_flag():
    direction.config(text=direction.get())


# Set Import or Export
trade_direction = ["EXPORT", "IMPORT"]

# datatype of menu text
direction = tk.StringVar()

# Initial Setting of Direction
direction.set("EXPORT")

# Create Dropdown
dropdown_lbl = tk.Label(root, text="Trade Direction:")
dropdown_lbl.grid(columnspan=1, column=0, row=2, sticky=tk.E, pady=5)
dropdown = tk.OptionMenu(root, direction, *trade_direction)
dropdown.grid(columnspan=1, column=1, row=2, pady=5, sticky=tk.EW)
dropdown.config(bg="#96be25", anchor=tk.CENTER)

# Set API Key Variable
api_key_lbl = tk.Label(root, text="API Key:")
api_key_lbl.grid(columnspan=1, column=0, row=3, sticky=tk.E)
api_key_entry = tk.StringVar()
api_key_entry = tk.Entry()
api_key_entry.insert(0, str(api_key))
api_key_entry.grid(column=1, row=3, ipadx=65, sticky=tk.W)
api_key_save_btn = tk.Button(root, text="Save Key", bg="#e5e82a", command=lambda: save_api())
api_key_save_btn.grid(columnspan=1, column=2, row=3, sticky=tk.W)


def save_api():
    config_file_save = ConfigParser()
    config_file_save.read('config.ini')
    api_key_save = config_file_save["DEFAULT"]
    api_key_save["api_key"] = api_key_entry.get()
    with open('config.ini', "w") as file_object_save:
        config_file_save.write(file_object_save)
        file_object_save.close()
    print('api key saved')
    status_txt.set("Status: API Key Saved")


# Save Location

# Save Directory Location
def savedirectory():
    save_dir = filedialog.askdirectory()
    dir_location.set(save_dir)


save_location_lbl = tk.Label(root, text="Save Location:")
save_location_lbl.grid(columnspan=1, column=0, row=11, sticky=tk.E)
dir_location = tk.StringVar()
dir_location_entry = tk.Entry(textvariable=dir_location)
dir_location_entry.grid(columnspan=2, column=1, row=11, ipadx=80, sticky=tk.W)
browse_btn = tk.Button(root, text="Browse", bg="#E5e82a", command=lambda: savedirectory())
browse_btn.grid(columnspan=1, column=2, row=11, sticky=tk.W)


# Date Setting
date_header = tk.Label(root, text="SET DATES", font=("Bold", 14), pady=5, padx=10)
date_header.grid(columnspan=1, column=0, row=21, sticky=tk.W)

date_frame1 = tk.Frame(root)
date_frame1.grid(columnspan=8, column=0, row=22, sticky=tk.W)

from_date_lbl = tk.Label(date_frame1, text="From Date:")
from_date_lbl.grid(columnspan=1, column=0, row=22, padx=(40,0), sticky=tk.W)
from_date = tk.Entry(date_frame1, borderwidth=2)
from_date.insert(0, "YYYY-MM")
from_date.grid(columnspan=1, column=1, row=22, sticky=tk.W)

to_date_lbl = tk.Label(date_frame1, text="To Date:")
to_date_lbl.grid(columnspan=1, column=2, row=22, padx=(20,0), sticky=tk.W)
to_date = tk.Entry(date_frame1, borderwidth=2)
to_date.insert(0, "YYYY-MM")
to_date.grid(columnspan=1, column=3, row=22, sticky=tk.W)


# HS Code Variable Initialization
custom_check1 = tk.IntVar()
custom_check2 = tk.IntVar()
custom_check3 = tk.IntVar()
custom_check4 = tk.IntVar()
custom_check5 = tk.IntVar()
custom_check6 = tk.IntVar()
custom_check7 = tk.IntVar()
custom_check8 = tk.IntVar()
custom_check9 = tk.IntVar()
custom_check10 = tk.IntVar()
custom_check11 = tk.IntVar()
custom_check12 = tk.IntVar()
custom_check13 = tk.IntVar()
custom_check14 = tk.IntVar()
custom_check15 = tk.IntVar()
custom_check16 = tk.IntVar()
custom_check17 = tk.IntVar()
custom_check18 = tk.IntVar()
custom_check19 = tk.IntVar()
custom_check20 = tk.IntVar()


# HS Code Save Presets
def save_hs_code():
    config_hs_save = ConfigParser()
    config_hs_save.read('config.ini')
    hs_code_save = config_hs_save["HSCODES"]
    hs_code_save["commodity_hs_1"] = custom1_entry.get()
    hs_code_save["commodity_hs_2"] = custom2_entry.get()
    hs_code_save["commodity_hs_3"] = custom3_entry.get()
    hs_code_save["commodity_hs_4"] = custom4_entry.get()
    hs_code_save["commodity_hs_5"] = custom5_entry.get()
    hs_code_save["commodity_hs_6"] = custom6_entry.get()
    hs_code_save["commodity_hs_7"] = custom7_entry.get()
    hs_code_save["commodity_hs_8"] = custom8_entry.get()
    hs_code_save["commodity_hs_9"] = custom9_entry.get()
    hs_code_save["commodity_hs_10"] = custom10_entry.get()
    hs_code_save["commodity_hs_11"] = custom11_entry.get()
    hs_code_save["commodity_hs_12"] = custom12_entry.get()
    hs_code_save["commodity_hs_13"] = custom13_entry.get()
    hs_code_save["commodity_hs_14"] = custom14_entry.get()
    hs_code_save["commodity_hs_15"] = custom15_entry.get()
    hs_code_save["commodity_hs_16"] = custom16_entry.get()
    hs_code_save["commodity_hs_17"] = custom17_entry.get()
    hs_code_save["commodity_hs_18"] = custom18_entry.get()
    hs_code_save["commodity_hs_19"] = custom19_entry.get()
    hs_code_save["commodity_hs_20"] = custom20_entry.get()
    hs_code_save = config_hs_save["HSNAMES"]
    hs_code_save["commodity_name_1"] = custom1_entry_name.get()
    hs_code_save["commodity_name_2"] = custom2_entry_name.get()
    hs_code_save["commodity_name_3"] = custom3_entry_name.get()
    hs_code_save["commodity_name_4"] = custom4_entry_name.get()
    hs_code_save["commodity_name_5"] = custom5_entry_name.get()
    hs_code_save["commodity_name_6"] = custom6_entry_name.get()
    hs_code_save["commodity_name_7"] = custom7_entry_name.get()
    hs_code_save["commodity_name_8"] = custom8_entry_name.get()
    hs_code_save["commodity_name_9"] = custom9_entry_name.get()
    hs_code_save["commodity_name_10"] = custom10_entry_name.get()
    hs_code_save["commodity_name_11"] = custom11_entry_name.get()
    hs_code_save["commodity_name_12"] = custom12_entry_name.get()
    hs_code_save["commodity_name_13"] = custom13_entry_name.get()
    hs_code_save["commodity_name_14"] = custom14_entry_name.get()
    hs_code_save["commodity_name_15"] = custom15_entry_name.get()
    hs_code_save["commodity_name_16"] = custom16_entry_name.get()
    hs_code_save["commodity_name_17"] = custom17_entry_name.get()
    hs_code_save["commodity_name_18"] = custom18_entry_name.get()
    hs_code_save["commodity_name_19"] = custom19_entry_name.get()
    hs_code_save["commodity_name_20"] = custom20_entry_name.get()
    with open('config.ini','w') as hs_file_save:
        config_hs_save.write(hs_file_save)
        hs_file_save.close()
    print('HS Codes Saved')
    status_txt.set("Status: HS Codes Saved")


# HS Code Grid
hs_header = tk.Label(root, text="HS CODES", font=("Bold", 14), pady=5, padx=10)
hs_header.grid(columnspan=1, column=0, row=31, sticky=tk.W)
hs_helper = tk.Label(root, text="(make sure to checkbox the ones you want to run")
hs_helper.grid(columnspan=1, column=1, row=31, sticky=tk.W)
hs_save_btn = tk.Button(root, text="Save HS Preset", bg="#e5e82a", command=lambda: save_hs_code())
hs_save_btn.grid(columnspan=1, column=2, row=31, sticky=tk.W)

hs_code_frame1 = tk.Frame(root)
hs_code_frame1.grid(columnspan=6, column=0, row=36)

custom1_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check1, onvalue=1, offvalue=0)
custom1_checkbox.grid(columnspan=1, column=0, row=36, sticky=tk.E)
custom1_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom1_entry.insert(0, str(custom1_hs))
custom1_entry.grid(columnspan=1, column=1, row=36, sticky=tk.W)
custom1_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom1_entry_name.insert(0, str(custom1_name))
custom1_entry_name.grid(columnspan=1, column=2, row=36, sticky=tk.W)

custom2_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check2, onvalue=1, offvalue=0)
custom2_checkbox.grid(columnspan=1, column=3, row=36, padx=(20, 0), sticky=tk.E)
custom2_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom2_entry.insert(0, str(custom2_hs))
custom2_entry.grid(columnspan=1, column=4, row=36, sticky=tk.W)
custom2_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom2_entry_name.insert(0, str(custom2_name))
custom2_entry_name.grid(columnspan=1, column=5, row=36, sticky=tk.W)

custom3_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check3, onvalue=1, offvalue=0)
custom3_checkbox.grid(columnspan=1, column=0, row=37, sticky=tk.E)
custom3_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom3_entry.insert(0, str(custom3_hs))
custom3_entry.grid(columnspan=1, column=1, row=37, sticky=tk.W)
custom3_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom3_entry_name.insert(0, str(custom3_name))
custom3_entry_name.grid(columnspan=1, column=2, row=37, sticky=tk.W)

custom4_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check4, onvalue=1, offvalue=0)
custom4_checkbox.grid(columnspan=1, column=3, row=37, padx=(20, 0), sticky=tk.E)
custom4_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom4_entry.insert(0, str(custom4_hs))
custom4_entry.grid(columnspan=1, column=4, row=37, sticky=tk.W)
custom4_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom4_entry_name.insert(0, str(custom4_name))
custom4_entry_name.grid(columnspan=1, column=5, row=37, sticky=tk.W)

custom5_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check5, onvalue=1, offvalue=0)
custom5_checkbox.grid(columnspan=1, column=0, row=38, sticky=tk.E)
custom5_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom5_entry.insert(0, str(custom5_hs))
custom5_entry.grid(columnspan=1, column=1, row=38, sticky=tk.W)
custom5_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom5_entry_name.insert(0, str(custom5_name))
custom5_entry_name.grid(columnspan=1, column=2, row=38, sticky=tk.W)

custom6_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check6, onvalue=1, offvalue=0)
custom6_checkbox.grid(columnspan=1, column=3, row=38, padx=(20, 0), sticky=tk.E)
custom6_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom6_entry.insert(0, str(custom6_hs))
custom6_entry.grid(columnspan=1, column=4, row=38, sticky=tk.W)
custom6_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom6_entry_name.insert(0, str(custom6_name))
custom6_entry_name.grid(columnspan=1, column=5, row=38, sticky=tk.W)

custom7_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check7, onvalue=1, offvalue=0)
custom7_checkbox.grid(columnspan=1, column=0, row=39, sticky=tk.E)
custom7_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom7_entry.insert(0, str(custom7_hs))
custom7_entry.grid(columnspan=1, column=1, row=39, sticky=tk.W)
custom7_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom7_entry_name.insert(0, str(custom7_name))
custom7_entry_name.grid(columnspan=1, column=2, row=39, sticky=tk.W)

custom8_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check8, onvalue=1, offvalue=0)
custom8_checkbox.grid(columnspan=1, column=3, row=39, padx=(20, 0), sticky=tk.E)
custom8_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom8_entry.insert(0, str(custom8_hs))
custom8_entry.grid(columnspan=1, column=4, row=39, sticky=tk.W)
custom8_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom8_entry_name.insert(0, str(custom8_name))
custom8_entry_name.grid(columnspan=1, column=5, row=39, sticky=tk.W)

custom9_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check9, onvalue=1, offvalue=0)
custom9_checkbox.grid(columnspan=1, column=0, row=40, sticky=tk.E)
custom9_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom9_entry.insert(0, str(custom9_hs))
custom9_entry.grid(columnspan=1, column=1, row=40, sticky=tk.W)
custom9_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom9_entry_name.insert(0, str(custom9_name))
custom9_entry_name.grid(columnspan=1, column=2, row=40, sticky=tk.W)

custom10_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check10, onvalue=1, offvalue=0)
custom10_checkbox.grid(columnspan=1, column=3, row=40, padx=(20, 0), sticky=tk.E)
custom10_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom10_entry.insert(0, str(custom10_hs))
custom10_entry.grid(columnspan=1, column=4, row=40, sticky=tk.W)
custom10_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom10_entry_name.insert(0, str(custom10_name))
custom10_entry_name.grid(columnspan=1, column=5, row=40, sticky=tk.W)

custom11_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check11, onvalue=1, offvalue=0)
custom11_checkbox.grid(columnspan=1, column=0, row=41, padx=(20, 0), sticky=tk.E)
custom11_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom11_entry.insert(0, str(custom11_hs))
custom11_entry.grid(columnspan=1, column=1, row=41, sticky=tk.W)
custom11_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom11_entry_name.insert(0, str(custom11_name))
custom11_entry_name.grid(columnspan=1, column=2, row=41, sticky=tk.W)

custom12_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check12, onvalue=1, offvalue=0)
custom12_checkbox.grid(columnspan=1, column=3, row=41, padx=(20, 0), sticky=tk.E)
custom12_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom12_entry.insert(0, str(custom12_hs))
custom12_entry.grid(columnspan=1, column=4, row=41, sticky=tk.W)
custom12_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom12_entry_name.insert(0, str(custom12_name))
custom12_entry_name.grid(columnspan=1, column=5, row=41, sticky=tk.W)

custom13_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check13, onvalue=1, offvalue=0)
custom13_checkbox.grid(columnspan=1, column=0, row=42, padx=(20, 0), sticky=tk.E)
custom13_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom13_entry.insert(0, str(custom13_hs))
custom13_entry.grid(columnspan=1, column=1, row=42, sticky=tk.W)
custom13_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom13_entry_name.insert(0, str(custom13_name))
custom13_entry_name.grid(columnspan=1, column=2, row=42, sticky=tk.W)

custom14_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check14, onvalue=1, offvalue=0)
custom14_checkbox.grid(columnspan=1, column=3, row=42, padx=(20, 0), sticky=tk.E)
custom14_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom14_entry.insert(0, str(custom14_hs))
custom14_entry.grid(columnspan=1, column=4, row=42, sticky=tk.W)
custom14_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom14_entry_name.insert(0, str(custom14_name))
custom14_entry_name.grid(columnspan=1, column=5, row=42, sticky=tk.W)

custom15_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check15, onvalue=1, offvalue=0)
custom15_checkbox.grid(columnspan=1, column=0, row=43, padx=(20, 0), sticky=tk.E)
custom15_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom15_entry.insert(0, str(custom15_hs))
custom15_entry.grid(columnspan=1, column=1, row=43, sticky=tk.W)
custom15_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom15_entry_name.insert(0, str(custom15_name))
custom15_entry_name.grid(columnspan=1, column=2, row=43, sticky=tk.W)

custom16_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check16, onvalue=1, offvalue=0)
custom16_checkbox.grid(columnspan=1, column=3, row=43, padx=(20, 0), sticky=tk.E)
custom16_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom16_entry.insert(0, str(custom16_hs))
custom16_entry.grid(columnspan=1, column=4, row=43, sticky=tk.W)
custom16_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom16_entry_name.insert(0, str(custom16_name))
custom16_entry_name.grid(columnspan=1, column=5, row=43, sticky=tk.W)

custom17_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check17, onvalue=1, offvalue=0)
custom17_checkbox.grid(columnspan=1, column=0, row=44, padx=(20, 0), sticky=tk.E)
custom17_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom17_entry.insert(0, str(custom17_hs))
custom17_entry.grid(columnspan=1, column=1, row=44, sticky=tk.W)
custom17_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom17_entry_name.insert(0, str(custom17_name))
custom17_entry_name.grid(columnspan=1, column=2, row=44, sticky=tk.W)

custom18_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check18, onvalue=1, offvalue=0)
custom18_checkbox.grid(columnspan=1, column=3, row=44, padx=(20, 0), sticky=tk.E)
custom18_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom18_entry.insert(0, str(custom18_hs))
custom18_entry.grid(columnspan=1, column=4, row=44, sticky=tk.W)
custom18_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom18_entry_name.insert(0, str(custom18_name))
custom18_entry_name.grid(columnspan=1, column=5, row=44, sticky=tk.W)

custom19_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check19, onvalue=1, offvalue=0)
custom19_checkbox.grid(columnspan=1, column=0, row=45, padx=(20, 0), sticky=tk.E)
custom19_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom19_entry.insert(0, str(custom19_hs))
custom19_entry.grid(columnspan=1, column=1, row=45, sticky=tk.W)
custom19_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom19_entry_name.insert(0, str(custom19_name))
custom19_entry_name.grid(columnspan=1, column=2, row=45, sticky=tk.W)

custom20_checkbox = tk.Checkbutton(hs_code_frame1, variable=custom_check20, onvalue=1, offvalue=0)
custom20_checkbox.grid(columnspan=1, column=3, row=45, padx=(20, 0), sticky=tk.E)
custom20_entry = tk.Entry(hs_code_frame1, borderwidth=2)
custom20_entry.insert(0, str(custom20_hs))
custom20_entry.grid(columnspan=1, column=4, row=45, sticky=tk.W)
custom20_entry_name = tk.Entry(hs_code_frame1, borderwidth=2)
custom20_entry_name.insert(0, str(custom20_name))
custom20_entry_name.grid(columnspan=1, column=5, row=45, sticky=tk.W)

# Bottom Buttons and Status
bottom_frame1 = tk.Frame(root)
bottom_frame1.grid(columnspan=6, column=0, row=99)

status_reset = tk.Button(bottom_frame1, text="Status Reset", bg="#5eafe4", command=lambda: reset_status())
status_reset.grid(columnspan=1, column=0, row=99, sticky=tk.W)

status_txt = tk.StringVar()
status_lbl_bg = "#5eafe4"
status_lbl = tk.Label(bottom_frame1, textvariable=status_txt, bg=status_lbl_bg)
status_txt.set("Status: Waiting for input")
status_lbl.grid(columnspan=2, column=1, row=99, padx=20, sticky=tk.W)

run_btn = tk.Button(bottom_frame1, text="RUN", bg="#96be25", command=lambda: run_query())
run_btn.grid(columnspan=1, column=4, row=99, sticky=tk.NE, ipadx=25, padx=(100, 20))

version_txt = tk.StringVar()
version_lbl = tk.Label(bottom_frame1, textvariable=version_txt)
version_txt.set(version)
version_lbl.grid(column=6, row=99, sticky=tk.NE)


canvas = tk.Canvas(root, width=700, height=15)
canvas.grid(columnspan=5, rowspan=100)

root.mainloop()