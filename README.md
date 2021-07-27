# CodeLouPythonGUIconverter

this project was to solve a problem I had at a previous job where our system would only upload documents from borrowers when I was a loan processor that were in a .pdf format, 
however most people sent things in .jpg so this project will convert the .jpg to a .pdf for you.

The requirements met for the project include:
   •	Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
   •	Implement a log that records errors, invalid inputs, or other important events and writes them to a text file
   •	Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
   •	Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. 
   •	Build a conversion tool that converts user input to another type and displays it 

In order to run this you'll need to download:
  - Pillow
  - Flask
  - img2pdf
  - PySimpleGUI
  
How to run this you will need to:
  - run the "main.py" file.
  - a GUI box will open up that will allow you to click browse button (this will allow you to navigate to your own directory and find a folder with .jpg images files
  - once you click to open that folder, all the .jpg, .jpeg type files will populate in the list box on the side.
  - you will be able to choose a file, it will preview on the right side
  - if that is the file you want to convert, click the "convert to .pdf" button
  - the file will be converted to .pdf and found in the same directory as the original file only instead of .jpg extension, it will be a .pdf with the same file name
  - you can also create an error if you don't choose a file from the list box and click the "convert to pdf" button
  - error messages are printed to a doc in the source folder where the images came from
