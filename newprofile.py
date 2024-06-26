import tkinter as tk
from tkinter import messagebox
import ctypes
import sys

def main():

    # Retrieve the tasveer URL from the command line arguments
    tasveer = sys.argv[1] if len(sys.argv) > 1 else ""

    def copy_to_clipboard(text):
        ctypes.windll.user32.OpenClipboard(0)
        ctypes.windll.user32.EmptyClipboard()
        ctypes.windll.user32.SetClipboardData(1, ctypes.create_string_buffer(text.encode("utf-8")))
        ctypes.windll.user32.CloseClipboard()

    def submit_form():
        name = entry_name.get()
        rank = entry_rank.get()
        division = entry_division.get()
        join_date = entry_join_date.get()
        positions_held = entry_positions_held.get()
        strike_suspension = entry_strike_suspension.get()
        previous_names = entry_previous_names.get()
        discord = entry_discord.get()
        timezone = entry_timezone.get()
        country = entry_country.get()

        bbcode = f"""
    [TABLE="class: grid, width: 600, align: center"][TR="bgcolor: #e9e9e9"][TD][CENTER][IMG]https://imgur.com/f5RxrTm.png[/IMG][/CENTER]
    [TABLE="width: 600, align: center"]
    [TR]
    [TD][right][IMG]https://i.imgur.com/feN27Ql.png[/IMG][/right][/TD] [TD][center][TABLE="width: 430, align: center"][TR][TD]  [COLOR=#000000][FONT=Arial][SIZE=5][FONT=Century Gothic][B]LOS SANTOS[/B][/FONT][/SIZE][/FONT][/COLOR]
    [COLOR=#ff1818][FONT=Arial][SIZE=5][FONT=Microsoft Sans Serif][B]FIRE & MEDICAL DEPARTMENT[/B][/FONT][/SIZE][/FONT][/COLOR][/TD][/TR][TR][TD] [/TD][/TR][TR][TD][COLOR=#000000][FONT=century gothic][SIZE=4][FONT=Microsoft Sans Serif][B]PARAMEDIC PROFILE[/B][/FONT][/SIZE][/FONT][/COLOR][/TD][/TR][/TABLE][/TD][/TR][/center][/TABLE]
    [FONT=Courier New][COLOR="#000000"][SIZE=3]
    [CENTER][FONT=Verdana][COLOR="#920000"][SIZE=4][B]Personal Information[/B][/SIZE][/COLOR][/FONT][/CENTER]
    [TABLE="width: 590, align: center"][TR][TD]
    [FONT=Arial][B]Name:[/B][/FONT][INDENT][B]{name}[/B][/INDENT][FONT=Arial][B]Rank:[/B][/FONT][INDENT][B]{rank}[/B][/INDENT][FONT=Arial][B]Division:[/B][/FONT][INDENT][B]{division}[/B][/INDENT][FONT=Arial][B]Join / Reinstate Date:[/B][/FONT][INDENT][B]{join_date}[/B][/INDENT][FONT=Arial][B]Positions Held:[/B][/FONT][INDENT][B]{positions_held}[/B][/INDENT][FONT=Arial][B]Strike / Suspension:[/B][/FONT][INDENT][B]{strike_suspension}[/B][/INDENT][/TD]
    [TD]
    [RIGHT][IMG]{tasveer}[/IMG][/RIGHT]
    [/TD][/TR][/TABLE]
    [CENTER][FONT=Verdana][COLOR="#920000"][SIZE=4][B]Additional Information ((OOC))[/B][/SIZE][/COLOR][/FONT][/CENTER]
    [TABLE="width: 590, align: center"][TR][TD]
    [FONT=Arial][B]Previous Names:[/B][/FONT][INDENT][B]{previous_names}[/B][/INDENT][FONT=Arial][B]Discord:[/B][/FONT][INDENT][B]{discord}[/B][/INDENT][FONT=Arial][B]Timezone:[/B][/FONT][INDENT][B]{timezone}[/B][/INDENT][FONT=Arial][B]Country:[/B][/FONT][INDENT][B]{country}[/B][/INDENT][/TD][/TR][/TABLE]
    [CENTER][FONT=Verdana][COLOR="#920000"][SIZE=4][B]Achievements[/B][/SIZE][/COLOR][/FONT][/CENTER]
    [TABLE="width: 600, align: center, class:grid"]
    [TR][TD]Award Name[/TD][TD]Description[/TD][/TR]
    [/TABLE]
    [/SIZE][/COLOR][/FONT]
    [CENTER][IMG]https://imgur.com/bMNEx6b.png[/IMG][/CENTER]
    [/TD][/TR][/TABLE]
    """
        copy_to_clipboard(bbcode)
        messagebox.showinfo("Success", "BBCode copied to clipboard!")
        root.destroy()

    root = tk.Tk()
    root.title("Main Profile Form")
    root.geometry("400x600")
    root.grab_set()

    # Caption
    caption = tk.Label(root, text="Fill your details here", font=("Arial", 14, "bold"))
    caption.pack(pady=10)

    # Personal Information section
    label_personal_info = tk.Label(root, text="Personal Information", font=("Arial", 12, "bold"))
    label_personal_info.pack(pady=10)

    label_name = tk.Label(root, text="Name:")
    label_name.pack()
    entry_name = tk.Entry(root)
    entry_name.pack()

    label_rank = tk.Label(root, text="Rank:")
    label_rank.pack()
    entry_rank = tk.Entry(root)
    entry_rank.pack()

    label_division = tk.Label(root, text="Division:")
    label_division.pack()
    entry_division = tk.Entry(root)
    entry_division.pack()

    label_join_date = tk.Label(root, text="Join / Reinstate Date:")
    label_join_date.pack()
    entry_join_date = tk.Entry(root)
    entry_join_date.pack()

    label_positions_held = tk.Label(root, text="Positions Held:")
    label_positions_held.pack()
    entry_positions_held = tk.Entry(root)
    entry_positions_held.pack()

    label_strike_suspension = tk.Label(root, text="Strike / Suspension:")
    label_strike_suspension.pack()
    entry_strike_suspension = tk.Entry(root)
    entry_strike_suspension.pack()

    # Additional Information section
    label_additional_info = tk.Label(root, text="Additional Information ((OOC))", font=("Arial", 12, "bold"))
    label_additional_info.pack(pady=10)

    label_previous_names = tk.Label(root, text="Previous Names:")
    label_previous_names.pack()
    entry_previous_names = tk.Entry(root)
    entry_previous_names.pack()

    label_discord = tk.Label(root, text="Discord:")
    label_discord.pack()
    entry_discord = tk.Entry(root)
    entry_discord.pack()

    label_timezone = tk.Label(root, text="Timezone:")
    label_timezone.pack()
    entry_timezone = tk.Entry(root)
    entry_timezone.pack()

    label_country = tk.Label(root, text="Country:")
    label_country.pack()
    entry_country = tk.Entry(root)
    entry_country.pack()

    # Submit button
    btn_submit = tk.Button(root, text="Submit", command=submit_form)
    btn_submit.pack(pady=10)

    root.mainloop()

    pass

if __name__ == "__main__":
    main()
