import tkinter as tk
from PIL import Image, ImageTk
import os
import multiprocessing
import webbrowser
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for cx_Freeze """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Function to open the passport selection window
def open_passport_selection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "passport_selection.py")
    multiprocessing.Process(target=lambda: os.system(f'python "{script_path}"')).start()

# Function to open the Employee Profiles window
def open_employee_profiles():
    profile_window = tk.Toplevel(root)
    profile_window.title("Employee Profiles")
    profile_window.geometry("400x600")
    profile_window.grab_set()

    # Update image path for the logo
    image_path = resource_path("sources/eGweu7I.png")

    logo = Image.open(image_path)
    logo = logo.resize((200, 200))
    logo = ImageTk.PhotoImage(logo)

    label_logo = tk.Label(profile_window, image=logo)
    label_logo.image = logo
    label_logo.pack(pady=10)

    # Button to open passport selection window
    btn_new_profile = tk.Button(profile_window, text="Create New Profile", command=open_passport_selection)
    btn_new_profile.pack(pady=10)

    btn_reply_profile = tk.Button(profile_window, text="Reply To Profile", command=open_reply_to_profile)
    btn_reply_profile.pack(pady=10)

    # Add exit button to employee profiles window
    btn_exit = tk.Button(profile_window, text="Back to Main Menu", command=profile_window.destroy)
    btn_exit.pack(pady=10)

def open_reply_to_profile():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "reply_to_profile.py")
    multiprocessing.Process(target=lambda: os.system(f'python "{script_path}"')).start()

# Function to open the resignations window
def open_resignations():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, "resignations.py")
    multiprocessing.Process(target=lambda: os.system(f'python "{script_path}"')).start()

# Function to open Discord profile link
def open_discord_link(event):
    webbrowser.open("https://discordapp.com/users/700554982750945281")

# Create the main window
root = tk.Tk()
root.title("LSFMD Copy Format")
root.geometry("400x600")

# Load and display the logo image
image_path = resource_path("sources/eGweu7I.png")
image = Image.open(image_path)
image = image.resize((200, 200))
logo = ImageTk.PhotoImage(image)

label_logo = tk.Label(root, image=logo)
label_logo.image = logo
label_logo.pack(pady=10)

# Create a welcome caption
caption = tk.Label(root, text="LSFMD Copy Format v1", font=("Segoe UI Light", 14, "bold"))
caption.pack(pady=10)

# Create buttons for the main menu
btn_employee_profiles = tk.Button(root, text="Employee Profiles", command=open_employee_profiles)
btn_employee_profiles.pack(pady=10)

btn_loa_resignations = tk.Button(root, text="Resignations", command=open_resignations)
btn_loa_resignations.pack(pady=10)

# Add exit button to main window
btn_exit_main = tk.Button(root, text="Exit", command=root.quit)
btn_exit_main.pack(pady=10)

# Create a frame for the labels
label_frame = tk.Frame(root)
label_frame.pack(side="bottom")

# Create the credits label
label_credits = tk.Label(label_frame, text="Made by ", font=("Arial", 10))
label_credits.pack(side="left")

# Create the clickable Discord link
discord_link = tk.Label(label_frame, text="terminatedguy", font=("Arial", 10), fg="blue", cursor="hand2")
discord_link.pack(side="left")
discord_link.bind("<Button-1>", open_discord_link)

# Run the application
root.mainloop()
