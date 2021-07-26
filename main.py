# img_viewer.py

import io
import os
import PySimpleGUI as sg
import os.path
import img2pdf
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]



# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button(button_text="Create pdf", key="-PDF-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

def handle_events(event, values):
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        handle_folder_selection(values)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        handle_file_selection(values)
    elif event == "-PDF-":  # User wants to convert to .pdf
        handle_create_pdf(values)
    #return()

def handle_folder_selection(values):
    folder = values["-FOLDER-"]
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
           and f.lower().endswith((".png", ".gif", ".jpg"))
    ]
    window["-FILE LIST-"].update(fnames)
    #return()

def handle_file_selection(values):
    try:
        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )
        window["-TOUT-"].update(filename)
        # window["-IMAGE-"].update(filename=filename)

        if os.path.exists(filename):
            image = Image.open(filename)
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())

    except Exception as e:
        log_error("file selection", e)
        print(e)
    #return()

def handle_create_pdf(values):  #the pdf will write with the same name as the jpg only with pdf extension
    try:
        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )
        base_file_name = os.path.splitext(filename)[0]
        new_file_name = base_file_name + ".pdf"
        image = Image.open(filename)

        # converting into chunks using img2pdf
        pdf_bytes = img2pdf.convert(image.filename)

        # opening or creating pdf file
        file = open(new_file_name, "wb")

        # writing pdf files with chunks
        file.write(pdf_bytes)

        # closing image file
        image.close()

        # closing pdf file
        file.close()
        print("pdf created at: " + new_file_name)
    except Exception as e:
        log_error("create pdf", e)
        print(e)
    #return()

def log_error(error_step, error_exception):  # append errors to the end of the text file
    error_path = os.path.join(
        values["-FOLDER-"], "errors.txt"
    )
    with open(error_path, "a")  as file_object:
        file_object.write("error occurred at {0}: {1}".format(str(error_step), str(error_exception)))
    return()

window = sg.Window("Image Viewer", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    else:
        handle_events(event, values)



window.close()
