__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import Gtk


class BoxesTest(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,
                            title="Boxes",
                            window_position=Gtk.WindowPosition.CENTER,
                            default_width=400,
                            default_height=300)
        self._init_ui()

    def _init_ui(self):
        self._vbox = Gtk.Box(spacing=6,
                             border_width=6,
                             orientation=Gtk.Orientation.VERTICAL)
        self.add(self._vbox)

        self._hbox = Gtk.Box(homogeneous=True,
                             spacing=6,
                             border_width=6,
                             orientation=Gtk.Orientation.HORIZONTAL)
        self._vbox.pack_end(self._hbox, False, False, 6)
        self._vbox.set_halign(Gtk.Align.CENTER)

        self._btn_hello = Gtk.Button(label="Hello")
        self._btn_hello.connect("clicked", self._on_hello)
        self._hbox.pack_start(self._btn_hello, True, True, 0)

        self._btn_goodbye = Gtk.Button(label="Goodbye")
        self._btn_goodbye.connect("clicked", self._on_goodbye)
        self._hbox.pack_start(self._btn_goodbye, True, True, 0)

    def _on_hello(self, button):
        print("Hello")

    def _on_goodbye(self, button):
        print("Goodbye")


wnd = BoxesTest()
wnd.connect("delete-event", Gtk.main_quit)
wnd.show_all()
Gtk.main()