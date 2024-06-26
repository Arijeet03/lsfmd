import tkinter as tk
from tkinter import messagebox
import ctypes
import os
import sys

def main():

    def copy_to_clipboard(text):
        ctypes.windll.user32.OpenClipboard(0)
        ctypes.windll.user32.EmptyClipboard()
        ctypes.windll.user32.SetClipboardData(1, ctypes.create_string_buffer(text.encode("utf-8")))
        ctypes.windll.user32.CloseClipboard()

    def submit_resignation():
        name = entry_name.get()
        rank = entry_rank.get()
        profile_link = entry_profile_link.get()
        purpose_of_resignation = entry_purpose.get()
        date_of_resignation = entry_date.get()
        additional_info = entry_additional_info.get()

        # Generate BBCode
        bbcode = f"""
    [TABLE="class: grid, width: 500, align: center"][TR][TD][COLOR="#FFFFFF"]51st Chief Saksham Slash[/COLOR][LEFT][/LEFT][CENTER][img]https://i.imgur.com/m4aFQpA.png?1[/img][IMG]https://i.imgur.com/ysNwX1n.png[/IMG][B][COLOR=#ffc0cb][SIZE=5]LOS SANTOS FIRE & MEDICAL DEPARTMENT[/SIZE][/COLOR]
    [FONT=courier new][SIZE=4][COLOR=#ffffff]Resignation Letter[/COLOR][/SIZE][/FONT][/B][FONT=courier new][IMG]https://i.imgur.com/ysNwX1n.png[/IMG][/FONT][/CENTER]
    [COLOR=#ffc0cb][SIZE=2][B]Employee's Name:[/B][/SIZE][/COLOR] [COLOR="#FFFFFF"]{name}[/COLOR]
    [COLOR=#ffc0cb][SIZE=2][B]Employee's current rank in the department:[/B][/SIZE][/COLOR] [COLOR="#FFFFFF"]{rank}[/COLOR]
    [COLOR=#ffc0cb][SIZE=2][B]Employee profile:[/B][/SIZE][/COLOR] [url={profile_link}][COLOR="#FFFFFA"]** Attachment **[/COLOR][/url]
    [COLOR=#ffc0cb][SIZE=2][B]Purpose of Resignation:[/B][/SIZE][/COLOR] [COLOR="#FFFFFF"]{purpose_of_resignation}[/COLOR]
    [COLOR=#ffc0cb][SIZE=2][B]Date of Resignation:[/B][/SIZE][/COLOR] [COLOR="#FFFFFF"]{date_of_resignation}[/COLOR]
    [COLOR=#ffc0cb][SIZE=2][B]Addtional Info:[/B][/SIZE][/COLOR] [COLOR="#FFFFFF"]{additional_info}[/COLOR]

    [COLOR="#FFFFE0"][QUOTE]I [B]{name}[/B] solemnly swear, by the power of Chief Slash, that I will not involve myself in any LSFMD business. This includes undergoing castration or usage of sexual toys and I understand that posting my letter will not allow me to reinstate back into the department for a month.[/quote][/COLOR][/TD][/TR][/TABLE]
    """
        copy_to_clipboard(bbcode)
        messagebox.showinfo("Success", "BBCode copied to clipboard!")
        root.destroy()

    # def close_all_windows_except_main_menu():
        # Get the PID of the main menu window if it's running
    #   main_menu_pid = None
    #   for window in tk._default_root.tk.eval('wm stackorder .').split():
    #      if 'Main Menu' in window:
    #          main_menu_pid = window

        # Close all windows except the main menu
    # for window in tk._default_root.tk.eval('wm stackorder .').split():
    #     if window != main_menu_pid:
    #         tk._default_root.tk.call('destroy', window)

    # Create the main window
    root = tk.Tk()
    root.title("Resignation Form")
    root.geometry("400x600")

    # Add the heading
    label_heading = tk.Label(root, text="Fill your details here", font=("Arial", 14, "bold"))
    label_heading.pack(pady=10)

    # Name
    label_name = tk.Label(root, text="Name:")
    label_name.pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    # Rank
    label_rank = tk.Label(root, text="Rank:")
    label_rank.pack()
    entry_rank = tk.Entry(root)
    entry_rank.pack()

    # Profile Link
    label_profile_link = tk.Label(root, text="Profile Link:")
    label_profile_link.pack()
    entry_profile_link = tk.Entry(root)
    entry_profile_link.pack()

    # Purpose of Resignation
    label_purpose = tk.Label(root, text="Purpose of Resignation:")
    label_purpose.pack()
    entry_purpose = tk.Entry(root)
    entry_purpose.pack()

    # Date of Resignation
    label_date = tk.Label(root, text="Date of Resignation:")
    label_date.pack()
    entry_date = tk.Entry(root)
    entry_date.pack()

    # Additional Info
    label_additional_info = tk.Label(root, text="Additional Info:")
    label_additional_info.pack()
    entry_additional_info = tk.Entry(root)
    entry_additional_info.pack()

    # Submit button
    btn_submit = tk.Button(root, text="Submit", command=submit_resignation)
    btn_submit.pack(pady=20)

    # Run the application
    root.mainloop()

    pass

if __name__ == "__main__":
    main()