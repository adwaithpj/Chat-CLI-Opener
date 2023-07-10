import webbrowser

def open_html_files():
    html_file1 = "https://bard.google.com/"  # Replace with the URL of your first HTML file
    html_file2 = "https://chat.openai.com/"  # Replace with the URL of your second HTML file
    
    webbrowser.open_new_tab(html_file1)
    webbrowser.open_new_tab(html_file2)

open_html_files()
