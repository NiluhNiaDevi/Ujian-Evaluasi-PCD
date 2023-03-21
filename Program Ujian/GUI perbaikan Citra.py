from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageStat, ImageTk
import numpy as np
import cv2


class ImageEditor:
    def __init__(self, master):
        self.master = master
        self.master.title ( "Aplikasi Perbaikan Citra" )

        # Membuat label nama dan nim di GUI
        label_nama = tk.Label ( root, text="Niluh Nia Devi_F55121058" )
        label_nama.pack ( side=tk.TOP, padx=10, pady=5 )

        label_nim = tk.Label ( root, text="kelas: B-Teknik Informatika" )
        label_nim.pack ( side=tk.TOP, padx=10, pady=5 )

        label_nim = tk.Label ( root, text="Edit foto untuk filter tinggi dan Menjadi Blur" )
        label_nim.pack ( side=tk.TOP, padx=10, pady=5 )

        # buat tombol "select image" dan hubungkan dengan metode "open_image"
        self.open_button = Button ( self.master, text="Select Image", command=self.open_image )
        self.open_button.pack ( )

        # buat tombol "High Pass Filtering" dan hubungkan dengan metode "high_pass_filtering"
        self.high_pass_filtering_button = Button ( self.master, text="High Pass Filtering",
                                                   command=self.high_pass_filtering )
        self.high_pass_filtering_button.pack ( )

        # buat tombol "Gaussian Blur" dan hubungkan dengan metode "gaussian_blur"
        self.gaussian_blur_button = Button ( self.master, text="Gaussian Blur", command=self.gaussian_blur )
        self.gaussian_blur_button.pack ( )

    def open_image(self):
        # membuka dialog box untuk memilih file citra
        file_path = filedialog.askopenfilename ( )

        # membuka citra dan menampilkan pada canvas
        self.image = Image.open ( file_path )
        self.photo = ImageTk.PhotoImage ( self.image )
        self.canvas = Canvas ( self.master, width=self.image.size[0], height=self.image.size[1] )
        self.canvas.pack ( )
        self.canvas.create_image ( 0, 0, anchor=NW, image=self.photo )

    def high_pass_filtering(self):
        # mempertajam citra dengan high pass filtering dan menampilkan hasil pada canvas
        img = cv2.cvtColor ( np.array ( self.image ), cv2.COLOR_RGB2GRAY )
        high_pass_kernel = np.array ( [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]] )
        filtered = cv2.filter2D ( img, -1, high_pass_kernel )
        self.image = Image.fromarray ( filtered )
        self.photo = ImageTk.PhotoImage ( self.image )
        self.canvas.create_image ( 0, 0, anchor=NW, image=self.photo )

    def gaussian_blur(self):
        # menghaluskan citra dengan gaussian blur dan menampilkan hasil pada canvas
        radius = 4
        kernel_size = int ( 4 * radius + 1 )
        self.image = self.image.filter ( ImageFilter.GaussianBlur ( radius=radius ) )
        self.photo = ImageTk.PhotoImage ( self.image )
        self.canvas.create_image ( 0, 0, anchor=NW, image=self.photo )


if __name__ == '__main__':
    root = Tk ( )
    app = ImageEditor ( root )
    root.mainloop ( )
