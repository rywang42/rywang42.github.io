import os
from pathlib import Path

def extract_number(filename):
    # Extract the number from filenames like IMG_2737.JPG
    try:
        return int(''.join(filter(str.isdigit, filename)))
    except ValueError:
        return float('inf')  # For files without numbers

def generate_photography_yaml():
    # Base directory for photography images
    base_dir = "/Users/owlowiscious/Desktop/seriousStuff/longTerm/rywang42.github.io/images/galleries/photography"

    # YAML header
    yaml_content = """---
name: "photography"
arts:
"""

    # Collect all image files with their full paths and categories
    image_files = []
    for root, dirs, files in os.walk(base_dir):
        category = os.path.relpath(root, base_dir)
        category = category if category != "." else ""

        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_files.append({
                    'file': file,
                    'category': category,
                    'full_path': os.path.join(category, file)
                })

    # Sort by the numeric part of the filename
    image_files.sort(key=lambda x: extract_number(x['file']))

    # Generate YAML entries
    for order, img_data in enumerate(image_files, 1):
        image_path = os.path.join("images/galleries/photography", img_data['full_path'])
        image_path = image_path.replace("\\", "/")  # Ensure forward slashes

        yaml_content += f"""- image: "{image_path}"
  order: "{order}"
  title: "{img_data['category'] if img_data['category'] else 'Uncategorized'}"
  description: "[{img_data['category'] if img_data['category'] else 'Uncategorized'}]"

"""

    # Write to file
    output_path = "/Users/owlowiscious/Desktop/seriousStuff/longTerm/rywang42.github.io/_galleries/photography.yml"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(yaml_content)

if __name__ == "__main__":
    generate_photography_yaml()