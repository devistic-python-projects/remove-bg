from rembg import remove
from PIL import Image

# Specify the input and output file paths
input_path = 'icon.png'
output_path = 'output.png'

# Open the input image
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the resulting image
output_image.save(output_path)
