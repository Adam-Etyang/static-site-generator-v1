import os
import markdown
import  shutil
import re
# Define paths
shutil.copytree("static", "output/static", dirs_exist_ok=True)
CONTENT_DIR = "content"
OUTPUT_DIR = "output"
TEMPLATE_FILE = "templates/base.html"
# extracting title

def extract_title(md_content):
    #spliting the markdown content into lines
    lines = md_content.split("\n")
    for line in lines:
        #using regex to find a line with "#" followed by a space
        match = re.match(r"^(#{1,6})\s+(.*)", line)
        if match:
            return match.group(2).strip()
    return "untitled page"
 Load the template
with open(TEMPLATE_FILE, "r") as file:
    template = file.read()

#extract_bold characters
def extract_bold(md_content):
    for word in md_content:
        match = re.match(r"^(*{2})+(.*)", word)
        if match:
            return match.group(2).strip()

#extract italics
def extract_italics(md_content):
    for word in md_content:
        match = re.match(r"^(*{1})+(.*)", word)
    if match:
        return match.group(2).strip()



# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Process Markdown files
for filename in os.listdir(CONTENT_DIR):
    print(f"Processing:{filename}")
    if filename.endswith(".md"):
        filepath = os.path.join(CONTENT_DIR, filename)
        
        # Read Markdown file
        with open(filepath, "r") as file:
            md_content = file.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)
       
        #extracting texts:
        





        # Save output as HTML
        output_filepath = os.path.join(OUTPUT_DIR, filename.replace(".md", ".html"))
        with open(output_filepath, "w") as file:
            file.write(full_html)

        print(f"Generated: {output_filepath}")

