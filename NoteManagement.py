import os

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
    note_manager = NoteManager()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Note Management System")
        print("1. Create Note")
        print("2. Read Note")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. See Notes")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_manager.create(title, content)
            print("Note created successfully.")
        elif choice == '2':
            title = input("Enter note title: ")
            content = note_manager.read(title)
            if content:
                print(f"Content: {content}")
            else:
                print("Note not found.")
        elif choice == '3':
            title = input("Enter note title: ")
            content = input("Enter new content: ")
            if note_manager.update(title, content):
                print("Note updated successfully.")
            else:
                print("Note not found.")
        elif choice == '4':
            title = input("Enter note title: ")
            if note_manager.delete(title):
                print("Note deleted successfully.")
            else:
                print("Note not found.")
        elif choice == '5':
            print("Available Notes:")
            if not note_manager.notes:
                print("No notes available.")
            else:
                for note in note_manager.notes:
                    print(f"- {note.title}")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
