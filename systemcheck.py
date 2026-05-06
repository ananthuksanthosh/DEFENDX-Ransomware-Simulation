import tkinter as tk
from tkinter import messagebox
import sys

class RansomwareSim:
    def __init__(self):
        self.password = "unlock123"
        self.attempts = 0
        
        # Main window
        self.root = tk.Tk()
        self.root.title("☠️ DEFENDX ☠️")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        
        # Center everything
        main = tk.Frame(self.root, bg='black')
        main.place(relx=0.5, rely=0.5, anchor='center')
        
        # ========== HEADER WITH SKULL EMOJIS ==========
        header = tk.Label(
            main, 
            text="☠️ DEFENDX ☠️", 
            font=('Arial', 52, 'bold'), 
            fg='red', 
            bg='black'
        )
        header.pack(pady=(0, 10))
        
        # ========== SUB HEADER ==========
        sub_header = tk.Label(
            main, 
            text="Your personal files are encrypted", 
            font=('Arial', 24, 'bold'), 
            fg='white', 
            bg='black'
        )
        sub_header.pack(pady=(0, 20))
        
        # ========== INFO BOX ==========
        info_frame = tk.Frame(main, bg='#111111', bd=2, relief='solid')
        info_frame.pack(fill='x', pady=(0, 15), padx=10)
        
        info_title = tk.Label(
            info_frame, 
            text="Info", 
            font=('Arial', 18, 'bold'), 
            fg='red', 
            bg='#111111'
        )
        info_title.pack(anchor='w', padx=15, pady=(10, 5))
        
        info_text = """Your important files were encrypted on this computer: photos, videos, documents, etc. 
You can verify this by clicking on see files and try to open them.

Encryption was produced using unique public key RSA-4096 generated for this computer. 
To decrypt files, you need to obtain private key.

The single copy of the private key, which will allow you to decrypt the files, 
is located on a secret server on the Internet. After that, nobody and never 
will be able to restore files."""
        
        info_content = tk.Label(
            info_frame, 
            text=info_text, 
            font=('Arial', 11), 
            fg='#cccccc', 
            bg='#111111', 
            justify='left'
        )
        info_content.pack(anchor='w', padx=15, pady=(0, 10))
        
        # ========== SEPARATOR ==========
        separator = tk.Label(
            main, 
            text="-" * 60, 
            font=('Arial', 10), 
            fg='gray', 
            bg='black'
        )
        separator.pack(pady=(0, 10))
        
        # ========== WARNING MESSAGE (NO TIMER) ==========
        warning_text = """To retrieve the private key, you need to enter the correct decryption key below.
Any attempt to remove or damage this software will lead to immediate
private key destruction by server."""
        
        warning_label = tk.Label(
            main, 
            text=warning_text, 
            font=('Arial', 12), 
            fg='red', 
            bg='black', 
            justify='left'
        )
        warning_label.pack(pady=(0, 20))
        
        # ========== PASSWORD INPUT SECTION ==========
        pass_label = tk.Label(
            main, 
            text="Enter Decryption Key:", 
            font=('Arial', 14, 'bold'), 
            fg='white', 
            bg='black'
        )
        pass_label.pack(pady=(0, 10))
        
        self.entry = tk.Entry(
            main,
            font=('Consolas', 16, 'bold'),
            width=30,
            show='*',
            bg='white',
            fg='black',
            insertbackground='red',
            justify='center',
            bd=3,
            relief='solid'
        )
        self.entry.pack(pady=(0, 15))
        self.entry.bind('<Return>', self.check)
        self.entry.focus()
        
        # ========== BUTTONS ==========
        btn_frame = tk.Frame(main, bg='black')
        btn_frame.pack(pady=(0, 15))
        
        see_btn = tk.Button(
            btn_frame, 
            text="See files", 
            font=('Arial', 11), 
            bg='gray', 
            fg='black', 
            command=self.fake_files,
            padx=15
        )
        see_btn.pack(side='left', padx=5)
        
        back_btn = tk.Button(
            btn_frame, 
            text="<< Back", 
            font=('Arial', 11), 
            bg='gray', 
            fg='black', 
            command=lambda: None,
            padx=15
        )
        back_btn.pack(side='left', padx=5)
        
        proceed_btn = tk.Button(
            btn_frame, 
            text="Proceed to unlock >>", 
            font=('Arial', 11, 'bold'), 
            bg='red', 
            fg='white', 
            command=self.check,
            padx=15
        )
        proceed_btn.pack(side='left', padx=5)
        
        # ========== STATUS ==========
        self.status = tk.Label(
            main, 
            text="", 
            font=('Arial', 11), 
            fg='yellow', 
            bg='black'
        )
        self.status.pack(pady=(0, 10))
        
        # ========== FOOTER ==========
        footer = tk.Label(
            self.root,
            text="DEFEND Cyber Security Challenge - Educational Simulation - No files were harmed",
            font=('Arial', 9),
            fg='gray',
            bg='black'
        )
        footer.pack(side='bottom', pady=10)
        
        self.root.mainloop()
    
    def fake_files(self):
        messagebox.showinfo(
            "See files", 
            "This is a SIMULATION.\n\nNo real files have been encrypted.\nYour files are completely safe.\n\nThis is for educational purposes only."
        )
    
    def check(self, event=None):
        user_input = self.entry.get()
        
        if user_input == self.password:
            self.root.destroy()
            messagebox.showinfo(
                "SYSTEM UNLOCKED",
                f"Decryption successful!\n\nYour system has been restored.\n\nKey used: {self.password}\n\nThis was an educational simulation.\nNo files were ever encrypted or harmed."
            )
            sys.exit(0)
        else:
            self.attempts += 1
            remaining = 5 - self.attempts
            self.status.config(
                text=f"INVALID DECRYPTION KEY! Attempt {self.attempts}/5. {remaining} attempts remaining.",
                fg='red'
            )
            self.entry.delete(0, 'end')
            self.entry.focus()
            
            if self.attempts >= 5:
                messagebox.showwarning(
                    "SIMULATION WARNING",
                    "In a real ransomware attack, your files would now be deleted.\n\nThis is an EDUCATIONAL SIMULATION.\nYour files are 100% safe."
                )
                self.attempts = 0
                self.status.config(text="")

if __name__ == "__main__":
    RansomwareSim()