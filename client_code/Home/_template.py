from anvil import *
from TuneItemTemplate import TuneItemTemplate


class HomeTemplate(HtmlPanel):
    def init_components(self, **properties):
        # Initialise HtmlPanel
        super().__init__()
        # Set the html template for the app
        self.html = "@theme:standard-page.html"

        # main
        #################################################################
        self.main = GridPanel(spacing_above="small", spacing_below="small")
        row = 0
        empty = Label(text="")
        self.main.add_component(empty, row=row, width_xs=12, col_xs=0)
        self.add_component(self.main)

        #################################################################
        row = 1
        font_size = 64
        font = "Inknut Antiqua"
        self.title = Label(text="LOERIC", font_size=font_size, font=font, align="left")
        self.main.add_component(self.title, row=row, width_xs=7, col_xs=1)

        font_size = 24
        font = "Roboto"
        self.about = Label(
            text="About",
            font_size=font_size,
            font=font,
            align="center",
            spacing_above="large",
        )
        self.main.add_component(self.about, row=row, width_xs=1, col_xs=8)

        self.how_to = Label(
            text="How-To",
            font_size=font_size,
            font=font,
            align="center",
            spacing_above="large",
        )
        self.main.add_component(self.how_to, row=row, width_xs=1, col_xs=9)

        self.contact = Label(
            text="Contact",
            font_size=font_size,
            font=font,
            align="center",
            spacing_above="large",
        )
        self.main.add_component(self.contact, row=row, width_xs=1, col_xs=10)

        #################################################################
        row = 2
        self.all_settings = LinearPanel()
        self.main.add_component(self.all_settings, row=row, width_xs=7, col_xs=1)

        #################################################################

        row = 2
        self.tune_selector = LinearPanel()
        self.main.add_component(self.tune_selector, row=row, width_xs=3, col_xs=8)

        #################################################################

        self.audio_midi_settings = GridPanel(
            spacing_above="small", spacing_below="small"
        )
        self.all_settings.add_component(self.audio_midi_settings)

        font_size = 16
        row = 0
        self.text_audio_select = Label(
            text="Audio Input", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.text_audio_select, row=row, width_xs=1, col_xs=0
        )

        self.audio_select = DropDown(
            placeholder="Select...", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.audio_select, row=row, width_xs=2, col_xs=1
        )

        self.text_midi_select_in = Label(
            text="MIDI Input", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.text_midi_select_in, row=row, width_xs=1, col_xs=3
        )
        self.midi_select_in = DropDown(
            placeholder="Select...", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.midi_select_in, row=row, width_xs=2, col_xs=4
        )

        self.text_midi_select_out = Label(
            text="MIDI Output", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.text_midi_select_out, row=row, width_xs=1, col_xs=6
        )
        self.midi_select_out = DropDown(
            placeholder="Select...", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.midi_select_out, row=row, width_xs=2, col_xs=7
        )

        self.text_midi_select_out_ch = Label(
            text="MIDI Channel", font_size=font_size, font=font, align="center"
        )
        self.audio_midi_settings.add_component(
            self.text_midi_select_out_ch, row=row, width_xs=1, col_xs=9
        )
        self.midi_select_out_ch = DropDown(
            items={str(i): i for i in range(1, 17)},
            font_size=font_size,
            font=font,
            align="center",
        )
        self.audio_midi_settings.add_component(
            self.midi_select_out_ch, row=row, width_xs=1, col_xs=10
        )

        #################################################################

        color = "#DAEBC2"
        self.user_visual = Canvas(background=color)
        self.all_settings.add_component(self.user_visual)

        #################################################################
        self.loeric_settings = GridPanel(spacing_above="small", spacing_below="small")
        self.all_settings.add_component(self.loeric_settings)

        font_size = 16
        row = 0
        self.text_instrument_select = Label(
            text="Instrument", font_size=font_size, font=font, align="center"
        )
        self.loeric_settings.add_component(
            self.text_instrument_select, row=row, width_xs=1, col_xs=0
        )

        self.instrument_select = DropDown(
            items={
                "Flute": "flute",
                "Accordion": "accordion",
                "Fiddle": "fiddle",
                "Piano": "piano",
            },
            font_size=font_size,
            font=font,
            align="center",
        )
        self.loeric_settings.add_component(
            self.instrument_select, row=row, width_xs=2, col_xs=1
        )

        self.text_level_select = Label(
            text="Level", font_size=font_size, font=font, align="center"
        )
        self.loeric_settings.add_component(
            self.text_level_select, row=row, width_xs=1, col_xs=3
        )
        self.level_select = DropDown(
            items={"Beginner": 0, "Intermediate": 1, "Expert": 2},
            font_size=font_size,
            font=font,
            align="center",
        )
        self.loeric_settings.add_component(
            self.level_select, row=row, width_xs=2, col_xs=4
        )

        self.text_resp_select = Label(
            text="Responsiveness", font_size=font_size, font=font, align="center"
        )
        self.loeric_settings.add_component(
            self.text_resp_select, row=row, width_xs=2, col_xs=6
        )
        self.resp_select = DropDown(
            items={"Fast": 0.8, "Normal": 0.5, "Slow": 0.25},
            font_size=font_size,
            font=font,
            align="center",
        )
        self.loeric_settings.add_component(
            self.resp_select, row=row, width_xs=1, col_xs=8
        )

        self.text_impact_select = Label(
            text="Impact", font_size=font_size, font=font, align="center"
        )
        self.loeric_settings.add_component(
            self.text_impact_select, row=row, width_xs=1, col_xs=9
        )
        self.impact_select = DropDown(
            items={"Human Only": 1, "Normal": "0.5", "LOERIC Only": 0},
            font_size=font_size,
            font=font,
            align="center",
        )
        self.loeric_settings.add_component(
            self.impact_select, row=row, width_xs=2, col_xs=10
        )

        #################################################################

        self.loeric_visual = Canvas(background=color)
        self.all_settings.add_component(self.loeric_visual)

        #################################################################

        self.player_visual = Canvas(background=color)
        self.all_settings.add_component(self.player_visual)

        #################################################################

        self.other_settings = GridPanel(spacing_above="small", spacing_below="small")
        self.all_settings.add_component(self.other_settings)

        row = 0
        font_size = 24
        self.export_button = Button(text="EXPORT", font=font, font_size=font_size)
        self.other_settings.add_component(
            self.export_button, row=row, width_xs=2, col_xs=0
        )

        #################################################################

        self.search_tune = TextBox(font=font, font_size=font_size)
        self.tune_selector.add_component(self.search_tune)

        font_size = 16
        self.tune_list = RepeatingPanel(item_template=TuneItemTemplate)
        self.tune_list.items = [{"name": 10 * str(i), "type": "jig"} for i in range(10)]
        self.tune_selector.add_component(self.tune_list)
