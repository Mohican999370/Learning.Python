__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World", type=Gtk.WindowType.TOPLEVEL)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.stick()

        self.button = Gtk.Button()
        self.button.set_label("Fußbälle")
        self.button.set_halign(Gtk.Align.CENTER)
        self.button.set_valign(Gtk.Align.CENTER)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

        print(dir(self.props))

    def on_button_clicked(self, widget):
        print("Fußbälle")


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.set_resizable(True)
win.show_all()
Gtk.main()