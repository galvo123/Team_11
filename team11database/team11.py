import sqlite3
#single tier
def create_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_note(title, content):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    print("Note added successfully!")

def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    print("Note deleted successfully!")

def display_notes():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    conn.close()
    
    if notes:
        for note in notes:
            print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}")
    else:
        print("No notes found.")

if __name__ == "__main__":
    create_db()
    while True:
        print("\n1. Add Note\n2. Delete Note\n3. Display Notes\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)
        elif choice == "2":
            note_id = input("Enter note ID to delete: ")
            delete_note(note_id)
        elif choice == "3":
            display_notes()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")
