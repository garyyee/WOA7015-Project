import gzip
import joblib
import json
import numpy as np
import pandas as pd
import pickle
from tqdm import tqdm
from colorama import Fore, Back, Style

# =========================================================================================================
# Data Extraction / Export functions
# =========================================================================================================
def read_file(path='', usecols=None, sort=False, replace_negative_one=False, replace_negative127=True):
    # LOAD DATAFRAME
    if path.endswith(".parquet"):
        if usecols is not None:
            df = pd.read_parquet(path, columns=usecols)
        else:
            df = pd.read_parquet(path)
    elif path.endswith(".ftr"):
        df = pd.read_feather(path)
    elif path.endswith(".csv"):
        df = pd.read_csv(path)
    elif path.endswith(".pkl"):
        df = pd.read_pickle(path)
    elif path.endswith(".json"):
        with gzip.GzipFile(path, mode='rb') as f:
            a = f.read()
        return a

def load_pickle(fpath):
    with open(fpath, "rb") as p:
        a = pickle.load(p)
    return a

def read_parquet(fpath):
    df = pd.read_parquet(fpath)
    df["dt"] = pd.to_datetime(df["ts"], unit='ms')
    return df

def export_data(data, fpath):
    if fpath.endswith(".pkl"):
        joblib.dump(data, fpath)
    elif fpath.endswith(".json"):
        with open(fpath, "w") as outfile:
            json.dump(data, outfile)
    else:
        print("Not pickle or json file, stop export")
        
def save_json_gz(obj, filepath):
    json_str = json.dumps(obj)
    json_bytes = json_str.encode()
    with gzip.GzipFile(filepath, mode="w") as f:
        f.write(json_bytes)

# =========================================================================================================
# Visualize Functions
# =========================================================================================================
def print_green(string, **kwargs):
    print(f"{Fore.GREEN}{Style.BRIGHT}" + string + f"{Style.RESET_ALL}", **kwargs)
    
def print_blue(string, **kwargs):
    print(f"{Fore.BLUE}{Style.BRIGHT}" + string + f"{Style.RESET_ALL}", **kwargs)

def print_red(string, **kwargs):
    print(f"{Fore.RED}{Style.BRIGHT}" + string + f"{Style.RESET_ALL}", **kwargs) 