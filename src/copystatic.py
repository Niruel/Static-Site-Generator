import os
import shutil

def replace_dir(static_path, public_path):


  delete_dir_contents(public_path)
  copy_files_recursive(static_path, public_path)

#correct answer
def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
            
def copy_dir_to(from_dir_path, to_dir_path):
  if os.path.exists(from_dir_path):
    static_dir = os.listdir(path = from_dir_path)
    for item in static_dir:
      if os.path.isfile(from_dir_path + "/" + item):
        shutil.copy(from_dir_path + "/" + item, to_dir_path + "/" + item)
      elif os.path.isdir(from_dir_path + "/" + item):
        shutil.copytree(from_dir_path + "/" + item, to_dir_path + "/" + item)

def delete_dir_contents(public_file_path):
   print("Deleting public directory...")
   if os.path.exists(public_file_path):
      shutil.rmtree(public_file_path)

    # Wrong way
    # public_dir = os.listdir(path=public_file_path)
    # for item in public_dir:
      
    #   if os.path.isfile(public_file_path + "/"+ item):
    #     os.remove(public_file_path + "/"+ item)
    #   elif os.path.isdir(public_file_path + "/"+ item):
    #     shutil.rmtree(public_file_path + "/"+ item)
      