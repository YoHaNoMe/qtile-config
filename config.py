# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
import os
import socket
# from libqtile.widget import backlight

from typing import List  # noqa: F401

mod = "mod4"
terminal="alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    # add key to navigate to certain layout
    # Navigate to Tile
    Key([mod, "control"], "t", lazy.to_layout_index(0)),
    # Navigate to Max
    Key([mod, "control"], "m", lazy.to_layout_index(1)),
    # Key([], "XF86MonBrightnessUp", lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.UP)),
    # Key([], "XF86MonBrightnessDown", lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.DOWN)),
    Key([mod], "comma", lazy.to_screen(0)),
    Key([mod], "period", lazy.to_screen(1)),
]

groups = [Group(i, persist=False) for i in "asdf1234"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layout_theme = {
    "border_focus": "#691D1D",
    "margin": 2,
    "border_width": 3,
}


layouts = [
    layout.Tile(add_after_last=True, add_on_top=False,**layout_theme),  # I want this
    layout.Max(),
    layout.MonadTall(**layout_theme), # I want this
    layout.MonadWide(**layout_theme), # I want this
    layout.RatioTile(**layout_theme), # I want this
    layout.Matrix(**layout_theme), # I want this
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()



colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

bar_theme = {
"background": colors[0]
}

group_box = widget.GroupBox(font="DejaVu Bold",
        fontsize = 9,
        margin_y = 3,
        margin_x = 0,
        padding_y = 5,
        padding_x = 5,
        borderwidth = 3,
        active = colors[2],
        inactive = colors[2],
        rounded = False,
        highlight_color = colors[1],
        highlight_method = "line",
        this_current_screen_border = colors[3],
        this_screen_border = colors [4],
        other_current_screen_border = colors[0],
        other_screen_border = colors[0],
        foreground = colors[2],
        background = colors[0]
)

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

fake_screens = [
    # Main Screen (My laptop)
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.Sep(),
                widget.GroupBox(font="DejaVu Bold",
                        fontsize = 9,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 5,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors[4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0]
                ),
                widget.Spacer(length=bar.STRETCH),
                # widget.Sep(),
                # widget.WindowName(),
                # widget.Wlan(interface='wlp3s0'),
                # widget.NetGraph(border_color='E0E0E0', graph_color='00CC00', frequency=5),
                # widget.Sep(),
                widget.TextBox('Battery:'),
                widget.Battery(show_short_text=False, format='{percent:2.0%} | {hour:d}h:{min:02d}m'),
                widget.Sep(),
                widget.TextBox("Brightness:"),
                widget.Backlight(backlight_name='intel_backlight'),
                widget.Sep(),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            30,
            **bar_theme
        ),
        x=0,
        y=0,
        width=1920,
        height=1080,
    ),
    # Second Screen
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(),
                widget.CurrentLayout(),
                widget.Sep(),
                group_box,
                widget.Prompt(
                    prompt=prompt,
                    font="DejaVu italic",
                    padding=10,
                    foreground = colors[3],
                    background = colors[1],
                ),
                # widget.Sep(),
                widget.WindowName(),
                # widget.Sep(),
                # widget.TextBox('Updates:'),
                # widget.Pacman(foreground='00CC00', unavailable='CC0000', execute='pacman -Syu'),
                # widget.Sep(),
                widget.Systray(),
                widget.Clock(format='%I:%M %p'),
            ],
            25,
            **bar_theme
        ),
        x=1920,
        y=311,
        width=1360,
        height=768,
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
follow_mouse_focus = False
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
