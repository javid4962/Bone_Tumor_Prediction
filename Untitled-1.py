# # import cv2

# # def enhance_image(input_image_path):
# #     # Read the input image
# #     img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# #     # Apply histogram equalization
# #     enhanced_img = cv2.equalizeHist(img)

# #     return enhanced_img

# # # Example usage:
# # input_image_path = 'test1.png'
# # enhanced_image = enhance_image(input_image_path)

# # # Display the original and enhanced images
# # cv2.imshow('Original Image', cv2.imread(input_image_path))
# # cv2.imshow('Enhanced Image', enhanced_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# import cv2
# import tkinter as tk
# from tkinter import filedialog
# import os

# def enhance_and_save_image(input_image_path):
#     # Read the input image
#     img = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

#     # Apply histogram equalization
#     enhanced_img = cv2.equalizeHist(img)

#     # Get the filename and folder path
#     filename = os.path.basename(input_image_path)
#     folder_path = os.path.dirname(input_image_path)

#     # Create a folder for saving the enhanced images if it doesn't exist
#     save_folder = os.path.join(folder_path, "enhanced_images")
#     if not os.path.exists(save_folder):
#         os.makedirs(save_folder)

#     # Save the enhanced image in the "enhanced_images" folder
#     save_path = os.path.join(save_folder, filename)
#     cv2.imwrite(save_path, enhanced_img)

#     return save_path

# def select_and_enhance_image():
#     # Open a file dialog for image selection
#     file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
#     if file_path:
#         # Call the enhance_and_save_image function with the selected image path
#         enhanced_image_path = enhance_and_save_image(file_path)

#         # Display a message box with the path to the saved enhanced image
#         # messagebox.showinfo("Enhanced Image Saved", f"The enhanced image has been saved at:\n{enhanced_image_path}")

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Image Enhancement")

# # Create a button for selecting and enhancing the image
# select_button = tk.Button(root, text="Select and Enhance Image", command=select_and_enhance_image)
# select_button.pack(pady=10)

# # Run the Tkinter event loop
# root.mainloop()



# ## Data processing code 
# def datasetPreprocessing():
#     global X
#     global Y
#     image_count = 0
#     # X.clear()
#     # Y.clear()
#     if os.path.exists('Model/myimg_data.txt.npy'):
#         X = np.load('Model/myimg_data.txt.npy')
#         Y = np.load('Model/myimg_label.txt.npy')
#     else:
#         for root, dirs, directory in os.walk(filename+"/no"):
#             for i in range(len(directory)):
#                 name = directory[i]
#                 img = cv2.imread(filename+"/no/"+name,0) #reading images
#                 ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) #processing and normalization images
#                 img = cv2.resize(img, (256,256)) #resizing images
#                 im2arr = np.array(img) #extract features from images
#                 im2arr = im2arr.reshape(128,128,1)
#                 X.append(im2arr)
#                 Y.append(0)
#                 print(filename+"/no/"+name)
#                 image_count += 1

#         for root, dirs, directory in os.walk(filename+"/yes"):
#             for i in range(len(directory)):
#                 name = directory[i]
#                 img = cv2.imread(filename+"/yes/"+name,0)
#                 ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#                 img = cv2.resize(img, (128,128))
#                 im2arr = np.array(img)
#                 im2arr = im2arr.reshape(128,128,1)
#                 X.append(im2arr)
#                 Y.append(1)
#                 print(filename+"/yes/"+name)
#                 image_count += 1
                
#         X = np.asarray(X)
#         Y = np.asarray(Y)            
#         np.save("Model/myimg_data.txt",X)
#         np.save("Model/myimg_label.txt",Y)
#     # print(X.shape)
#     # print(Y.shape)
#     # print(Y)
#     cv2.imshow('ss',X[20])
#     cv2.waitKey(0)
#     text.insert(END,"Total number of images found in dataset : "+str(image_count)+"\n")
#     text.insert(END,"Total number of classes : "+str(len(set(Y)))+"\n\n")
#     text.insert(END,"Class labels found in dataset : "+str(disease))
   
   
import numpy as np
import cv2
import os

# Load the .npy file
data = np.load('Model/myimg_data.txt.npy')
# Load the .npy file
label = np.load('Model/myimg_label.txt.npy')

# Specify the folder path to save the data
Yes_save_folder = 'Dummy/yes'
No_save_folder = 'Dummy/no'

# Create the folder if it doesn't exist
os.makedirs(Yes_save_folder, exist_ok=True)
os.makedirs(No_save_folder, exist_ok=True)

# Save the data to the folder
# Save each image in the data array as a PNG file
for i, (image,label) in enumerate(zip(data,label)):
    image = np.array(image)
    if label == 1:
        save_path = os.path.join(Yes_save_folder, f'Y{i}.png')
    else:
        save_path = os.path.join(No_save_folder, f'N{i}.png')
    cv2.imwrite(save_path, image)
        
# np.save(save_path, data)

###############################################

# Specify the folder path to save the data
# save_folder = 'Dummy2'

# # Create the folder if it doesn't exist
# os.makedirs(save_folder, exist_ok=True)

# # Save each image in the data array as a PNG file
# for i, image in enumerate(data):
#     image = np.array(image)  # Convert to NumPy array
#     # save_path = os.path.join(save_folder, f'image_{i}.txt')
#     # cv2.imwrite(save_path, image)
#     print(image)

# # Print a message to indicate the completion of saving the images
# print(f'{len(data)} images saved as PNG files in {save_folder}.')
