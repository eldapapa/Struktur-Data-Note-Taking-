"""
====================================================
NOTE-TAKING APP DATA STRUCTURE
====================================================

Fitur:
1. Multiple tags per note
   -> Multi Linked List

2. Chronological & Alphabetical Views
   -> Doubly Linked List

3. Sync status tracking
   -> Circular Buffer

Author : Maulana Daffa Wibowo
====================================================
"""

from collections import deque
from datetime import datetime


# ====================================================
# NOTE CLASS
# ====================================================

class Note:
    def __init__(self, note_id, title, content):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.created_at = datetime.now()

        # Multi tags
        self.tags = []

        # Doubly linked chronological
        self.prev_chrono = None
        self.next_chrono = None

        # Doubly linked alphabetical
        self.prev_alpha = None
        self.next_alpha = None

    def __str__(self):
        return f"[{self.note_id}] {self.title}"


# ====================================================
# TAG CLASS (MULTI LINKED LIST)
# ====================================================

class Tag:
    def __init__(self, name):
        self.name = name
        self.notes = []

    def add_note(self, note):
        if note not in self.notes:
            self.notes.append(note)

    def show_notes(self):
        print(f"\nTag: {self.name}")
        for note in self.notes:
            print("-", note.title)


# ====================================================
# CIRCULAR BUFFER FOR SYNC LOG
# ====================================================

class CircularBuffer:
    def __init__(self, size=5):
        self.buffer = deque(maxlen=size)

    def add_log(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.buffer.append(f"{timestamp} -> {action}")

    def show_logs(self):
        print("\n=== RECENT SYNC LOGS ===")
        for log in self.buffer:
            print(log)


# ====================================================
# NOTE MANAGER
# ====================================================

class NoteManager:
    def __init__(self):

        # Store all notes
        self.notes = []

        # Store all tags
        self.tags = {}

        # Circular buffer
        self.sync_logs = CircularBuffer()

        # Head doubly linked lists
        self.chrono_head = None
        self.alpha_head = None

    # ==========================================
    # ADD NOTE
    # ==========================================
    def add_note(self, note_id, title, content, tag_names):

        note = Note(note_id, title, content)

        # Add tags
        for tag_name in tag_names:

            if tag_name not in self.tags:
                self.tags[tag_name] = Tag(tag_name)

            tag = self.tags[tag_name]

            tag.add_note(note)
            note.tags.append(tag_name)

        # Add to notes list
        self.notes.append(note)

        # Insert chronological
        self.insert_chronological(note)

        # Insert alphabetical
        self.insert_alphabetical(note)

        # Add sync log
        self.sync_logs.add_log(f"Added note '{title}'")

    # ==========================================
    # CHRONOLOGICAL LINKED LIST
    # ==========================================
    def insert_chronological(self, note):

        if self.chrono_head is None:
            self.chrono_head = note
            return

        current = self.chrono_head

        while current.next_chrono:
            current = current.next_chrono

        current.next_chrono = note
        note.prev_chrono = current

    # ==========================================
    # ALPHABETICAL LINKED LIST
    # ==========================================
    def insert_alphabetical(self, note):

        if self.alpha_head is None:
            self.alpha_head = note
            return

        current = self.alpha_head
        previous = None

        while current and current.title.lower() < note.title.lower():
            previous = current
            current = current.next_alpha

        if previous is None:
            note.next_alpha = self.alpha_head
            self.alpha_head.prev_alpha = note
            self.alpha_head = note

        else:
            note.next_alpha = current
            note.prev_alpha = previous
            previous.next_alpha = note

            if current:
                current.prev_alpha = note

    # ==========================================
    # SHOW CHRONOLOGICAL
    # ==========================================
    def show_chronological(self):

        print("\n=== CHRONOLOGICAL VIEW ===")

        current = self.chrono_head

        while current:
            print(current)
            current = current.next_chrono

    # ==========================================
    # SHOW ALPHABETICAL
    # ==========================================
    def show_alphabetical(self):

        print("\n=== ALPHABETICAL VIEW ===")

        current = self.alpha_head

        while current:
            print(current)
            current = current.next_alpha

    # ==========================================
    # SHOW NOTES BY TAG
    # ==========================================
    def show_notes_by_tag(self, tag_name):

        if tag_name in self.tags:
            self.tags[tag_name].show_notes()
        else:
            print("Tag not found.")

    # ==========================================
    # SHOW ALL TAGS
    # ==========================================
    def show_all_tags(self):

        print("\n=== TAG LIST ===")

        for tag in self.tags:
            print("-", tag)

    # ==========================================
    # SHOW LOGS
    # ==========================================
    def show_sync_logs(self):
        self.sync_logs.show_logs()


# ====================================================
# MAIN PROGRAM
# ====================================================

if __name__ == "__main__":

    app = NoteManager()

    # Add notes
    app.add_note(
        1,
        "Struktur Data",
        "Belajar linked list",
        ["Kuliah", "Penting"]
    )

    app.add_note(
        2,
        "Basis Data",
        "Belajar normalisasi",
        ["Kuliah"]
    )

    app.add_note(
        3,
        "Tugas AI",
        "Kerjakan machine learning",
        ["Tugas", "Penting"]
    )

    # Show chronological
    app.show_chronological()

    # Show alphabetical
    app.show_alphabetical()

    # Show tag notes
    app.show_notes_by_tag("Penting")

    # Show logs
    app.show_sync_logs()
