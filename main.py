import os
from PIL import Image
import pillow_avif  # Ensure this plugin is imported to add AVIF support

# Define paths
data_folder = 'data'
old_folder = os.path.join(data_folder, 'old')

# Create 'old' directory if it doesn't exist
if not os.path.exists(old_folder):
    os.makedirs(old_folder)

# Function to convert images to PNG
def convert_to_png(image_path, output_path):
    with Image.open(image_path) as img:
        img.save(output_path, 'PNG')

# Iterate through files in the data folder
for filename in os.listdir(data_folder):
    file_path = os.path.join(data_folder, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Determine output file path
    output_filename = os.path.splitext(filename)[0] + '.png'
    output_path = os.path.join(data_folder, output_filename)
    
    # Convert and save image as PNG
    try:
        convert_to_png(file_path, output_path)
        
        # Move original file to 'old' folder
        old_file_path = os.path.join(old_folder, filename)
        os.rename(file_path, old_file_path)
        print(f"Converted {filename} to PNG and moved the original to 'old' folder.")
    except Exception as e:
        print(f"Failed to convert {filename}: {e}")

print("Conversion process completed.")
