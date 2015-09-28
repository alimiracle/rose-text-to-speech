import signal
import subprocess
import os
from gi.repository import Gtk
window = Gtk.Window(title="Rose Text to Speech")
window.set_border_width(10)
window.connect("destroy", lambda w: Gtk.main_quit())
hbox = Gtk.Box(spacing=6)
window.add(hbox)
textview = Gtk.TextView()
hbox.pack_start(textview, True, True, 0)
def p(button):
  global po
  text = textview.get_buffer()
  start = text.get_start_iter()
  end = text.get_end_iter()
  input =text.get_text(start, end, include_hidden_chars=1)
  file=open("file", "w+")
  print(input, end="", file=file)
  fest="festival --tts "
  text=fest+"file"
  po = subprocess.Popen(text, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 
def ex(button1):
  exit()
def st(button2):
  os.killpg(po.pid, signal.SIGTERM)  # Send the signal to all the process groups

button = Gtk.Button.new_with_label("Play")
button.connect("clicked", p)
hbox.pack_start(button, True, True, 0)
button1 = Gtk.Button.new_with_label("Stop")
button1.connect("clicked", st)
hbox.pack_start(button1, True, True, 0)
button2 = Gtk.Button.new_with_label("Exit")
button2.connect("clicked", ex)
hbox.pack_start(button2, True, True, 0)
window.show_all()
Gtk.main()
