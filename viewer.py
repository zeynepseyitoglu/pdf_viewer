import PyPDF2
import tkinter as tk
from tkinter import filedialog, Text, Scrollbar


class PDFViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer")
        self.root.geometry("800x600")

        self.text_widget = Text(self.root, wrap="word", font=("Helvetica", 12))
        self.text_widget.pack(fill="both", expand=True)

        self.scrollbar = Scrollbar(self.text_widget, command=self.text_widget.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_pdf)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.root.config(menu=self.menu_bar)

    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            text = self.read_pdf(file_path)
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, text)

    def read_pdf(self, file_path):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text


def main():
    root = tk.Tk()
    app = PDFViewerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
