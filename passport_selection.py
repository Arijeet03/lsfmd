import tkinter as tk
from PIL import Image, ImageTk
import os
import pyperclip
import subprocess

def main():

    # Global variable to store the selected photo link
    tasveer = ""

    # Function to handle photo selection, copy URL, and execute newprofile.py
    def select_photo(photo_num):
        global tasveer
        imgur_urls = {
            1: "https://imgur.com/RpFuyeE.png",
            2: "https://imgur.com/zoRPVdn.png",
            3: "https://imgur.com/ExjOTyn.png",
            4: "https://imgur.com/hOoCYCP.png",
            5: "https://imgur.com/W7K0dAN.png",
            6: "https://imgur.com/Z8PTmkZ.png",
            7: "https://imgur.com/sw3yDu8.png",
            8: "https://imgur.com/h5aWWOT.png",
            9: "https://imgur.com/i65V2BZ.png",
            10: "https://imgur.com/KUTT6TQ.png",
            11: "https://imgur.com/1gfaDWK.png",
            12: "https://imgur.com/z5KZW2s.png",
            13: "https://imgur.com/TsDf4TJ.png",
            14: "https://imgur.com/4RlijfR.png",
            15: "https://imgur.com/XcgcmTF.png",
            16: "https://imgur.com/bOuTMa7.png",
            17: "https://imgur.com/YFLw8ev.png",
            18: "https://imgur.com/1l41wwI.png",
            19: "https://imgur.com/rnb1TMM.png",
            20: "https://imgur.com/X9GOJyy.png"
        }
        tasveer = imgur_urls.get(photo_num)
        pyperclip.copy(tasveer)
        print("Image URL copied to clipboard and variable:", tasveer)

        # Execute newprofile.py with the selected photo URL
        base_dir = os.path.dirname(os.path.abspath(__file__))
        subprocess.run(["python", os.path.join(base_dir, "newprofile.py"), tasveer])

        # Close the window after selecting a photo
        passport_window.after(100, passport_window.destroy)

    # Create the passport selection window
    passport_window = tk.Tk()
    passport_window.title("Passport Selection")

    # Get the directory of the currently executing script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Relative path to the passport images folder
    passport_dir = os.path.join(base_dir, "sources", "passport")

    # Create a frame to hold the rows of images and buttons
    content_frame = tk.Frame(passport_window)
    content_frame.pack(expand=True, fill="both")

    # Caption for selecting passport photograph
    caption = tk.Label(passport_window, text="Select your passport photograph from these options here", font=("Arial", 14, "bold"))
    caption.pack(pady=10)

    # Loop through passport images and display with "Select" buttons
    for i in range(1, 21):
        # Calculate row and column index for each image
        row_idx = (i - 1) // 5
        col_idx = (i - 1) % 5

        # Load image
        image_path = os.path.join(passport_dir, f"image_{i}.jpeg")
        image = Image.open(image_path)
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)

        # Create a frame for each row of images
        if col_idx == 0:
            row_frame = tk.Frame(content_frame)
            row_frame.pack(side="top", fill="x", pady=10)

        # Create a label to display the image
        label_image = tk.Label(row_frame, image=photo)
        label_image.image = photo
        label_image.grid(row=row_idx, column=col_idx, padx=10)

        # Create a button for each image
        btn_select_photo = tk.Button(row_frame, text="Select", command=lambda idx=i: select_photo(idx))
        btn_select_photo.grid(row=row_idx + 1, column=col_idx, pady=5)

    # Run the application
    passport_window.mainloop()
    pass

if __name__ == "__main__":
    main()
