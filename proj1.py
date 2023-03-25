import img2pdf
import sys
import os

from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QRadioButton, QFileDialog
from PyQt5.QtCore import Qt

app=QApplication([])

def rbtn_selected():
    try:
        if rbtn1.isChecked():
            with open("merged.pdf", "wb") as f:
                f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))
        elif(rbtn2.isChecked()):
            for i in os.listdir('.'):
                if i.endswith(".jpg"): 
                    name = i+".pdf" 
                    with open(name, "wb") as f:
                        f.write(img2pdf.convert(i))
    except:
        print("an error occured")
    else:
        SuccessMsg.setText("Pdfs made!")

def select_folder():
    try:
        Selpath=QFileDialog.getExistingDirectory(None,"Select folder")
        print(f'Selected folder: {Selpath}')
        os.chdir(Selpath)
        button.setEnabled(True)
        selFolMsg.setText(f'Selected folder: {Selpath}')
    except:
        print("an error occurred")
    else:
        SuccessMsg.setText("Select to merge file or not") 
        

window=QWidget()
window.setWindowTitle("Convert Image to PDF App")
window.setGeometry(100,100,800,300)
helloMsg= QLabel("<h1>Image to PDF converter</h1>",parent=window)
helloMsg.move(60,15)

helloMsg= QLabel("<h3>Select the folder with image(s) and convert them into PDF(s)!</h3>",parent=window)
helloMsg.move(60,60)

SuccessMsg= QLabel("Choose folder",parent=window)
SuccessMsg.move(60,90)
SuccessMsg.setFixedSize(500,20)

folbutton =QPushButton("Select folder",parent=window)
folbutton.move(60,120)
# folder_path="C:/Users/Priyanshi"
folbutton.clicked.connect(select_folder)

selFolMsg=QLabel("Selected folder:",parent=window)
selFolMsg.move(180,120)
selFolMsg.setFixedSize(500,20)

MergeMsg= QLabel("Merge images into one pdf ?",parent=window)
MergeMsg.move(60,160)
rbtn1=QRadioButton("Yes",parent=window)
rbtn1.move(60,190)

rbtn2=QRadioButton("No",parent=window)
rbtn2.move(60,220)

button =QPushButton("Go!",parent=window)
button.setToolTip("This is a button")
button.setEnabled(False)
button.move(60,260)
button.clicked.connect(rbtn_selected)

window.show()
sys.exit(app.exec())
