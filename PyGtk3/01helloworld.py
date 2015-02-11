__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import Gtk, Gdk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World", type=Gtk.WindowType.TOPLEVEL)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.stick()

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.set_resizable(True)
win.show_all()
Gtk.main()