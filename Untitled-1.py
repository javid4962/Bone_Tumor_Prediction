# import cv2

# def enhance_image(input_image_path):
#     # Read the input image
#     img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

#     # Apply histogram equalization
#     enhanced_img = cv2.equalizeHist(img)

#     return enhanced_img

# # Example usage:
# input_image_path = 'test1.png'
# enhanced_image = enhance_image(input_image_path)

# # Display the original and enhanced images
# cv2.imshow('Original Image', cv2.imread(input_image_path))
# cv2.imshow('Enhanced Image', enhanced_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import tkinter as tk
from tkinter import filedialog
import os

def enhance_and_save_image(input_image_path):
    # Read the input image
    img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Apply histogram equalization
    enhanced_img = cv2.equalizeHist(img)

    # Get the filename and folder path
    filename = os.path.basename(input_image_path)
    folder_path = os.path.dirname(input_image_path)

    # Create a folder for saving the enhanced images if it doesn't exist
    save_folder = os.path.join(folder_path, "enhanced_images")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Save the enhanced image in the "enhanced_images" folder
    save_path = os.path.join(save_folder, filename)
    cv2.imwrite(save_path, enhanced_img)

    return save_path

def select_and_enhance_image():
    # Open a file dialog for image selection
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        # Call the enhance_and_save_image function with the selected image path
        enhanced_image_path = enhance_and_save_image(file_path)

        # Display a message box with the path to the saved enhanced image
        # messagebox.showinfo("Enhanced Image Saved", f"The enhanced image has been saved at:\n{enhanced_image_path}")

# Create a Tkinter window
root = tk.Tk()
root.title("Image Enhancement")

# Create a button for selecting and enhancing the image
select_button = tk.Button(root, text="Select and Enhance Image", command=select_and_enhance_image)
select_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
