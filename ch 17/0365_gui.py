# Office 365 Clone - GUI Version
# Graphical interface using tkinter

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog, filedialog
import os
import json
import datetime

class Office365GUI:
    """Main GUI launcher for Office 365 clone"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Office 365 Clone")
        self.root.geometry("800x600")
        self.version = "1.0.0"
        self.user = os.getlogin()
        self.documents_path = "/home/regular/Documents/repos/office_docs/"
        self._ensure_docs_folder()
        self._create_main_window()
    
    def _ensure_docs_folder(self):
        """Create documents folder if it doesn't exist"""
        if not os.path.exists(self.documents_path):
            os.makedirs(self.documents_path)
    
    def _create_main_window(self):
        """Create the main launcher window"""
        # Header
        header = tk.Frame(self.root, bg="#0078D4", height=100)
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text="Office 365 Clone", 
                              font=("Arial", 24, "bold"), 
                              bg="#0078D4", fg="white")
        title_label.pack(pady=20)
        
        version_label = tk.Label(header, text=f"Version {self.version} | User: {self.user}",
                                font=("Arial", 10), bg="#0078D4", fg="white")
        version_label.pack()
        
        # Main content area
        content = tk.Frame(self.root, bg="#F3F3F3")
        content.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        
        # Application buttons
        apps = [
            ("Word", "#2B579A", self.launch_word),
            ("Excel", "#217346", self.launch_excel),
            ("PowerPoint", "#D24726", self.launch_powerpoint),
            ("File Manager", "#7719AA", self.launch_file_manager)
        ]
        
        for i, (name, color, command) in enumerate(apps):
            row = i // 2
            col = i % 2
            
            btn = tk.Button(content, text=name, font=("Arial", 16, "bold"),
                          bg=color, fg="white", width=15, height=3,
                          command=command, cursor="hand2")
            btn.grid(row=row, column=col, padx=20, pady=20)
        
        # Exit button
        exit_btn = tk.Button(content, text="Exit", font=("Arial", 12),
                           bg="#D13438", fg="white", width=15,
                           command=self.root.quit)
        exit_btn.grid(row=2, column=0, columnspan=2, pady=20)
    
    def launch_word(self):
        WordProcessorGUI(self.documents_path)
    
    def launch_excel(self):
        SpreadsheetGUI(self.documents_path)
    
    def launch_powerpoint(self):
        PresentationGUI(self.documents_path)
    
    def launch_file_manager(self):
        FileManagerGUI(self.documents_path)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()


class WordProcessorGUI:
    """GUI Word Processor"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.window = tk.Toplevel()
        self.window.title("Word Processor")
        self.window.geometry("900x700")
        
        self.filename = None
        self.metadata = {
            'created': str(datetime.datetime.now()),
            'modified': str(datetime.datetime.now()),
            'author': os.getlogin()
        }
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create Word processor widgets"""
        # Menu bar
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_document)
        file_menu.add_command(label="Open", command=self.open_document)
        file_menu.add_command(label="Save", command=self.save_document)
        file_menu.add_command(label="Save As", command=self.save_as_document)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.window.destroy)
        
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Statistics", command=self.show_statistics)
        
        # Toolbar
        toolbar = tk.Frame(self.window, bg="#E1E1E1", height=40)
        toolbar.pack(fill=tk.X)
        
        tk.Button(toolbar, text="New", command=self.new_document).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Open", command=self.open_document).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Save", command=self.save_document).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Stats", command=self.show_statistics).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Status bar
        self.status_bar = tk.Label(self.window, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Text editor
        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, 
                                                    font=("Arial", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.update_status("New document")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=message)
    
    def new_document(self):
        """Create new document"""
        if self.text_area.get(1.0, tk.END).strip():
            if not messagebox.askyesno("New Document", "Discard current document?"):
                return
        
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.metadata['created'] = str(datetime.datetime.now())
        self.window.title("Word Processor - Untitled")
        self.update_status("New document created")
    
    def open_document(self):
        """Open existing document"""
        filepath = filedialog.askopenfilename(
            initialdir=self.docs_path,
            title="Open Document",
            filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
        )
        
        if filepath:
            try:
                with open(filepath, 'r') as f:
                    doc_data = json.load(f)
                
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, '\n'.join(doc_data['content']))
                self.metadata = doc_data['metadata']
                self.filename = os.path.basename(filepath)
                self.window.title(f"Word Processor - {self.filename}")
                self.update_status(f"Opened: {self.filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")
    
    def save_document(self):
        """Save document"""
        if not self.filename:
            self.save_as_document()
        else:
            self._save_to_file(os.path.join(self.docs_path, self.filename))
    
    def save_as_document(self):
        """Save document with new name"""
        filepath = filedialog.asksaveasfilename(
            initialdir=self.docs_path,
            title="Save Document As",
            defaultextension=".docx",
            filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
        )
        
        if filepath:
            self.filename = os.path.basename(filepath)
            self._save_to_file(filepath)
    
    def _save_to_file(self, filepath):
        """Save content to file"""
        content = self.text_area.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "No content to save")
            return
        
        self.metadata['modified'] = str(datetime.datetime.now())
        
        doc_data = {
            'content': content.split('\n'),
            'metadata': self.metadata
        }
        
        try:
            with open(filepath, 'w') as f:
                json.dump(doc_data, f, indent=2)
            
            self.window.title(f"Word Processor - {self.filename}")
            self.update_status(f"Saved: {self.filename}")
            messagebox.showinfo("Success", "Document saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def show_statistics(self):
        """Show document statistics"""
        content = self.text_area.get(1.0, tk.END).strip()
        
        if not content:
            messagebox.showinfo("Statistics", "No content to analyze")
            return
        
        words = len(content.split())
        chars = len(content)
        lines = len(content.split('\n'))
        
        stats = f"""Document Statistics:
        
Lines: {lines}
Words: {words}
Characters: {chars}

Created: {self.metadata['created']}
Modified: {self.metadata['modified']}
Author: {self.metadata['author']}"""
        
        messagebox.showinfo("Document Statistics", stats)


class SpreadsheetGUI:
    """GUI Spreadsheet Application"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.window = tk.Toplevel()
        self.window.title("Spreadsheet")
        self.window.geometry("1000x700")
        
        self.filename = None
        self.data = {}
        self.rows = 20
        self.cols = 10
        self.cells = {}
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create spreadsheet widgets"""
        # Menu bar
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_spreadsheet)
        file_menu.add_command(label="Open", command=self.open_spreadsheet)
        file_menu.add_command(label="Save", command=self.save_spreadsheet)
        file_menu.add_command(label="Save As", command=self.save_as_spreadsheet)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.window.destroy)
        
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Sum Column", command=self.sum_column)
        tools_menu.add_command(label="Clear All", command=self.clear_all)
        
        # Toolbar
        toolbar = tk.Frame(self.window, bg="#E1E1E1")
        toolbar.pack(fill=tk.X)
        
        tk.Button(toolbar, text="New", command=self.new_spreadsheet).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Open", command=self.open_spreadsheet).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Save", command=self.save_spreadsheet).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Sum Column", command=self.sum_column).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Status bar
        self.status_bar = tk.Label(self.window, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Spreadsheet grid with scrollbars
        container = tk.Frame(self.window)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(container)
        scrollbar_v = tk.Scrollbar(container, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_h = tk.Scrollbar(container, orient=tk.HORIZONTAL, command=canvas.xview)
        
        self.grid_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.grid_frame, anchor=tk.NW)
        
        canvas.configure(yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set)
        
        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create grid
        self._create_grid()
        
        self.grid_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        
        self.update_status("New spreadsheet")
    
    def _create_grid(self):
        """Create the spreadsheet grid"""
        # Column headers
        tk.Label(self.grid_frame, text="", width=3, relief=tk.RIDGE).grid(row=0, column=0)
        for col in range(self.cols):
            tk.Label(self.grid_frame, text=chr(65 + col), width=10, 
                    relief=tk.RIDGE, bg="#D0D0D0").grid(row=0, column=col + 1)
        
        # Rows
        for row in range(self.rows):
            # Row header
            tk.Label(self.grid_frame, text=str(row + 1), width=3, 
                    relief=tk.RIDGE, bg="#D0D0D0").grid(row=row + 1, column=0)
            
            # Cells
            for col in range(self.cols):
                cell = tk.Entry(self.grid_frame, width=10)
                cell.grid(row=row + 1, column=col + 1, padx=1, pady=1)
                self.cells[(row, col)] = cell
                
                # Load existing data
                if row in self.data and col in self.data[row]:
                    cell.insert(0, self.data[row][col])
    
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=message)
    
    def new_spreadsheet(self):
        """Create new spreadsheet"""
        if messagebox.askyesno("New Spreadsheet", "Clear all data?"):
            self.data = {}
            self.filename = None
            for cell in self.cells.values():
                cell.delete(0, tk.END)
            self.window.title("Spreadsheet - Untitled")
            self.update_status("New spreadsheet created")
    
    def _collect_data(self):
        """Collect data from cells"""
        self.data = {}
        for (row, col), cell in self.cells.items():
            value = cell.get().strip()
            if value:
                if row not in self.data:
                    self.data[row] = {}
                self.data[row][col] = value
    
    def save_spreadsheet(self):
        """Save spreadsheet"""
        if not self.filename:
            self.save_as_spreadsheet()
        else:
            self._save_to_file(os.path.join(self.docs_path, self.filename))
    
    def save_as_spreadsheet(self):
        """Save spreadsheet with new name"""
        filepath = filedialog.asksaveasfilename(
            initialdir=self.docs_path,
            title="Save Spreadsheet As",
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
        )
        
        if filepath:
            self.filename = os.path.basename(filepath)
            self._save_to_file(filepath)
    
    def _save_to_file(self, filepath):
        """Save to file"""
        self._collect_data()
        
        try:
            with open(filepath, 'w') as f:
                json.dump(self.data, f, indent=2)
            
            self.window.title(f"Spreadsheet - {self.filename}")
            self.update_status(f"Saved: {self.filename}")
            messagebox.showinfo("Success", "Spreadsheet saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def open_spreadsheet(self):
        """Open spreadsheet"""
        filepath = filedialog.askopenfilename(
            initialdir=self.docs_path,
            title="Open Spreadsheet",
            filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
        )
        
        if filepath:
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                self.data = {int(k): {int(k2): v2 for k2, v2 in v.items()} 
                           for k, v in data.items()}
                
                # Clear and populate cells
                for cell in self.cells.values():
                    cell.delete(0, tk.END)
                
                for row, cols in self.data.items():
                    for col, value in cols.items():
                        if (row, col) in self.cells:
                            self.cells[(row, col)].insert(0, value)
                
                self.filename = os.path.basename(filepath)
                self.window.title(f"Spreadsheet - {self.filename}")
                self.update_status(f"Opened: {self.filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open: {str(e)}")
    
    def sum_column(self):
        """Calculate sum of a column"""
        col_letter = simpledialog.askstring("Sum Column", "Enter column letter (A-J):")
        
        if col_letter:
            col_letter = col_letter.upper()
            if col_letter in 'ABCDEFGHIJ':
                col = ord(col_letter) - 65
                self._collect_data()
                
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
                
                result = f"Column {col_letter} Statistics:\n\nSum: {total}\nCount: {count}"
                if count > 0:
                    result += f"\nAverage: {total/count:.2f}"
                
                messagebox.showinfo("Column Sum", result)
            else:
                messagebox.showwarning("Invalid Input", "Please enter a letter from A to J")
    
    def clear_all(self):
        """Clear all cells"""
        if messagebox.askyesno("Clear All", "Clear all data?"):
            self.data = {}
            for cell in self.cells.values():
                cell.delete(0, tk.END)
            self.update_status("All data cleared")


class PresentationGUI:
    """GUI Presentation Application"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.window = tk.Toplevel()
        self.window.title("Presentation")
        self.window.geometry("900x700")
        
        self.filename = None
        self.slides = []
        self.current_slide = 0
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create presentation widgets"""
        # Menu bar
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_presentation)
        file_menu.add_command(label="Open", command=self.open_presentation)
        file_menu.add_command(label="Save", command=self.save_presentation)
        file_menu.add_command(label="Save As", command=self.save_as_presentation)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.window.destroy)
        
        slide_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Slide", menu=slide_menu)
        slide_menu.add_command(label="New Slide", command=self.add_slide)
        slide_menu.add_command(label="Delete Slide", command=self.delete_slide)
        slide_menu.add_command(label="Edit Slide", command=self.edit_slide)
        
        # Toolbar
        toolbar = tk.Frame(self.window, bg="#E1E1E1")
        toolbar.pack(fill=tk.X)
        
        tk.Button(toolbar, text="New", command=self.new_presentation).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Open", command=self.open_presentation).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Save", command=self.save_presentation).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="New Slide", command=self.add_slide).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Delete Slide", command=self.delete_slide).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Main content
        content = tk.Frame(self.window)
        content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Slide list (left sidebar)
        sidebar = tk.Frame(content, width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        tk.Label(sidebar, text="Slides", font=("Arial", 12, "bold")).pack()
        
        self.slide_listbox = tk.Listbox(sidebar, width=20)
        self.slide_listbox.pack(fill=tk.BOTH, expand=True)
        self.slide_listbox.bind('<<ListboxSelect>>', self.on_slide_select)
        
        # Slide viewer (main area)
        viewer_frame = tk.Frame(content)
        viewer_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.slide_title = tk.Label(viewer_frame, text="No Slide", 
                                    font=("Arial", 20, "bold"), bg="#F0F0F0")
        self.slide_title.pack(fill=tk.X, pady=(0, 10))
        
        self.slide_content = scrolledtext.ScrolledText(viewer_frame, wrap=tk.WORD, 
                                                       font=("Arial", 14), state=tk.DISABLED)
        self.slide_content.pack(fill=tk.BOTH, expand=True)
        
        # Navigation buttons
        nav_frame = tk.Frame(viewer_frame)
        nav_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Button(nav_frame, text="◀ Previous", command=self.prev_slide).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Next ▶", command=self.next_slide).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="Edit", command=self.edit_slide).pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_bar = tk.Label(self.window, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.update_status("New presentation")
    
    def update_status(self, message):
        """Update status bar"""
        self.status_bar.config(text=message)
    
    def update_slide_list(self):
        """Update the slide list"""
        self.slide_listbox.delete(0, tk.END)
        for i, slide in enumerate(self.slides):
            self.slide_listbox.insert(tk.END, f"{i+1}. {slide['title'][:20]}")
    
    def display_slide(self, index):
        """Display a slide"""
        if 0 <= index < len(self.slides):
            slide = self.slides[index]
            self.slide_title.config(text=slide['title'])
            
            self.slide_content.config(state=tk.NORMAL)
            self.slide_content.delete(1.0, tk.END)
            self.slide_content.insert(1.0, '\n'.join(slide['content']))
            self.slide_content.config(state=tk.DISABLED)
            
            self.current_slide = index
            self.slide_listbox.selection_clear(0, tk.END)
            self.slide_listbox.selection_set(index)
            self.update_status(f"Slide {index + 1} of {len(self.slides)}")
        else:
            self.slide_title.config(text="No Slide")
            self.slide_content.config(state=tk.NORMAL)
            self.slide_content.delete(1.0, tk.END)
            self.slide_content.config(state=tk.DISABLED)
            self.update_status("No slides")
    
    def new_presentation(self):
        """Create new presentation"""
        if self.slides and not messagebox.askyesno("New Presentation", "Discard current presentation?"):
            return
        
        self.slides = []
        self.filename = None
        self.current_slide = 0
        self.update_slide_list()
        self.display_slide(0)
        self.window.title("Presentation - Untitled")
        self.update_status("New presentation created")
    
    def add_slide(self):
        """Add new slide"""
        dialog = SlideEditorDialog(self.window, "New Slide")
        if dialog.result:
            slide = {
                'title': dialog.result['title'],
                'content': dialog.result['content'].split('\n'),
                'created': str(datetime.datetime.now())
            }
            self.slides.append(slide)
            self.update_slide_list()
            self.display_slide(len(self.slides) - 1)
            self.update_status(f"Added slide {len(self.slides)}")
    
    def edit_slide(self):
        """Edit current slide"""
        if not self.slides:
            messagebox.showinfo("No Slide", "No slide to edit")
            return
        
        slide = self.slides[self.current_slide]
        dialog = SlideEditorDialog(self.window, "Edit Slide", 
                                   slide['title'], '\n'.join(slide['content']))
        
        if dialog.result:
            slide['title'] = dialog.result['title']
            slide['content'] = dialog.result['content'].split('\n')
            self.update_slide_list()
            self.display_slide(self.current_slide)
            self.update_status(f"Slide {self.current_slide + 1} updated")
    
    def delete_slide(self):
        """Delete current slide"""
        if not self.slides:
            messagebox.showinfo("No Slide", "No slide to delete")
            return
        
        if messagebox.askyesno("Delete Slide", f"Delete slide {self.current_slide + 1}?"):
            self.slides.pop(self.current_slide)
            if self.current_slide >= len(self.slides):
                self.current_slide = max(0, len(self.slides) - 1)
            self.update_slide_list()
            self.display_slide(self.current_slide if self.slides else -1)
            self.update_status("Slide deleted")
    
    def on_slide_select(self, event):
        """Handle slide selection"""
        selection = self.slide_listbox.curselection()
        if selection:
            self.display_slide(selection[0])
    
    def prev_slide(self):
        """Go to previous slide"""
        if self.current_slide > 0:
            self.display_slide(self.current_slide - 1)
    
    def next_slide(self):
        """Go to next slide"""
        if self.current_slide < len(self.slides) - 1:
            self.display_slide(self.current_slide + 1)
    
    def save_presentation(self):
        """Save presentation"""
        if not self.slides:
            messagebox.showwarning("Warning", "No slides to save")
            return
        
        if not self.filename:
            self.save_as_presentation()
        else:
            self._save_to_file(os.path.join(self.docs_path, self.filename))
    
    def save_as_presentation(self):
        """Save presentation with new name"""
        if not self.slides:
            messagebox.showwarning("Warning", "No slides to save")
            return
        
        filepath = filedialog.asksaveasfilename(
            initialdir=self.docs_path,
            title="Save Presentation As",
            defaultextension=".pptx",
            filetypes=[("PowerPoint Files", "*.pptx"), ("All Files", "*.*")]
        )
        
        if filepath:
            self.filename = os.path.basename(filepath)
            self._save_to_file(filepath)
    
    def _save_to_file(self, filepath):
        """Save to file"""
        try:
            with open(filepath, 'w') as f:
                json.dump(self.slides, f, indent=2)
            
            self.window.title(f"Presentation - {self.filename}")
            self.update_status(f"Saved: {self.filename}")
            messagebox.showinfo("Success", "Presentation saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save: {str(e)}")
    
    def open_presentation(self):
        """Open presentation"""
        filepath = filedialog.askopenfilename(
            initialdir=self.docs_path,
            title="Open Presentation",
            filetypes=[("PowerPoint Files", "*.pptx"), ("All Files", "*.*")]
        )
        
        if filepath:
            try:
                with open(filepath, 'r') as f:
                    self.slides = json.load(f)
                
                self.filename = os.path.basename(filepath)
                self.current_slide = 0
                self.update_slide_list()
                self.display_slide(0 if self.slides else -1)
                self.window.title(f"Presentation - {self.filename}")
                self.update_status(f"Opened: {self.filename} ({len(self.slides)} slides)")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open: {str(e)}")


class SlideEditorDialog:
    """Dialog for editing slides"""
    
    def __init__(self, parent, title, slide_title="", content=""):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("600x400")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Title
        tk.Label(self.dialog, text="Slide Title:").pack(pady=(10, 5))
        self.title_entry = tk.Entry(self.dialog, width=60, font=("Arial", 12))
        self.title_entry.pack(pady=5)
        self.title_entry.insert(0, slide_title)
        
        # Content
        tk.Label(self.dialog, text="Slide Content:").pack(pady=(10, 5))
        self.content_text = scrolledtext.ScrolledText(self.dialog, wrap=tk.WORD, 
                                                      font=("Arial", 11), height=15)
        self.content_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.content_text.insert(1.0, content)
        
        # Buttons
        btn_frame = tk.Frame(self.dialog)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="OK", width=10, command=self.ok).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5)
        
        self.dialog.wait_window()
    
    def ok(self):
        """OK button handler"""
        title = self.title_entry.get().strip()
        content = self.content_text.get(1.0, tk.END).strip()
        
        if not title:
            messagebox.showwarning("Warning", "Please enter a slide title")
            return
        
        self.result = {'title': title, 'content': content}
        self.dialog.destroy()
    
    def cancel(self):
        """Cancel button handler"""
        self.dialog.destroy()


class FileManagerGUI:
    """GUI File Manager"""
    
    def __init__(self, docs_path):
        self.docs_path = docs_path
        self.window = tk.Toplevel()
        self.window.title("File Manager")
        self.window.geometry("800x600")
        
        self._create_widgets()
        self.refresh_file_list()
    
    def _create_widgets(self):
        """Create file manager widgets"""
        # Toolbar
        toolbar = tk.Frame(self.window, bg="#E1E1E1")
        toolbar.pack(fill=tk.X)
        
        tk.Button(toolbar, text="Refresh", command=self.refresh_file_list).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Delete", command=self.delete_file).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Rename", command=self.rename_file).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(toolbar, text="Info", command=self.show_file_info).pack(side=tk.LEFT, padx=5, pady=5)
        
        # File list
        list_frame = tk.Frame(self.window)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.file_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, font=("Courier", 10))
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Status bar
        self.status_bar = tk.Label(self.window, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def refresh_file_list(self):
        """Refresh file list"""
        self.file_listbox.delete(0, tk.END)
        
        try:
            files = os.listdir(self.docs_path)
            if not files:
                self.file_listbox.insert(tk.END, "No files found")
                self.status_bar.config(text="No files in directory")
            else:
                for file in sorted(files):
                    filepath = os.path.join(self.docs_path, file)
                    size = os.path.getsize(filepath)
                    self.file_listbox.insert(tk.END, f"{file:<40} {size:>10} bytes")
                self.status_bar.config(text=f"{len(files)} file(s)")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to list files: {str(e)}")
    
    def get_selected_filename(self):
        """Get selected filename"""
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a file")
            return None
        
        line = self.file_listbox.get(selection[0])
        if line == "No files found":
            return None
        
        return line.split()[0]
    
    def delete_file(self):
        """Delete selected file"""
        filename = self.get_selected_filename()
        if not filename:
            return
        
        if messagebox.askyesno("Delete File", f"Delete '{filename}'?"):
            filepath = os.path.join(self.docs_path, filename)
            try:
                os.remove(filepath)
                self.refresh_file_list()
                messagebox.showinfo("Success", f"File '{filename}' deleted")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete: {str(e)}")
    
    def rename_file(self):
        """Rename selected file"""
        filename = self.get_selected_filename()
        if not filename:
            return
        
        new_name = simpledialog.askstring("Rename File", f"Rename '{filename}' to:", 
                                         initialvalue=filename)
        
        if new_name and new_name != filename:
            old_path = os.path.join(self.docs_path, filename)
            new_path = os.path.join(self.docs_path, new_name)
            
            try:
                os.rename(old_path, new_path)
                self.refresh_file_list()
                messagebox.showinfo("Success", f"Renamed to '{new_name}'")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to rename: {str(e)}")
    
    def show_file_info(self):
        """Show file information"""
        filename = self.get_selected_filename()
        if not filename:
            return
        
        filepath = os.path.join(self.docs_path, filename)
        
        try:
            stats = os.stat(filepath)
            info = f"""File Information:

Name: {filename}
Size: {stats.st_size} bytes
Created: {datetime.datetime.fromtimestamp(stats.st_ctime)}
Modified: {datetime.datetime.fromtimestamp(stats.st_mtime)}
Path: {filepath}"""
            
            messagebox.showinfo("File Information", info)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get file info: {str(e)}")


if __name__ == "__main__":
    app = Office365GUI()
    app.run()
