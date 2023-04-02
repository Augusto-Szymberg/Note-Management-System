import os
import tkinter as tk
from tkinter import messagebox

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def create(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def read(self, title):
        for note in self.notes:
            if note.title == title:
                return note.content
        return None

    def update(self, title, content):
        for note in self.notes:
            if note.title == title:
                note.content = content
                return True
        return False

    def delete(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return True
        return False

def main():
    def create_note():
        title = entry_title.get()
        content = text_content.get("1.0", tk.END)
        if title:
            note_manager.create(title, content)
            entry_title.delete(0, tk.END)
            text_content.delete("1.0", tk.END)
            update_note_list()
            messagebox.showinfo("Success", "Note created successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a title for the note.")

    def read_note():
        title = note_listbox.get(note_listbox.curselection())
        content = note_manager.read(title)
        if content:
            entry_title.delete(0, tk.END)
            entry_title.insert(0, title)
            text_content.delete("1.0", tk.END)
            text_content.insert(tk.END, content)
        else:
            messagebox.showerror("Error", "Note not found.")

    def update_note():
        title = entry_title.get()
        content = text_content.get("1.0", tk.END)
        if note_manager.update(title, content):
            update_note_list()
            messagebox.showinfo("Success", "Note updated successfully.")
        else:
            messagebox.showerror("Error", "Note not found.")

    def delete_note():
        title = entry_title.get()
        if note_manager.delete(title):
            entry_title.delete(0, tk.END)
            text_content.delete("1.0", tk.END)
            update_note_list()
            messagebox.showinfo("Success", "Note deleted successfully.")
        else:
            messagebox.showerror("Error", "Note not found.")

    def update_note_list():
        note_listbox.delete(0, tk.END)
        for note in note_manager.notes:
            note_listbox.insert(tk.END, note.title)

    def on_note_selected(event):
        read_note()

    note_manager = NoteManager()

    root = tk.Tk()
    root.title("Note Management System")

    note_listbox = tk.Listbox(root, width=30, height=20, selectmode=tk.SINGLE)
    note_listbox.grid(row=0, column=0, rowspan=3, padx=10, pady=10)
    note_listbox.bind("<<ListboxSelect>>", on_note_selected)
    update_note_list()

    tk.Label(root, text="Title:").grid(row=0, column=1, padx=10, pady=10, sticky="e")
    entry_title = tk.Entry(root, width=40)
    entry_title.grid(row=0, column=2, padx=10, pady=10)

    tk.Label(root, text="Content:").grid(row=1, column=1, padx=10, pady=10, sticky="ne")
    text_content = tk.Text(root, width=60, height=20, wrap=tk.WORD)
    text_content.grid(row=1, column=2, padx=10, pady=10)

    button_frame = tk.Frame(root)
    button_frame.grid(row=2, column=1, columnspan=2, pady=10)

    tk.Button(button_frame, text="Create", command=create_note, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Update", command=update_note, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Delete", command=delete_note, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Quit", command=root.quit, width=10).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()