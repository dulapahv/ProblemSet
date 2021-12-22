# Convert H.264 Hi10P to H.265 Hi10P using ffmpeg
# Tkinter based GUI
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import sys
class App:
def __init__(self, master):


self.var1 = IntVar()
self.var2 = IntVar()
self.var3 = IntVar()
self.var4 = IntVar()
self.re_encoded = IntVar()
self.master = master
self.master.title("H.264 to H.265")
self.master.geometry("500x750")
self.master.configure(background="#d9d9d9")
self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
self.input_path = StringVar()
self.output_path = StringVar()
self.input_path.set("")
self.output_path.set("")
self.input_label = Label(self.master, text="Input file:", bg="#d9d9d9")
self.input_label.place(x=10, y=10)
self.input_entry = Entry(self.master, textvariable=self.input_path, width=40)
self.input_entry.place(x=10, y=30)
self.input_button = Button(self.master, text="Browse",
                           command=self.browse_input)
self.input_button.place(x=330, y=30)
self.output_label = Label(self.master, text="Output file:", bg="#d9d9d9")
self.output_label.place(x=10, y=60)
self.output_entry = Entry(self.master, textvariable=self.output_path, width=40)
self.output_entry.place(x=10, y=80)self.output_button = Button(self.master, text="Browse", command=self.browse_output)
self.output_button.place(x=330, y=80)
self.lebel1 = Label(
    self.master, text="Which device do you use for watch?", bg="#d9d9d9")
self.lebel1.place(x=10, y=150)
self.radio_button = Radiobutton(self.master, text="Phone, Laptop, TV, 21ʺ monitor",
value=1, bg="#d9d9d9",
variable=self.var1)
self.radio_button.place(x=10, y=170)
self.radio_button2 = Radiobutton(self.master, text="21-24ʺ monitor", value=2,
bg="#d9d9d9", variable=self.var1)
self.radio_button2.place(x=10, y=190)
self.radio_button3 = Radiobutton(self.master, text="4K monitor", value=3, bg="#d9d9d9",
variable=self.var1)
self.radio_button3.place(x=10, y=210)
self.radio_button4 = Radiobutton(self.master, text="JUST DON'T(Bloated file and forever
encode time)", value=4,
bg="#d9d9d9", variable=self.var1)
self.radio_button4.place(x=10, y=230)
self.label2 = Label(self.master, text="Preset? (If you don't know what is it and have time,
pick slow)", bg="  # d9d9d9")
self.label2.place(x=10, y=260)
self.radio_button5=Radiobutton(self.master, text="fast", value=1, bg="#d9d9d9",
variable=self.var2)
self.radio_button5.place(x=10, y=280)
self.radio_button6=Radiobutton(self.master, text="slow (Recommended)", value=2,
bg="#d9d9d9", variable=self.
var2)
self.radio_button6.place(x=10, y=300)
self.radio_button7=Radiobutton(self.master, text="veryslow", value=3, bg="#d9d9d9",
variable=self.var2)
self.radio_button7.place(x=10, y=320)
self.label3=Label(self.master, text="Re-encoded file? (If you download file from random
site, tick this)",bg="  # d9d9d9")
self.label3.place(x=10, y=350)
self.re_encoder=Checkbutton(self.master, text="Re-encoded", variable=self.re_encoded,
bg="#d9d9d9", onvalue=1,
offvalue=0)
self.re_encoder.place(x=10, y=370)
self.label4=Label(self.master, text="What kind of anime is this? Answer this and you can
skip all questions",
bg="#d9d9d9")
self.label4.place(x=10, y=400)
self.anime_type1=Radiobutton(self.master, text="I don't know. I never even watch trailer
of it before",
value=1, bg="#d9d9d9", variable=self.var3)
self.anime_type1.place(x=10, y=420)
self.anime_type2=Radiobutton(self.master, text="Flat and slow anime(New Game, K-On!,
All CGDCT anime goes here)", value=2,
bg="#d9d9d9", variable=self.var3)
self.anime_type2.place(x=10, y=440)
self.anime_type3=Radiobutton(self.master, text="Fast anime, battle scene(Shonen,
Demon Slayer)", value=3,
bg="#d9d9d9", variable=self.var3)
self.anime_type3.place(x=10, y=460)
self.anime_type4=Radiobutton(self.master,
text="Movie dark scene, ton of detail that can't be lose(Madoka Magica
Movie "
"3?)",
value=4, bg="#d9d9d9", variable=self.var3)
self.anime_type4.place(x=10, y=480)
self.anime_type5=Radiobutton(self.master, text="Just give me the best. I have 177013TB
of HDD(Please don't)",
value=5, bg="#d9d9d9", variable=self.var3)
self.anime_type5.place(x=10, y=500)
self.label5=Label(self.master,
text="Opus, AAC or Copy(Choose copy if you download from streaming site or
mini)",
bg="#d9d9d9")self.label5.place(x=10, y=530)
self.audio1=Radiobutton(self.master, text="Opus (Recommended for FLAC)", value=1,
bg="#d9d9d9", variable=self.
var4)
self.audio1.place(x=10, y=550)
self.audio2=Radiobutton(self.master,
text="AAC (Not recommended. Must build FFMPEG by yourself with nonfree flag)",
value=2, bg="#d9d9d9", variable=self.var4)
self.audio2.place(x=10, y=570)
self.audio3=Radiobutton(self.master, text="Copy(Use this if you download from
streaming site or mini)",
value=3, bg="#d9d9d9", variable=self.var4)
self.audio3.place(x=10, y=590)
self.label6=Label(self.master, text="You know why AAC isn't recommended?",
bg="#d9d9d9")
self.label6.place(x=10, y=620)
self.label7=Label(self.master, text="Because FFMPEG built-in AAC encoder suck. I need to
use FDK AAC instead",
bg="#d9d9d9")
self.label7.place(x=10, y=640)
self.label8=Label(self.master, text="AAC is good codec but Opus is better. It's transparent
at "
"128kbps", bg="#d9d9d9")
self.label8.place(x=10, y=660)
self.label9=Label(self.master, text="Just use Opus. It's almost 2022 already. Your device
very likely "
"supported it", bg="#d9d9d9")
self.label9.place(x=10, y=680)
self.convert_button=Button(self.master, text="Convert", command=self.convert)
self.convert_button.place(x=10, y=110)
self.quit_button=Button(self.master, text="Quit", command=self.quit)
self.quit_button.place(x=330, y=110)
def browse_input(self): self.input_path.set(filedialog.askopenfilename())
def browse_output(self):
self.output_path.set(filedialog.asksaveasfilename())
def convert(self):
audio=None
preset=None
anime_type=None
if self.input_path.get() == "":
messagebox.showerror("Error", "No input file selected")
elif self.output_path.get() == "":
messagebox.showerror("Error", "No output file selected")
else:
if self.output_path.get().endswith(".mkv"):
if self.var1.get() == 1:
crf="23"
elif self.var1.get() == 2:
crf="21"
elif self.var1.get() == 3:
crf="18"
elif self.var1.get() == 4:
crf="14"  # DON'T
else:
crf="21"
if self.var2.get() == 1:
preset="fast"
elif self.var2.get() == 2:
preset="slow"
elif self.var2.get() == 3:
preset="veryslow"
if self.var3.get() == 1:
anime_type="anime"
elif self.var3.get() == 2:
anime_type="sol"
elif self.var3.get() == 3:
anime_type="shonen"
elif self.var3.get() == 4:
anime_type="movie"
elif self.var3.get() == 5:
anime_type="masochist"if self.var4.get() == 1:
audio="opus"
elif self.var4.get() == 2:
audio="aac"
elif self.var4.get() == 3:
audio="copy"
if self.re_encoded.get() == 1:
re_encode=True
else:
re_encode=False
if anime_type == "anime" and re_encode is not True:
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=20:psy-rd=1:bframes=8:aq-mode=3", "-c:a",
"libopus", "-b:a",
"128k",
"-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "sol" and re_encode is not True:
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow", "-x265 -
params",
"crf=19:bframes=8:psy-rd=1:aq-mode=3:aq-strength=0.8:deblock=1,1", "-c:a",
"libopus", "-b:a",
"128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "shonen" and re_encode is not True:
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow", "-x265 -
params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aq-mode=3", "-c:a",
"libopus", "-b:a",
"128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "movie" and re_encode is not True:
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow", "-x265 -
params","crf=16:no-sao=1:bframes=8:psy-rd=1.5:psy-rdoq=3:aq-mode=3:ref=6", "-c:a",
"libopus", "-b:a",
"128k", "-vbr", "on", self.output_path.get()])  # psy-rdoq > 3 isn't recommended
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "masochist" and re_encode is not True:  # If you choose this. Sure! I
will maxed out
# everything. Prepare your PC though!!!
if messagebox.askyesno("Warning",
"This option is really only for masochist due to it render time and file "
"size.\nIf you have this level of PC, you shouldn't use this tool in the "
"first place\nAre you sure you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=5:aq-mode=3"
":deblock=-1,-1:ref=6",
"-c:a", "libopus", "-b:a", "192k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "anime" and re_encode is True:
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=20:psy-rd=1:bframes=8:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a",
"128k",
"-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "sol" and re_encode is True:
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow", "-x265 -
params",
"crf=19:bframes=8:psy-rd=1:aq-mode=3:aqstrength=0.8:deblock=1,1:constrained-intra=1", "-c:a",
"libopus", "-b:a",
"128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "shonen" and re_encode is True:
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow", "-x265 -
params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a",
"128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "movie" and re_encode is True:
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow", "-x265 -
params",
"crf=16:no-sao=1:bframes=8:psy-rd=1.5:psy-rdoq=3:aqmode=3:ref=6:constrained-intra=1", "-c:a",
"libopus", "-b:a",
"128k", "-vbr", "on", self.output_path.get()])  # psy-rdoq > 3 isn't recommended
messagebox.showinfo("Success", "Conversion completed")
elif anime_type == "masochist" and re_encode is True:  # If you choose this. Sure! I will
maxed out
# everything. Prepare your PC though!!!
messagebox.askyesno("Warning",
"This option is really only for masochist due to it render time and file "
"size.\nIf you have this level of PC, you shouldn't use this tool in the "
"first place\nAre you sure you want to continue?")
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=5:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libopus", "-b:a", "192k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
else:
if crf == "23" and preset == "fast" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libopus",
"-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "slow" and re_encode is not True and audio == "opus": subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libopus",
"-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "veryslow" and re_encode is not True and audio ==
"opus":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a", "libopus", "-
b:a", "128k",
"-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "fast" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libfdk_aac",
"-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "slow" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libfdk_aac",
"-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "veryslow" and re_encode is not True and audio ==
"aac":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a", "libfdk_aac",
"-m", "5",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "fast" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast", "-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"copy",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "slow" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"copy",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "veryslow" and re_encode is not True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3", "-c:a", "copy",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "fast" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libopus",
"-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "slow" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libopus",
"-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "veryslow" and re_encode is not True and audio ==
"opus":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a", "libopus", "-
b:a", "128k",
"-vbr", "on", self.output_path.get()])messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "fast" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libfdk_aac",
"-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "slow" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"libfdk_aac",
"-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "veryslow" and re_encode is not True and audio ==
"aac":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a", "libfdk_aac",
"-m", "5",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "fast" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"copy",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "slow" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a",
"copy",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")elif crf == "21" and preset == "veryslow" and re_encode is not True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3", "-c:a", "copy",
self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "fast" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "slow" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "veryslow" and re_encode is not True and audio ==
"opus":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "fast" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "slow" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow", "-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "veryslow" and re_encode is not True and audio ==
"aac":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "fast" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "slow" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "veryslow" and re_encode is not True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "fast" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params", "crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq"
"-mode=3:deblock=-1,-1:ref=6",
"-c:a", "libopus", "-b:a", "192k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "slow" and re_encode is not True and audio == "opus":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq"
"-mode=3:deblock=-1,-1:ref=6",
"-c:a", "libopus", "-b:a", "192k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "veryslow" and re_encode is not True and audio ==
"opus":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3:deblock "
"=-1,-1:ref=6",
"-c:a", "libopus", "-b:a", "192k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "fast" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq "
"-mode=3:deblock=-1,-1:ref=6",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "slow" and re_encode is not True and audio == "aac":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq "
"-mode=3:deblock=-1,-1:ref=6", "-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "veryslow" and re_encode is not True and audio ==
"aac":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3:deblock "
"=-1,-1:ref=6",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "fast" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"fast",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq"
"-mode=3:deblock=-1,-1:ref=6",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "slow" and re_encode is not True and audio == "copy":
subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq"
"-mode=3:deblock=-1,-1:ref=6",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "veryslow" and re_encode is not True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3:deblock"
"=-1,-1:ref=6",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")else:
if crf == "23" and preset == "fast" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "slow" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "veryslow" and re_encode is True and audio ==
"opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "fast" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fasta", "-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "slow" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "veryslow" and re_encode is True and audio ==
"aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "fast" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "23" and preset == "slow" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")elif crf == "23" and preset == "veryslow" and re_encode is True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=23:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "fast" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "slow" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "veryslow" and re_encode is True and audio ==
"opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")elif crf == "21" and preset == "fast" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "slow" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "veryslow" and re_encode is True and audio ==
"aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue?"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "fast" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")elif crf == "21" and preset == "slow" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "21" and preset == "veryslow" and re_encode is True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params", "crf=21:bframes=8:psy-rd=1:aq-mode=3:constrainedintra=1", "-c:a",
"copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "fast" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3:constrained-intra=1",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "slow" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3:constrained-intra=1",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "veryslow" and re_encode is True and audio ==
"opus":
if messagebox.askokcancel("Warning", "You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3:constrained-intra=1",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "fast" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3:constrained-intra=1",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "slow" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3:constrained-intra=1",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "veryslow" and re_encode is True and audio ==
"aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params", "crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aqmode=3:constrained-intra=1",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "fast" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aq-mode=3:constrainedintra=1",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "slow" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aq-mode=3:constrainedintra=1",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "18" and preset == "veryslow" and re_encode is True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params",
"crf=18:limit-sao:bframes=8:psy-rd=1.5:psy-rdoq=2:aq-mode=3:constrainedintra=1",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "fast" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "slow" and re_encode is True and audio == "opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "veryslow" and re_encode is True and audio ==
"opus":
if messagebox.askokcancel("Warning",
"You pick opus audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libopus", "-b:a", "128k", "-vbr", "on", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "fast" and re_encode is True and audio == "aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "slow" and re_encode is True and audio == "aac": if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3 "
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "veryslow" and re_encode is True and audio ==
"aac":
if messagebox.askokcancel("Warning",
"You pick aac audio codec while input file is encoded which is "
"strongly not recommended.\nDo you want to continue"):
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "libfdk_aac", "-m", "5", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "fast" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "fast",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "slow" and re_encode is True and audio == "copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "slow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1", "-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
elif crf == "14" and preset == "veryslow" and re_encode is True and audio ==
"copy":
subprocess.call(
["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset", "veryslow",
"-x265-params",
"crf=14:no-sao=1:no-strong-intra-smoothing=1:bframes=8:psy-rd=2:psyrdoq=3:aq-mode=3"
":deblock=-1,-1:ref=6:constrained-intra=1",
"-c:a", "copy", self.output_path.get()])
messagebox.showinfo("Success", "Conversion completed")
else:
messagebox.showerror("Error", "Please select a valid choice")
# else: subprocess.call(["ffmpeg", "-i", self.input_path.get(), "-c:v", "libx265", "-preset",
"slow",
# "-x265-params", "crf=23:psy-rd=1:bframe elif crf == "21" and preset ==
# "ultrafast" and re_encode is True and audio == "copy":"libopus", "-b:a", "128k", "-vbr",
"on",
# self.output_path.get()]) messagebox.showinfo("Success", "Conversion complete")
def on_closing(self):
if messagebox.askokcancel("Quit", "Do you want to quit?"):
self.master.destroy()
sys.exit()
def quit(self):
self.master.destroy()
sys.exit()
root=Tk()
app=App(root)
root.mainloop()
root.destroy()
sys.exit()
