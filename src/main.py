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

def main():
  basepath = sys.argv[0]
  if not basepath:
    basepath = '/'
  

  replace_dir(static_path, docs_path)
 
  
  print("Generating content...")
  generate_pages_recursive(dir_path_content, template_path,docs_path, basepath)

main()

