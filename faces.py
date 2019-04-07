from tkinter import *
from tkinter import filedialog
import tkinter.filedialog
import os
import face_recognition
from PIL import Image, ImageDraw

master = Tk()  # Create the main window

tekst1 = "Program instruction"
tekst2 = "Face recognition application is based on face_recognition python libary\n\n" \
         "Load face file - load the photo with the face you want to search for\n" \
         "Select folder  - select the folder in which you want to search"


def master_setup():
    master.title("Faces")
    master.geometry("486x382")
    master.configure(background='#C0D4EE')
    master.resizable(0, 0)


def instruction():
    def close(what):
        instruction.quit()
        instruction.destroy()

    instruction = Toplevel()
    instruction.title("Program instruction")
    instruction.geometry("800x180")
    instruction.resizable(0, 0)
    Label(instruction, text=tekst1, font="Times 20 bold").pack()
    Label(instruction, text=tekst2, font="20").pack()
    przycisk = Button(instruction, text="Close", width=20, bg="lightgrey", height=3)
    przycisk.bind("<Button-1>", close)
    przycisk.pack(side="bottom")
    instruction.mainloop()


def loadface():
    file = tkinter.filedialog.askopenfilename(parent=master,
                                              initialdir='')
    global face_location_test_photo
    face_location_test_photo = face_recognition.load_image_file(file)


def choosefolder():
    global folder_path
    folder_path = filedialog.askdirectory()


def showpics():

    for filename in os.listdir(folder_path):

        Contains = 0

        test_image = face_recognition.load_image_file('%s' % folder_path +"/"+ filename)

        # Find faces in test image
        face_locations = face_recognition.face_locations(test_image)
        face_on_photo = face_recognition.face_encodings(test_image, face_locations)

        known_face = face_recognition.face_encodings(face_location_test_photo)[0]

        known_face_encodings = [
            known_face,
        ]
        # Convert to PIL format
        pil_image = Image.fromarray(test_image)

        # Create a ImageDraw instance
        draw = ImageDraw.Draw(pil_image)

        # Loop through faces in test image
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_on_photo):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            if True in matches:
                Contains = 1
                # Draw box
                draw.rectangle(((left - 16, top - 16), (right + 16, bottom + 16)), outline=(14, 22, 200), width=3)

        del draw

        # Display image

        if (Contains):
            pil_image.show()


def rename():  # rename file to pic"i"
    global i
    i=1
    j=1
    for filename in os.listdir(folder_path):
        dst = "temp" + str(j) + ".jpg"
        src = '%s/' % folder_path + filename
        dst = '%s/' % folder_path + dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        j += 1
    for filename in os.listdir(folder_path):
        dst = "pic" + str(i) + ".jpg"
        src = '%s/' % folder_path + filename
        dst = '%s/' % folder_path + dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


def wyjscie():
    sys.exit()


def show_menu():
    Label(master, text='Application menu',
          width=30, font="Times 20 bold", bg='#C0D4EE').grid(row=0, pady=4, padx=4, column=0, columnspan=3)
    Button(master, text='Instruction',
           command=instruction, width=25, height=5, font=20, bg='lightgreen').grid(row=1, column=0)
    Button(master, text='Load face file',
           command=loadface, width=25, height=5, font=20, bg="#ff7777").grid(row=1, column=1)
    Button(master, text='Select folder',
           command=choosefolder, width=25, height=5, font=20, bg="#C0D4CC").grid(row=2, column=0)
    Button(master, text='Show images containing face',
           command=showpics, width=25, height=5, font=20, bg="#ffcc44").grid(row=2, column=1, pady=10)
    Button(master, text='Rename files\n(optional)',
           command=rename, width=25, height=5, font=20, bg="wheat").grid(row=3, column=0)
    Button(master, text='Exit',
           command=wyjscie, width=25, height=5, font=20, bg="lightpink").grid(row=3, column=1)
    master.mainloop()


def main():
    master_setup()
    show_menu()


main()
