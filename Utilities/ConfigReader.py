from configparser import ConfigParser
import os

def read_config(section, key, file_path="D:\\Programming\\PythonProgramming\\PageObjectModelFramework\\Configurations\\config.ini"):
    global config
    config = ConfigParser()
    current_dir = os.getcwd()
    print(f"current_dir in config reader: {current_dir}")
    print(f"file_path in config reader: {file_path}")
    filename = config.read(file_path)
    value = config.get(section, key)
    return value

def get_all_keys(section, file_path="D:\\Programming\\PythonProgramming\\PageObjectModelFramework\\Configurations\\config.ini"):
    config = ConfigParser()
    config.read(file_path)
    return config.options(section)

if __name__ == "__main__":
    print(read_config('basic info','testsiteurl'))
    for key in get_all_keys('locators'):
        value = read_config( 'locators', key)
        print(f"{key}: {value}")