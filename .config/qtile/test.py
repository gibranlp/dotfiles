from functions import *
# Popup Widgets
def show_keyboard_layout(qtile):
    controls = [
        PopupWidget(
            widget=widget.CPUGraph(),
            width=0.45,
            height=0.45,
            pos_x=0.05,
            pos_y=0.05
        ),
        PopupWidget(
            widget=widget.NetGraph(),
            width=0.45,
            height=0.45,
            pos_x=0.5,
            pos_y=0.05
        ),
        PopupWidget(
            widget=widget.MemoryGraph(),
            width=0.9,
            height=0.45,
            pos_x=0.05,
            pos_y=0.5
        )
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
        close_on_click=False
    )
    layout.show(centered=True)


show_keyboard_layout(qtile)