import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading
import subprocess

def select_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("Jar Files", "*.jar")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        update_scan_button()

def select_path(entry):
    path = filedialog.askdirectory()
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)
        update_scan_button()

def run_scan():
    jar_path = entry_jar.get()
    report_path = entry_report.get()
    report_format = report_format_var.get()
    update_option = update_var.get()
    
    if not jar_path or not report_path:
        messagebox.showwarning("Warning", "Please fill in all the paths.")
        return
    
    jar_name = os.path.splitext(os.path.basename(jar_path))[0]
    
    if update_option == "Yes":
        nvd_key = entry_nvd_key.get()
        if not nvd_key:
            messagebox.showwarning("Warning", "Please enter the NVD API key.")
            return
        command = f'docker run --rm -v "{report_path}:/report" -v "{os.path.dirname(jar_path)}:/app" obsidian6362/easy-dependency-check:latest --project "{jar_name}" --scan "/app/{os.path.basename(jar_path)}" --format "{report_format}" --out /report --nvdApiKey {nvd_key}'
    else:
        command = f'docker run --rm -v "{report_path}:/report" -v "{os.path.dirname(jar_path)}:/app" obsidian6362/easy-dependency-check:latest --project "{jar_name}" --scan "/app/{os.path.basename(jar_path)}" --format "{report_format}" --out /report --noupdate'
    
    progress_bar.grid(row=10, columnspan=3, pady=10, sticky=(tk.W, tk.E))
    progress_bar.start()
    threading.Thread(target=execute_command, args=(command,)).start()

def execute_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            log_text.insert(tk.END, output)
            log_text.yview(tk.END)
    progress_bar.stop()
    progress_bar.grid_remove()
    messagebox.showinfo("Info", "Scanning completed.")

def update_visibility(*args):
    if update_var.get() == "Yes":
        entry_nvd_key.grid()
    else:
        entry_nvd_key.grid_remove()
    update_scan_button()

def update_scan_button(*args):
    if (update_var.get() == "Yes" and not entry_nvd_key.get()) or not entry_jar.get() or not entry_report.get():
        scan_button.config(state=tk.DISABLED)
    else:
        scan_button.config(state=tk.NORMAL)

def change_language(*args):
    language = language_var.get()
    labels = {
        'English': ["Jar File:", "Report Path:", "Report Format:", "Vulnerability DB Update:", "NVD API Key:", "Logs:", "Scan", "Language:"],
        '简体中文': ["Jar 文件:", "报告路径:", "报告格式:", "漏洞库更新:", "NVD API 密钥:", "日志:", "扫描", "语言:"],
        '繁體中文': ["Jar 檔案:", "報告路徑:", "報告格式:", "漏洞庫更新:", "NVD API 金鑰:", "日誌:", "掃描", "語言:"],
        '日本語': ["Jar ファイル:", "レポートパス:", "レポート形式:", "脆弱性DB更新:", "NVD APIキー:", "ログ:", "スキャン", "言語:"]
    }
    label_jar.config(text=labels[language][0])
    label_report.config(text=labels[language][1])
    label_format.config(text=labels[language][2])
    label_update.config(text=labels[language][3])
    label_nvd_key.config(text=labels[language][4])
    label_logs.config(text=labels[language][5])
    scan_button.config(text=labels[language][6])
    label_language.config(text=labels[language][7])
    root.update_idletasks()
    center_window()

def center_window():
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = tk.Tk()
root.title("Jar File Vulnerability Scanner")
root.geometry("600x450")
root.eval('tk::PlaceWindow . center')

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Jar Path
label_jar = ttk.Label(mainframe, text="Jar File:")
label_jar.grid(row=0, column=0, sticky=tk.W)
entry_jar = ttk.Entry(mainframe, width=50)
entry_jar.grid(row=0, column=1)
ttk.Button(mainframe, text="Browse", command=lambda: select_file(entry_jar)).grid(row=0, column=2)

# Report Path
label_report = ttk.Label(mainframe, text="Report Path:")
label_report.grid(row=1, column=0, sticky=tk.W)
entry_report = ttk.Entry(mainframe, width=50)
entry_report.grid(row=1, column=1)
ttk.Button(mainframe, text="Browse", command=lambda: select_path(entry_report)).grid(row=1, column=2)

# Report Format
label_format = ttk.Label(mainframe, text="Report Format:")
label_format.grid(row=2, column=0, sticky=tk.W)
report_format_var = tk.StringVar(value="HTML")
report_format_option = ttk.Combobox(mainframe, textvariable=report_format_var, values=["HTML", "XML", "CSV", "JSON", "JUNIT"])
report_format_option.grid(row=2, column=1)

# Update Option
label_update = ttk.Label(mainframe, text="Vulnerability DB Update:")
label_update.grid(row=3, column=0, sticky=tk.W)
update_var = tk.StringVar(value="No")
ttk.Radiobutton(mainframe, text="No", variable=update_var, value="No").grid(row=3, column=1, sticky=tk.W)
ttk.Radiobutton(mainframe, text="Yes", variable=update_var, value="Yes").grid(row=3, column=2, sticky=tk.W)

# NVD API Key (only visible if update is Yes)
label_nvd_key = ttk.Label(mainframe, text="NVD API Key:")
label_nvd_key.grid(row=4, column=0, sticky=tk.W)
entry_nvd_key = ttk.Entry(mainframe, width=50)
entry_nvd_key.grid(row=4, column=1)
entry_nvd_key.grid_remove()

# Log Text
label_logs = ttk.Label(mainframe, text="Logs:")
label_logs.grid(row=5, column=0, sticky=tk.W)
log_text = tk.Text(mainframe, height=10, width=70)
log_text.grid(row=6, columnspan=3, pady=10, sticky=(tk.W, tk.E))
log_text.config(state=tk.NORMAL)

# Progress Bar
progress_bar = ttk.Progressbar(mainframe, mode='indeterminate')
progress_bar.grid(row=7, columnspan=3, pady=10, sticky=(tk.W, tk.E))
progress_bar.grid_remove()

# Scan Button
scan_button = ttk.Button(mainframe, text="Scan", command=run_scan)
scan_button.grid(row=8, column=1)
scan_button.config(state=tk.DISABLED)

update_var.trace_add("write", update_visibility)
entry_nvd_key.bind("<KeyRelease>", update_scan_button)
entry_jar.bind("<KeyRelease>", update_scan_button)
entry_report.bind("<KeyRelease>", update_scan_button)

# Language Selection
label_language = ttk.Label(mainframe, text="Language:")
label_language.grid(row=9, column=0, sticky=tk.W, pady=(10,0))
language_var = tk.StringVar(value="English")
language_option = ttk.Combobox(mainframe, textvariable=language_var, values=["English", "简体中文", "繁體中文", "日本語"])
language_option.grid(row=9, column=1, pady=(10,0))
language_var.trace_add("write", change_language)

center_window()

root.mainloop()
