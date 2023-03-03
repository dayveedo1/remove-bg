from rembg import remove
from PIL import Image

input_path = 'me_career_home.jpg'           # Path to the image you want to remove the background from
output_path = 'me_career_home_no_bg.png'    # Path to the image you want to save the result to

input = Image.open(input_path)              # Open the image
output = remove(input)                      # Remove the background
output.save(output_path)                    # Save the result

