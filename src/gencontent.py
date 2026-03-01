import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
           return line[2:].strip()
    raise Exception("No header found")

    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        content_md = f.read()

    with open(template_path, 'r') as t:
        content_template = t.read()

    tp_node = markdown_to_html_node(content_md)
    node_2_html = tp_node.to_html()        
    template_title = extract_title(content_md)
    content_template = content_template.replace("{{ Title }}", template_title)
    content_template = content_template.replace("{{ Content }}", node_2_html)

    directory = os.path.dirname(dest_path)
    if directory != "":
        os.makedirs(directory, exist_ok= True)

    with open(dest_path, 'w') as file:
        file.write(content_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    

    