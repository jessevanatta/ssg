import os, shutil
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_converter import *

linebreak = "------------------------------------"
astbreak = "************************************"

def refresh_public(src, dst):
    # Delete destination dir if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleted {dst}")

    # Create destination dir
    os.mkdir(dst)
    print(f"Recreated {dst}")
    print(linebreak)

    # Get list of paths in source
    source_list = os.listdir(src)

    # Loop over list and recurse this func to copy items
    for item in source_list:
        item_path = os.path.join(src, item)
        # Copy item
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
            print(f"Entering directory {current_dir}")
            refresh_public(current_dir, new_dir)

def extract_title(markdown):
    title = markdown.split("\n")[0]
    if title[0] != "#" or title[1] != " ":
        raise Exception("Invalid markdown syntax.")
    # Remove hash and surrounding whitespaces from markdown title
    return title.lstrip("#").strip()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = open(from_path).read()
    template = open(template_path).read()
    title = extract_title(md)
    node = markdown_to_html_node(md)
    html = node.to_html()
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    page_file = open(f"{dest_path}/index.html", "w")
    page_file.write(page)
    page_file.close()

def main():
    public_complete = False

    # Refresh public directory with source tree
    refresh_source = "./static"
    refresh_destination = "./public"
    refresh_public(refresh_source, refresh_destination)

    # Verify tree match
    source_length = len(os.listdir(refresh_source))
    destination_length = len(os.listdir(refresh_destination))
    if source_length == destination_length:
        public_complete = True
        print("Successfully copied all data.")
        print(astbreak)
    
    # Generate index.html
    if public_complete:
        generate_page("./content/index.md", "./template.html", "./public")
        

main()