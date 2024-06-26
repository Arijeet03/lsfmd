import tkinter as tk
from tkinter import messagebox
import ctypes

def main():

    def copy_to_clipboard(text):
        ctypes.windll.user32.OpenClipboard(0)
        ctypes.windll.user32.EmptyClipboard()
        ctypes.windll.user32.SetClipboardData(1, ctypes.create_string_buffer(text.encode("utf-8")))
        ctypes.windll.user32.CloseClipboard()

    def submit_form():
        name_upd = entry_name_upd.get()
        dou = entry_dou.get()
        approvedby = entry_approvedby.get()
        updatedinfo = entry_updatedinfo.get()
        addinfo = entry_addinfo.get()

        bbcode = f"""
    [table="width: 600, class: outer_border, align: center"]
    [tr=bgcolor:#ff6b6b][td]
    [table="width: 600, align: center"]
    [tr][td][LEFT][url=https://forums.hzgaming.net/forumdisplay.php/48-Los-Santos-Fire-amp-Medical-Department-(LSFMD)][img]https://i.imgur.com/zDvW3zn.png[/img][/url][/LEFT][/td][/tr]
    [tr][td]  [/td][/tr]
    [tr][td][table="width: 600, align: center"][tr][td][LEFT][img]https://i.imgur.com/i7g9Mrn.png[/img][/LEFT][/td][td]      [/td][td][LEFT][url=https://forums.hzgaming.net/forumdisplay.php/63-Recruitment-Office][img]https://i.imgur.com/75k1XOq.png[/img][/url][/LEFT][/td][td]      [/td][td][LEFT][url=https://forums.hzgaming.net/showthread.php/485784-LSFMD-Employee-Roster][img]https://i.imgur.com/AIGEiCw.png[/img][/url][/LEFT][/td][td]      [/td][td][LEFT][url=https://forums.hzgaming.net/forumdisplay.php/2193-Employee-Complaints][img]https://i.imgur.com/Mg30cLR.png[/img][/url][/LEFT][/td][td]      [/td][td][LEFT][url=https://forums.hzgaming.net/forumdisplay.php/758-Public-Relations-Office][img]https://i.imgur.com/L5mU7u6.png[/img][/url][/LEFT][/td][/tr][/table][/td][/tr][/table][/td][/tr][tr=bgcolor:#0f0f0f]
    [td]
    [LEFT][SIZE=1][SIZE=1][B][COLOR=#FFC0CB]Chief [/COLOR] [COLOR=white]Saksham Slash [/COLOR][/B][/SIZE]
    [COLOR=white][FONT=Century Gothic][I]San Andreas,
    Los Santos International,
    LSFMD Headquarters[/I][/FONT][/COLOR]
    [/SIZE][/LEFT]
    [TABLE="width: 600, align: center"]
    [TR]
    [TD][left][IMG]https://i.imgur.com/feN27Ql.png[/IMG][/left][/TD] [TD][center][TABLE="width: 430, align: center"][TR][TD]  [COLOR=#FFC0CB][FONT=Arial][SIZE=5][B][FONT=Microsoft Sans Serif]LOS SANTOS FIRE & MEDICAL DEPARTMENT[/FONT][/B][/SIZE][/FONT][/COLOR][/TD][/TR][TR][TD] [/TD][/TR][TR][TD][COLOR=#FFF0F5][FONT=century gothic][SIZE=5][B][FONT=Microsoft Sans Serif]EMPLOYEE UPDATE[/FONT][/B][/SIZE][/FONT][/COLOR][/TD][/TR][/TABLE][/TD][/TR][/center][/TABLE][center][/center][TABLE="width: 550, align: center"][TR][TD][LEFT][COLOR=#ffffff][FONT=Century Gothic][size=2]

    [B][COLOR=#ffcccc] Employee Name: [/COLOR][/B][I]{name_upd}                                                                  [/I]
    [B][COLOR=#ffcccc] Date of Update: [/COLOR][/B][I]{dou}                                                              [/I]
    [B][COLOR=#ffcccc] Approved by: [/COLOR][/B][COLOR=#ffcccc][/COLOR][I]{approvedby}                                                                          [/I]
    [B][COLOR=#ffcccc] Updated Information: [/COLOR][/B][COLOR=#ffcccc][/COLOR][I]{updatedinfo}[/I]
    [B][COLOR=#ffcccc] Additional Information: [/COLOR][/B][COLOR=#ffcccc][/COLOR][I]{addinfo}                                                         [/I]

    [/SIZE][/FONT][/COLOR][/LEFT]


    [/TD][/TR][/TABLE][/TD][/TR][/TABLE]
    """
        copy_to_clipboard(bbcode)
        messagebox.showinfo("Success", "BBCode copied to clipboard!")
        root.destroy()

    root = tk.Tk()
    root.title("Employee Update Form")
    root.geometry("400x600")
    root.grab_set()

    # Caption
    caption = tk.Label(root, text="Fill your details here", font=("Arial", 14, "bold"))
    caption.pack(pady=10)

    # Form fields
    label_name_upd = tk.Label(root, text="Name:")
    label_name_upd.pack()
    entry_name_upd = tk.Entry(root)
    entry_name_upd.pack()

    label_dou = tk.Label(root, text="Date of Update:")
    label_dou.pack()
    entry_dou = tk.Entry(root)
    entry_dou.pack()

    label_approvedby = tk.Label(root, text="Approved By:")
    label_approvedby.pack()
    entry_approvedby = tk.Entry(root)
    entry_approvedby.pack()

    label_updatedinfo = tk.Label(root, text="Updated Information:")
    label_updatedinfo.pack()
    entry_updatedinfo = tk.Entry(root)
    entry_updatedinfo.pack()

    label_addinfo = tk.Label(root, text="Additional Information:")
    label_addinfo.pack()
    entry_addinfo = tk.Entry(root)
    entry_addinfo.pack()

    # Submit button
    btn_submit = tk.Button(root, text="Submit", command=submit_form)
    btn_submit.pack(pady=10)

    root.mainloop()

    pass

if __name__ == "__main__":
    main()