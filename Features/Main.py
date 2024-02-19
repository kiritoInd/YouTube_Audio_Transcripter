import GenrateSubtitles as gs
import tkinter as tk
from tkinter import filedialog
import csv
import os
import shutil

def run_subtitle_generator():
    def open_file_dialog():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            entry_input.delete(0, tk.END)
            entry_input.insert(0, file_path)

    def process():
        input_file = entry_input.get()
        if input_file:
            gs.generate_transcriptions(input_file, '.') 
            status_label.config(text="Transcriptions generated successfully!")

            download_link = tk.Label(window, text="Download Transcriptions CSV", fg="blue", cursor="hand2")
            download_link.grid(row=3, column=0, columnspan=3)
            download_link.bind("<Button-1>", lambda e: download_output('transcription_output.csv'))

    def download_output(output_file):
        if os.path.exists(output_file):
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if save_path:
                shutil.copy(output_file, save_path)
                status_label.config(text="File saved successfully")
            else:
                status_label.config(text="Save cancelled")
        else:
            status_label.config(text="Error: Output file not found")

    window = tk.Tk()
    window.title("Subtitle Generator")

    window.geometry("440x180") 
    label_input = tk.Label(window, text="Input CSV file:")
    label_input.grid(row=0, column=0, sticky=tk.E+tk.W)
    entry_input = tk.Entry(window, width=50)
    entry_input.grid(row=0, column=1, sticky=tk.E+tk.W)
    button_browse_input = tk.Button(window, text="Browse", command=open_file_dialog)
    button_browse_input.grid(row=0, column=2, sticky=tk.E+tk.W)

    button_process = tk.Button(window, text="Generate Subtitles", command=process)
    button_process.grid(row=1, column=1, sticky=tk.E+tk.W)

    status_label = tk.Label(window, text="")
    status_label.grid(row=4, column=0, columnspan=3, sticky=tk.E+tk.W)
    info_label = tk.Label(window, text="It takes 2-3 minutes to generate subtitles for 1 video of 30mins. Please be patient.")
    info_label.grid(row=5, column=0, columnspan=3, sticky=tk.E+tk.W)

    window.mainloop()
