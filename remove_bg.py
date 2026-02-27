from PIL import Image
import os

# Define paths
input_path = r"c:\Users\Bnant\Desktop\Nord Breeze Digital WEBSITE\nord breeze logo.png"
output_path = r"c:\Users\Bnant\Desktop\Nord Breeze Digital WEBSITE\nord breeze logo.png"

# Open the image
img = Image.open(input_path)

# Convert to RGBA if not already
img = img.convert('RGBA')

# Get pixel data
pixels = img.load()

# Define the background color (typically white or light color)
# We'll remove pixels that are similar to white
width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        
        # If pixel is close to white (high RGB values), make it transparent
        if r > 240 and g > 240 and b > 240:
            pixels[x, y] = (r, g, b, 0)  # Make transparent

# Save the result
img.save(output_path, 'PNG')
print(f"Background removed successfully! Saved to: {output_path}")
