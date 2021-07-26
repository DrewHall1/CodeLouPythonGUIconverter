# image_viewer.py
import io
import os
import img2pdf
import PySimpleGUI as sg
from PIL import Image
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
            sg.Button("Convert Image to .pdf")
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
                break
            break
        # if event == "Convert Image to .pdf":
        #      with open("output.pdf", "wb") as f:
        #         f.write(img2pdf.convert([i for i in os.listdir('.')if i.endswith(".jpg")]))
        #      break


    #window.close()

if __name__ == "__main__":
    main()