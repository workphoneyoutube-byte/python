# Build Office 365 Software Clone
# A simple clone featuring Word, Excel, and PowerPoint-like applications

import os
import json
import datetime

class Office365:
    """Main application launcher for Office 365 clone"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.user = os.getlogin()
        self.documents_path = "/home/regular/Documents/repos/office_docs/"
        self._ensure_docs_folder()
    
    def _ensure_docs_folder(self):
        """Create documents folder if it doesn't exist"""
        if not os.path.exists(self.documents_path):
            os.makedirs(self.documents_path)
    
    def display_header(self):
        """Display application header"""
        print("\n" + "=" * 60)
        print(f"{'OFFICE 365 CLONE':^60}")
        print(f"{'Version ' + self.version:^60}")
        print(f"{'User: ' + self.user:^60}")
        print("=" * 60)
    
    def main_menu(self):
        """Display main menu and handle user choice"""
        while True:
            self.display_header()
            print("\nSelect an application:")
            print("1. Word (Text Processor)")
            print("2. Excel (Spreadsheet)")
            print("3. PowerPoint (Presentation)")
            print("4. File Manager")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                WordProcessor(self.documents_path).run()
            elif choice == '2':
                Spreadsheet(self.documents_path).run()
            elif choice == '3':
                Presentation(self.documents_path).run()
            elif choice == '4':
                FileManager(self.documents_path).run()
            elif choice == '5':
                print("\nThank you for using Office 365 Clone!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")


class WordProcessor:
    """Word processor application (like Microsoft Word)"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.content = []
        self.filename = None
        self.metadata = {
            'created': str(datetime.datetime.now()),
            'modified': str(datetime.datetime.now()),
            'author': os.getlogin()
        }
    
    def run(self):
        """Main word processor interface"""
        while True:
            print("\n" + "=" * 60)
            print(f"{'WORD PROCESSOR':^60}")
            print("=" * 60)
            print("\n1. New Document")
            print("2. Open Document")
            print("3. Edit Current Document")
            print("4. Save Document")
            print("5. Display Document")
            print("6. Document Statistics")
            print("7. Back to Main Menu")
            
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                self.new_document()
            elif choice == '2':
                self.open_document()
            elif choice == '3':
                self.edit_document()
            elif choice == '4':
                self.save_document()
            elif choice == '5':
                self.display_document()
            elif choice == '6':
                self.show_statistics()
            elif choice == '7':
                break
            else:
                print("Invalid choice.")
    
    def new_document(self):
        """Create a new document"""
        self.content = []
        self.filename = None
        self.metadata['created'] = str(datetime.datetime.now())
        print("\nNew document created. Use 'Edit Current Document' to add content.")
    
    def edit_document(self):
        """Edit document content"""
        print("\n--- DOCUMENT EDITOR ---")
        print("Type your content (one line at a time)")
        print("Type 'DONE' on a new line when finished")
        print("Type 'CLEAR' to clear all content\n")
        
        while True:
            line = input()
            if line.upper() == 'DONE':
                break
            elif line.upper() == 'CLEAR':
                self.content = []
                print("Content cleared.")
            else:
                self.content.append(line)
        
        self.metadata['modified'] = str(datetime.datetime.now())
        print(f"\nDocument updated. Total lines: {len(self.content)}")
    
    def save_document(self):
        """Save document to file"""
        if not self.content:
            print("\nNo content to save.")
            return
        
        if not self.filename:
            self.filename = input("Enter filename (without extension): ") + ".docx"
        
        filepath = os.path.join(self.docs_path, self.filename)
        
        doc_data = {
            'content': self.content,
            'metadata': self.metadata
        }
        
        with open(filepath, 'w') as f:
            json.dump(doc_data, f, indent=2)
        
        print(f"\nDocument saved as: {self.filename}")
    
    def open_document(self):
        """Open an existing document"""
        filename = input("Enter filename (with .docx extension): ")
        filepath = os.path.join(self.docs_path, filename)
        
        try:
            with open(filepath, 'r') as f:
                doc_data = json.load(f)
            
            self.content = doc_data['content']
            self.metadata = doc_data['metadata']
            self.filename = filename
            print(f"\nDocument '{filename}' opened successfully.")
        except FileNotFoundError:
            print(f"\nFile '{filename}' not found.")
        except json.JSONDecodeError:
            print("\nError reading file.")
    
    def display_document(self):
        """Display current document"""
        if not self.content:
            print("\nNo content to display.")
            return
        
        print("\n" + "-" * 60)
        print(f"Document: {self.filename or 'Untitled'}")
        print("-" * 60)
        for line in self.content:
            print(line)
        print("-" * 60)
    
    def show_statistics(self):
        """Show document statistics"""
        if not self.content:
            print("\nNo content to analyze.")
            return
        
        text = ' '.join(self.content)
        word_count = len(text.split())
        char_count = len(text)
        line_count = len(self.content)
        
        print("\n--- DOCUMENT STATISTICS ---")
        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
        print(f"Created: {self.metadata['created']}")
        print(f"Modified: {self.metadata['modified']}")
        print(f"Author: {self.metadata['author']}")


class Spreadsheet:
    """Spreadsheet application (like Microsoft Excel)"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.data = {}  # {row: {col: value}}
        self.filename = None
        self.rows = 10
        self.cols = 5
    
    def run(self):
        """Main spreadsheet interface"""
        while True:
            print("\n" + "=" * 60)
            print(f"{'SPREADSHEET':^60}")
            print("=" * 60)
            print("\n1. New Spreadsheet")
            print("2. Open Spreadsheet")
            print("3. Edit Cell")
            print("4. Display Spreadsheet")
            print("5. Calculate Column Sum")
            print("6. Save Spreadsheet")
            print("7. Back to Main Menu")
            
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                self.new_spreadsheet()
            elif choice == '2':
                self.open_spreadsheet()
            elif choice == '3':
                self.edit_cell()
            elif choice == '4':
                self.display_spreadsheet()
            elif choice == '5':
                self.calculate_sum()
            elif choice == '6':
                self.save_spreadsheet()
            elif choice == '7':
                break
            else:
                print("Invalid choice.")
    
    def new_spreadsheet(self):
        """Create new spreadsheet"""
        self.data = {}
        self.filename = None
        print("\nNew spreadsheet created.")
    
    def edit_cell(self):
        """Edit a cell value"""
        try:
            row = int(input("Enter row number (0-9): "))
            col = int(input("Enter column number (0-4): "))
            value = input("Enter value: ")
            
            if row not in self.data:
                self.data[row] = {}
            
            self.data[row][col] = value
            print(f"\nCell [{row},{col}] updated.")
        except ValueError:
            print("\nInvalid input.")
    
    def display_spreadsheet(self):
        """Display spreadsheet grid"""
        print("\n" + "-" * 60)
        print("   ", end="")
        for col in range(self.cols):
            print(f"  Col{col}  ", end="")
        print("\n" + "-" * 60)
        
        for row in range(self.rows):
            print(f"{row:2d} |", end="")
            for col in range(self.cols):
                value = self.data.get(row, {}).get(col, "")
                print(f"{str(value):^9}|", end="")
            print()
        print("-" * 60)
    
    def calculate_sum(self):
        """Calculate sum of a column"""
        try:
            col = int(input("Enter column number to sum (0-4): "))
            total = 0
            count = 0
            
            for row in range(self.rows):
                value = self.data.get(row, {}).get(col, "")
                if value:
                    try:
                        total += float(value)
                        count += 1
                    except ValueError:
                        pass
            
            print(f"\nColumn {col} Sum: {total}")
            print(f"Count: {count}")
            if count > 0:
                print(f"Average: {total/count:.2f}")
        except ValueError:
            print("\nInvalid input.")
    
    def save_spreadsheet(self):
        """Save spreadsheet to file"""
        if not self.filename:
            self.filename = input("Enter filename (without extension): ") + ".xlsx"
        
        filepath = os.path.join(self.docs_path, self.filename)
        
        with open(filepath, 'w') as f:
            json.dump(self.data, f, indent=2)
        
        print(f"\nSpreadsheet saved as: {self.filename}")
    
    def open_spreadsheet(self):
        """Open existing spreadsheet"""
        filename = input("Enter filename (with .xlsx extension): ")
        filepath = os.path.join(self.docs_path, filename)
        
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            # Convert string keys back to integers
            self.data = {int(k): {int(k2): v2 for k2, v2 in v.items()} 
                        for k, v in data.items()}
            self.filename = filename
            print(f"\nSpreadsheet '{filename}' opened successfully.")
        except FileNotFoundError:
            print(f"\nFile '{filename}' not found.")
        except json.JSONDecodeError:
            print("\nError reading file.")


class Presentation:
    """Presentation application (like Microsoft PowerPoint)"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.slides = []
        self.filename = None
    
    def run(self):
        """Main presentation interface"""
        while True:
            print("\n" + "=" * 60)
            print(f"{'PRESENTATION':^60}")
            print("=" * 60)
            print("\n1. New Presentation")
            print("2. Open Presentation")
            print("3. Add Slide")
            print("4. Edit Slide")
            print("5. View All Slides")
            print("6. View Specific Slide")
            print("7. Delete Slide")
            print("8. Save Presentation")
            print("9. Back to Main Menu")
            
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                self.new_presentation()
            elif choice == '2':
                self.open_presentation()
            elif choice == '3':
                self.add_slide()
            elif choice == '4':
                self.edit_slide()
            elif choice == '5':
                self.view_all_slides()
            elif choice == '6':
                self.view_slide()
            elif choice == '7':
                self.delete_slide()
            elif choice == '8':
                self.save_presentation()
            elif choice == '9':
                break
            else:
                print("Invalid choice.")
    
    def new_presentation(self):
        """Create new presentation"""
        self.slides = []
        self.filename = None
        print("\nNew presentation created.")
    
    def add_slide(self):
        """Add a new slide"""
        print("\n--- NEW SLIDE ---")
        title = input("Enter slide title: ")
        content = []
        
        print("Enter slide content (one line at a time, type 'DONE' when finished):")
        while True:
            line = input()
            if line.upper() == 'DONE':
                break
            content.append(line)
        
        slide = {
            'title': title,
            'content': content,
            'created': str(datetime.datetime.now())
        }
        
        self.slides.append(slide)
        print(f"\nSlide {len(self.slides)} added.")
    
    def edit_slide(self):
        """Edit an existing slide"""
        if not self.slides:
            print("\nNo slides to edit.")
            return
        
        try:
            slide_num = int(input(f"Enter slide number (1-{len(self.slides)}): "))
            if 1 <= slide_num <= len(self.slides):
                slide = self.slides[slide_num - 1]
                
                print(f"\nCurrent title: {slide['title']}")
                new_title = input("Enter new title (or press Enter to keep current): ")
                if new_title:
                    slide['title'] = new_title
                
                print("\nUpdate content? (y/n): ", end="")
                if input().lower() == 'y':
                    content = []
                    print("Enter new content (type 'DONE' when finished):")
                    while True:
                        line = input()
                        if line.upper() == 'DONE':
                            break
                        content.append(line)
                    slide['content'] = content
                
                print(f"\nSlide {slide_num} updated.")
            else:
                print("\nInvalid slide number.")
        except ValueError:
            print("\nInvalid input.")
    
    def view_all_slides(self):
        """View all slides in presentation"""
        if not self.slides:
            print("\nNo slides to display.")
            return
        
        print(f"\n{'='*60}")
        print(f"Total Slides: {len(self.slides)}")
        print(f"{'='*60}")
        
        for i, slide in enumerate(self.slides, 1):
            self._display_slide(i, slide)
    
    def view_slide(self):
        """View a specific slide"""
        if not self.slides:
            print("\nNo slides to display.")
            return
        
        try:
            slide_num = int(input(f"Enter slide number (1-{len(self.slides)}): "))
            if 1 <= slide_num <= len(self.slides):
                self._display_slide(slide_num, self.slides[slide_num - 1])
            else:
                print("\nInvalid slide number.")
        except ValueError:
            print("\nInvalid input.")
    
    def _display_slide(self, num, slide):
        """Helper method to display a slide"""
        print(f"\n{'='*60}")
        print(f"Slide {num}: {slide['title']}")
        print(f"{'='*60}")
        for line in slide['content']:
            print(f"  {line}")
        print(f"{'='*60}")
    
    def delete_slide(self):
        """Delete a slide"""
        if not self.slides:
            print("\nNo slides to delete.")
            return
        
        try:
            slide_num = int(input(f"Enter slide number to delete (1-{len(self.slides)}): "))
            if 1 <= slide_num <= len(self.slides):
                confirm = input(f"Delete slide {slide_num}? (y/n): ")
                if confirm.lower() == 'y':
                    self.slides.pop(slide_num - 1)
                    print(f"\nSlide {slide_num} deleted.")
            else:
                print("\nInvalid slide number.")
        except ValueError:
            print("\nInvalid input.")
    
    def save_presentation(self):
        """Save presentation to file"""
        if not self.slides:
            print("\nNo slides to save.")
            return
        
        if not self.filename:
            self.filename = input("Enter filename (without extension): ") + ".pptx"
        
        filepath = os.path.join(self.docs_path, self.filename)
        
        with open(filepath, 'w') as f:
            json.dump(self.slides, f, indent=2)
        
        print(f"\nPresentation saved as: {self.filename}")
    
    def open_presentation(self):
        """Open existing presentation"""
        filename = input("Enter filename (with .pptx extension): ")
        filepath = os.path.join(self.docs_path, filename)
        
        try:
            with open(filepath, 'r') as f:
                self.slides = json.load(f)
            
            self.filename = filename
            print(f"\nPresentation '{filename}' opened successfully.")
            print(f"Total slides: {len(self.slides)}")
        except FileNotFoundError:
            print(f"\nFile '{filename}' not found.")
        except json.JSONDecodeError:
            print("\nError reading file.")


class FileManager:
    """File manager for Office documents"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
    
    def run(self):
        """Main file manager interface"""
        while True:
            print("\n" + "=" * 60)
            print(f"{'FILE MANAGER':^60}")
            print("=" * 60)
            print("\n1. List All Files")
            print("2. Delete File")
            print("3. Rename File")
            print("4. File Information")
            print("5. Back to Main Menu")
            
            choice = input("\nEnter your choice: ")
            
            if choice == '1':
                self.list_files()
            elif choice == '2':
                self.delete_file()
            elif choice == '3':
                self.rename_file()
            elif choice == '4':
                self.file_info()
            elif choice == '5':
                break
            else:
                print("Invalid choice.")
    
    def list_files(self):
        """List all files in documents folder"""
        try:
            files = os.listdir(self.docs_path)
            if not files:
                print("\nNo files found.")
                return
            
            print("\n--- FILES IN DOCUMENTS FOLDER ---")
            for i, file in enumerate(files, 1):
                filepath = os.path.join(self.docs_path, file)
                size = os.path.getsize(filepath)
                print(f"{i}. {file} ({size} bytes)")
        except Exception as e:
            print(f"\nError listing files: {e}")
    
    def delete_file(self):
        """Delete a file"""
        filename = input("Enter filename to delete: ")
        filepath = os.path.join(self.docs_path, filename)
        
        try:
            if os.path.exists(filepath):
                confirm = input(f"Delete '{filename}'? (y/n): ")
                if confirm.lower() == 'y':
                    os.remove(filepath)
                    print(f"\nFile '{filename}' deleted.")
            else:
                print(f"\nFile '{filename}' not found.")
        except Exception as e:
            print(f"\nError deleting file: {e}")
    
    def rename_file(self):
        """Rename a file"""
        old_name = input("Enter current filename: ")
        new_name = input("Enter new filename: ")
        
        old_path = os.path.join(self.docs_path, old_name)
        new_path = os.path.join(self.docs_path, new_name)
        
        try:
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f"\nFile renamed from '{old_name}' to '{new_name}'.")
            else:
                print(f"\nFile '{old_name}' not found.")
        except Exception as e:
            print(f"\nError renaming file: {e}")
    
    def file_info(self):
        """Display file information"""
        filename = input("Enter filename: ")
        filepath = os.path.join(self.docs_path, filename)
        
        try:
            if os.path.exists(filepath):
                stats = os.stat(filepath)
                print("\n--- FILE INFORMATION ---")
                print(f"Name: {filename}")
                print(f"Size: {stats.st_size} bytes")
                print(f"Created: {datetime.datetime.fromtimestamp(stats.st_ctime)}")
                print(f"Modified: {datetime.datetime.fromtimestamp(stats.st_mtime)}")
            else:
                print(f"\nFile '{filename}' not found.")
        except Exception as e:
            print(f"\nError getting file info: {e}")


# Main entry point
if __name__ == "__main__":
    app = Office365()
    app.main_menu()