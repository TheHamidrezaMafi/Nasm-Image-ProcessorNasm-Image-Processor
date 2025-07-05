from PIL import Image
import numpy as np

# Function to convert RGB image to RGB matrix
def image_to_rgb_matrix(image_path):
    img = Image.open(image_path)
    
    # Ensure the image is in RGB mode
    img = img.convert('RGB')
    
    # Convert PIL image to numpy array
    matrix = np.array(img)
    
    return img.width, img.height, matrix

# Function to write RGB matrix to text file with image dimensions
def rgb_matrix_to_text(matrix, width, height, output_file):
    with open(output_file, 'w') as f:
        # Write the width and height as the first line
        f.write(f"{width} {height}\n")
        
        for row in matrix:
            for pixel in row:
                # Join pixel elements as strings and write to file
                pixel_str = ' '.join(map(str, pixel))
                f.write(pixel_str + '\n')

if __name__ == "__main__":
    # Replace 'input_image.jpg' with your input image file path
    input_image = 'phase2/input_image.jpg'
    
    # Replace 'output_matrix.txt' with desired output text file path
    output_file = 'phase2/output_matrix.txt'
    
    # Convert image to RGB matrix and get dimensions
    width, height, rgb_matrix = image_to_rgb_matrix(input_image)
    
    # Write RGB matrix to text file with dimensions
    rgb_matrix_to_text(rgb_matrix, width, height, output_file)
    
    print(f"RGB matrix of the image has been written to '{output_file}' successfully.")
