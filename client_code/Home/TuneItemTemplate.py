from anvil import *


class TuneItemTemplate(GridPanel):
    def __init__(self, item, **properties):
        super().__init__()
        self.item = item
        font = "Roboto"
        font_size = 16
        self.add_component(
            Label(text=item["name"], font_size=font_size, font=font),
            width_xs=4,
            col_xs=0,
        )
        self.add_component(
            Label(text=item["type"], font_size=font_size, font=font),
            width_xs=4,
            col_xs=4,
        )
