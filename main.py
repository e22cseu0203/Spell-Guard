from textblob import TextBlob
from tkinter import *
from tkinter import messagebox, filedialog
from textblob import TextBlob
from tkinter import messagebox

def check():
    original_text = e.get("1.0", END)  # Get input text from the user
    b = TextBlob(original_text)  # Correct the text using TextBlob
    corrected_text = str(b.correct())  # Get the corrected text

    # Show the corrected text in the label
    corrected_text_label.config(text=corrected_text)

    # Calculate accuracy
    accuracy = calculate_accuracy(original_text.strip(), corrected_text.strip())
    
    # Show accuracy in a pop-up message box
    messagebox.showinfo("Accuracy", f"Accuracy: {accuracy}%")

# Function to launch the main SpellCheck window
def open_spellcheck():
    start_window.destroy()  # Close the start window
    root = Tk()
    root.title('SpellCheck')
    root.geometry('1600x900')  # Very large window size
    root.config(bg="#FF0000")  # Red background color

    head = Label(root, text='SpellCheck', font=('Arial', 36, 'bold'), bg="#FFFF00", fg="black")  # Yellow header with black text
    head.pack(pady=20)

    # Reduced horizontal size of the green frame
    frame = Frame(root, bg="#008000")  # Green frame background
    frame.pack(pady=20, padx=20, ipadx=20, ipady=20)  # Reduced padx and ipadx

    e_label = Label(frame, text="Enter Text:", font=('Arial', 18, 'bold'), bg="#F5DEB3", fg="#000000")  # Biscuit label background
    e_label.grid(row=0, column=0, sticky=W, pady=10)

    e = Text(frame, wrap=WORD, width=70, height=10, borderwidth=5, font=('Arial', 16), bg="#E0FFFF", fg="black", insertbackground='black')  # Smaller text area width
    e.grid(row=1, column=0, columnspan=5, padx=20, pady=20)

    def check():
        original_text = e.get("1.0", END)
        b = TextBlob(original_text)
        corrected_text = str(b.correct())
        corrected_text_label.config(text=corrected_text)

    def clear():
        e.delete("1.0", END)
        corrected_text_label.config(text="")

    def copy_to_clipboard():
        root.clipboard_clear()
        root.clipboard_append(corrected_text_label.cget("text"))
        messagebox.showinfo("Copied", "Corrected text copied to clipboard!")

    def save_output():
        corrected_text = corrected_text_label.cget("text")
        if corrected_text:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(corrected_text)
                messagebox.showinfo("Saved", f"Corrected text saved to {file_path}")
        else:
            messagebox.showwarning("No Text", "There is no corrected text to save!")

    def load_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                e.delete("1.0", END)
                e.insert(END, file_content)
                messagebox.showinfo("File Loaded", f"File loaded from {file_path}")

    def tokenize():
        original_text = e.get("1.0", END).strip()
        if original_text:
            b = TextBlob(original_text)
            tokens = b.tokens
            tokens_text = '\n'.join(tokens)  # Join tokens with newline for better readability
            corrected_text_label.config(text=f"Tokens:\n{tokens_text}")
            
            
        else:
            corrected_text_label.config(text="No text to tokenize.")

    correct_btn = Button(frame, text='Check', font=('Arial', 14, 'bold'), fg='white', bg='blue', command=check)  # Blue button
    correct_btn.grid(row=2, column=0, pady=20, padx=10)

    clear_btn = Button(frame, text='Clear', font=('Arial', 14, 'bold'), fg='white', bg='brown', command=clear)  # Brown button
    clear_btn.grid(row=2, column=1, pady=20, padx=10)

    copy_btn = Button(frame, text='Copy Corrected Text', font=('Arial', 14, 'bold'), fg='white', bg='indigo', command=copy_to_clipboard)  # Indigo button
    copy_btn.grid(row=2, column=2, pady=20, padx=10)

    save_btn = Button(frame, text='Save Output', font=('Arial', 14, 'bold'), fg='white', bg='purple', command=save_output)  # Purple button
    save_btn.grid(row=2, column=3, pady=20, padx=10)

    load_btn = Button(frame, text='Choose File', font=('Arial', 14, 'bold'), fg='white', bg='darkorange', command=load_file)  # Orange button for file selection
    load_btn.grid(row=2, column=4, pady=20, padx=10)

    # Tokenize button
    tokenize_btn = Button(frame, text='Tokenize', font=('Arial', 14, 'bold'), fg='white', bg='cyan', command=tokenize)  # Cyan button for tokenization
    tokenize_btn.grid(row=2, column=5, pady=20, padx=10)
   
    # Red output section with black text
    corrected_text_label = Label(root, text='', font=('Arial', 24, 'bold'), bg="#FF0000", fg="black", wraplength=1000, justify=LEFT)  # Black text on red background
    corrected_text_label.pack(pady=20)
    
  
 

    root.mainloop()

# Create the start window
start_window = Tk()
start_window.title('Start SpellCheck')
start_window.geometry('600x300')
start_window.config(bg="#FF1493")  # Dark pink background

start_label = Label(start_window, text='WELCOME', font=('Arial', 24, 'bold'), bg="#FF1493", fg="black")
start_label.pack(pady=50)

start_button = Button(start_window, text='Start', font=('Arial', 24, 'bold'), fg='white', bg='#008000', command=open_spellcheck)  # Green start button
start_button.pack(pady=20)

start_window.mainloop()