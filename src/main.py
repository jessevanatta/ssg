import os, shutil, sys
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_converter import *

basepath = "/"
if len(sys.argv) > 1:
    basepath = sys.argv[1]

linebreak = "------------------------------------"
astbreak = "************************************"

def copy_static_files(src, dst):
    # Delete and recreate destination 
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleted {dst}")
    os.mkdir(dst)
    print(f"Recreated {dst}")
    print(linebreak)

    # Get list of paths in source
    source_list = os.listdir(src)

    # Copy items
    for item in source_list:
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            print(f"Copying {item_path} to {dst}...")
            shutil.copy(item_path, dst)
            print(f"New file: {os.path.join(dst, item)}")
            print(linebreak)
        else:
            current_dir = os.path.join(src, item)
            new_dir = os.path.join(dst, item)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            print(f"Entering source directory {current_dir}")
            copy_static_files(current_dir, new_dir)

def generate_content(src, dst, bp):
    tmpl = "./template.html"
    
    # Get list of paths in source
    source_list = os.listdir(src)

    # Generate pages
    for item in source_list:
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            print(f"Generating HTML page for {item_path}...")
            generate_page(item_path, tmpl, dst, bp)
            print(f"New page: {os.path.join(dst, os.listdir(dst)[0])}")
            print(linebreak)
        else:
            current_dir = os.path.join(src, item)
            new_dir = os.path.join(dst, item)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            print(f"Entering source directory {current_dir}")    
            generate_content(current_dir, new_dir, bp)

def extract_title(markdown):
    title = markdown.split("\n")[0]
    if title[0] != "#" or title[1] != " ":
        raise Exception("Invalid markdown syntax.")
    # Remove hash and surrounding whitespaces from markdown title
    return title.lstrip("#").strip()

def generate_page(from_path, template_path, dest_path, base_path):
    md = open(from_path).read()
    template = open(template_path).read()
    title = extract_title(md)
    node = markdown_to_html_node(md)
    html = node.to_html()
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    page_file = open(f"{dest_path}/index.html", "w")
    page_file.write(page)
    page_file.close()

def main():
    # Copy static files to public
    print(astbreak)
    print("Beginning copy of static files.")
    print(linebreak)
    copy_static_files("./static", "./docs")
    print("Finished copying static files.")
    print(astbreak)
   
    # Generate pages
    print(astbreak)
    print("Beginning generation of HTML pages.")
    print(linebreak)
    generate_content("./content", "./docs", basepath)
    print(f"Finished generating HTML pages.")
    print(astbreak)

main()