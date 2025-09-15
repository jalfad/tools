import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog,messagebox

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\jalfad\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def run_ocr():
    file_path = filedialog.askopenfilename(
        title = "Select an Image",
        filetypes=[("Image Files","*.png;*jpg;,*jpeg;,*tif;,*bmp;")]
 )
    if not file_path:
        return
     
    try:
        img = Image.open(file_path)

        pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf')

        save_path = file_path.rsplit(".",1)[0] + ".pdf"
    
        with open(save_path, "wb") as f:
         f.write(pdf_bytes)
         
        messagebox.showinfo("Error", f"PDF saved at \n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Image to PDF OCR")
root.geometry("300x150")

btn = tk.Button(root, text="SELECT IMAGE AND CONVERT", command=run_ocr,width=30,height=2,font=("Arial", 12))
btn.pack(pady=20)
root.mainloop() 
