from PIL import Image
import numpy as np


def text_to_rgb_matrix(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    with open(input_file, 'w') as file:
        file.writelines(lines[:-1])
    with open(input_file, 'r') as f:
        width, height = map(int, f.readline().strip().split())
        
        matrix = []
        for line in f:
            pixel = list(map(int, line.strip().split()))
            matrix.append(pixel)

    matrix = np.array(matrix).reshape((height, width, 3))
    
    return matrix, width, height

def rgb_matrix_to_image(matrix, output_image_path):
    img = Image.fromarray(matrix.astype(np.uint8), mode='RGB')

    img.save(output_image_path)


def text_to_grayscale_matrix(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    with open(input_file, 'w') as file:
        file.writelines(lines[:-1])
    with open(input_file, 'r') as f:
        width, height = map(int, f.readline().strip().split())
        
        matrix = []
        for line in f:
            pixel = int(line.strip())
            matrix.append(pixel)
    
    matrix = np.array(matrix).reshape((height, width))
    
    return matrix, width, height

def grayscale_matrix_to_image(matrix, output_image_path):
    img = Image.fromarray(matrix.astype(np.uint8), mode='L')
    
    img.save(output_image_path)

if __name__ == "__main__":
    input_file = 'phase2/resized_matrix.txt'
    output_image = 'phase2/output_image_resized.jpg'
    rgb_matrix, width, height = text_to_rgb_matrix(input_file)
    rgb_matrix_to_image(rgb_matrix, output_image)
    print(f"Image has been created and saved to '{output_image}' successfully.")

    input_file = 'phase2/grayscaled_matrix.txt'
    output_image = 'phase2/output_image_grayscaled.jpg'
    grayscale_matrix, width, height = text_to_grayscale_matrix(input_file)
    grayscale_matrix_to_image(grayscale_matrix, output_image)
    print(f"Image has been created and saved to '{output_image}' successfully.")

    input_file = 'phase2/edge_detection_matrix.txt'
    output_image = 'phase2/output_image_edge_detection.jpg'
    grayscale_matrix, width, height = text_to_grayscale_matrix(input_file)
    grayscale_matrix_to_image(grayscale_matrix, output_image)
    print(f"Image has been created and saved to '{output_image}' successfully.")

    input_file = 'phase2/gaussian_blur_matrix.txt'
    output_image = 'phase2/output_image_gaussian_blur.jpg'
    grayscale_matrix, width, height = text_to_grayscale_matrix(input_file)
    grayscale_matrix_to_image(grayscale_matrix, output_image)
    print(f"Image has been created and saved to '{output_image}' successfully.")
