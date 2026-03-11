import os
import sys
from textnode import TextNode
from textnode import TextType
from copystatic import replace_dir
from generatecontent import generate_pages_recursive

static_path = "./static" 
docs_path = "./docs" 
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
  bbasepath = default_basepath
  if len(sys.argv) > 1:
      basepath = sys.argv[1]
  

  replace_dir(static_path, docs_path)
 
  
  print("Generating content...")
  generate_pages_recursive(dir_path_content, template_path,docs_path, basepath)

main()

