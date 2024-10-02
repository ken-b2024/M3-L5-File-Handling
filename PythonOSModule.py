import os

def list_directory_contents(path):
    new_path = input("Enter the path of the directory you wish to access: ")
    if os.path.exists(new_path):
      print(f"Here are the contents of your directory: \n{os.listdir(new_path)}")
    else:
      print("This path is not valid. Please try again.")

list_directory_contents('path')