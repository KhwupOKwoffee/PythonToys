import tkinter as tk
from tkinter import filedialog, ttk

import os
from PIL import Image, ImageTk, ImageFilter


class SIMPWindow(tk.Tk):

    def __init__(self):

        # Window properties
        super().__init__()
        self.title("Simple Image Manipulation Program")
        self.geometry("1280x720")
        self.resizable(width = True, height = True)

        # Image panel
        self.image_panel = tk.Label(self)
        self.image_panel.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        # Open & save buttons
        self.open_button = tk.Button(
            self,
            width = 16,
            text = "Open Image",
            command = self.open
        )
        self.open_button.grid(row = 1, column = 1)

        self.save_button = tk.Button(
            self,
            width = 16,
            text = "Save Image",
            command = self.save
        )
        self.save_button.grid(row = 1, column = 2)

        # Greyscale & invert colours buttons
        self.greyscale_button = tk.Button(
            self,
            width = 16,
            text = "Greyscale",
            command = self.greyscale
        )
        self.greyscale_button.grid(row = 2, column = 1)

        self.invert_colours_button = tk.Button(
            self,
            width = 16,
            text = "Invert Colours",
            command = self.invert_colours
        )
        self.invert_colours_button.grid(row = 2, column = 2)

        # Remove colours button & checkbuttons
        self.remove_colours_button = tk.Button(
            self,
            width = 16,
            text = "Remove Colours",
            command = self.remove_colours
        )
        self.remove_colours_button.grid(row = 3, column = 1)

        self.remove_red = tk.IntVar(self)
        self.remove_green = tk.IntVar(self)
        self.remove_blue = tk.IntVar(self)
        self.remove_red_checkbutton = tk.Checkbutton(
            self,
            text = "R",
            variable = self.remove_red,
            onvalue = 1,
            offvalue = 0
        )
        self.remove_green_checkbutton = tk.Checkbutton(
            self,
            text = "G",
            variable = self.remove_green,
            onvalue = 1,
            offvalue = 0
        )
        self.remove_blue_checkbutton = tk.Checkbutton(
            self,
            text = "B",
            variable = self.remove_blue,
            onvalue = 1,
            offvalue = 0
        )
        self.remove_red_checkbutton.grid(row = 3, column = 2, sticky = tk.W)
        self.remove_green_checkbutton.grid(row = 3, column = 2)
        self.remove_blue_checkbutton.grid(row = 3, column = 2, sticky = tk.E)

        # Reflect button & checkbuttons
        self.reflect_button = tk.Button(
            self,
            width = 16,
            text = "Reflect",
            command = self.reflect
        )
        self.reflect_button.grid(row = 4, column = 1)

        self.reflect_horizontally = tk.IntVar(self)
        self.reflect_vertically = tk.IntVar(self)
        self.reflect_horizontally_checkbutton = tk.Checkbutton(
            self,
            text = "H",
            variable = self.reflect_horizontally,
            onvalue = 1,
            offvalue = 0
        )
        self.reflect_vertically_checkbutton = tk.Checkbutton(
            self,
            text = "V",
            variable = self.reflect_vertically,
            onvalue = 1,
            offvalue = 0
        )
        self.reflect_horizontally_checkbutton.grid(row = 4, column = 2, sticky = tk.W)
        self.reflect_vertically_checkbutton.grid(row = 4, column = 2, sticky = tk.E)

        # Rotate button & radiobuttons
        self.rotate_button = tk.Button(
            self,
            width = 16,
            text = "Rotate 90°",
            command = self.rotate
        )
        self.rotate_button.grid(row = 5, column = 1)

        self.rotate_direction = tk.StringVar(self, "clockwise")
        self.rotate_clockwise_radiobutton = tk.Radiobutton(
            self,
            text = "↻",
            variable = self.rotate_direction,
            value = "clockwise"
        )
        self.rotate_anticlockwise_radiobutton = tk.Radiobutton(
            self,
            text = "↺",
            variable = self.rotate_direction,
            value = "anticlockwise"
        )
        self.rotate_clockwise_radiobutton.grid(row = 5, column = 2, sticky = tk.W)
        self.rotate_anticlockwise_radiobutton.grid(row = 5, column = 2, sticky = tk.E)

        # Blur button & slider
        self.blur_button = tk.Button(
            self,
            width = 16,
            text = "Blur",
            command = self.blur
        )
        self.blur_button.grid(row = 6, column = 1)

        self.blur_radius = tk.IntVar(self)
        self.blur_radius_slider = tk.Scale(
            self,
            variable = self.blur_radius,
            from_ = 1,
            to = 32,
            orient = tk.HORIZONTAL,
            showvalue = False
        )
        self.blur_radius_slider.grid(row = 6, column = 2)

        # Apply effects button & combobox
        self.apply_effect_button = tk.Button(
            self,
            width = 16,
            text = "Apply Effect",
            command = self.apply_effect
        )
        self.apply_effect_button.grid(row = 7, column = 1)

        self.effect = tk.StringVar(self)
        self.effect_combobox = ttk.Combobox(
            self,
            textvariable = self.effect,
            width = 16
        )
        self.effect_combobox["values"] = (
            "CONTOUR",
            "DETAIL",
            "EDGE_ENHANCE",
            "EMBOSS",
            "FIND_EDGES",
            "SHARPEN",
            "SMOOTH"
        )
        self.effect_combobox.grid(row = 7, column = 2)

    def open(self, filename=None):
        
        if filename:
            self.filename = filename
        else:
            self.filename = filedialog.askopenfilename(title = "Open Image")
            if not self.filename:
                return
        
        if self.filename != "temp.bmp":
            self.og_filename = self.filename
            self.title(f"{self.filename} - Simple Image Manipulation Program")
        else:
            self.title(f"{self.og_filename}* - Simple Image Manipulation Program")

        self.image = Image.open(self.filename)
        self.image.display = ImageTk.PhotoImage(self.image)
        self.image_panel["image"] = self.image.display

    def save(self):

        filename = filedialog.asksaveasfilename(title = "Save Image", initialfile = "simp.bmp")
        self.image.save(filename, format = "bmp")
        os.remove("temp.bmp")
        self.open(filename)

    def save_temp(self):
        self.image.save("temp.bmp", format = "bmp")
        self.open("temp.bmp")

    def greyscale(self):

        self.image = self.image.convert(mode = "L")
        self.image = self.image.convert(mode = "RGB")
        self.save_temp()

    def invert_colours(self):

        self.image.pixelmap = self.image.load()
        for i in range(self.image.width):
            for j in range(self.image.height):
                r, g, b = self.image.getpixel((i, j))

                r = 255 - r
                g = 255 - g
                b = 255 - b

                self.image.pixelmap[i, j] = (r, g, b)
        self.save_temp()

    def remove_colours(self):

        self.image.pixelmap = self.image.load()
        for i in range(self.image.width):
            for j in range(self.image.height):
                r, g, b = self.image.getpixel((i, j))

                if self.remove_red.get(): r = 0
                if self.remove_green.get(): g = 0
                if self.remove_blue.get(): b = 0

                self.image.pixelmap[i, j] = (r, g, b)
        self.save_temp()

    def reflect(self):

        if self.reflect_horizontally.get():
            self.image = self.image.transpose(method = Image.Transpose.FLIP_LEFT_RIGHT)
        if self.reflect_vertically.get():
            self.image = self.image.transpose(method = Image.Transpose.FLIP_TOP_BOTTOM)
        self.save_temp()

    def rotate(self):

        if self.rotate_direction.get() == "clockwise":
            self.image = self.image.transpose(method = Image.Transpose.ROTATE_270)
        else:
            self.image = self.image.transpose(method = Image.Transpose.ROTATE_90)
        self.save_temp()

    def blur(self):

        self.image = self.image.filter(filter = ImageFilter.GaussianBlur(self.blur_radius.get()))
        self.save_temp()

    def apply_effect(self):

        self.image = eval(f"self.image.filter(filter = ImageFilter.{self.effect.get()})")
        self.save_temp()

