from libqtile.config import Key
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
  
    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "d", lazy.spawn("dmenu_run -i"), desc="Dmenu app"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # SysKeys
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),



    # ROFI
    Key([mod], "v", lazy.spawn("rofi -font 'hack 15' -modi 'clipboard:~/.config/qtile/paste_modi.sh' -show clipboard"), desc="clipboard manager"),
    
    # POGRAMAS
    Key([mod], "b", lazy.spawn("chromium"), desc="Launch FURROFOX OwO"),
    Key([mod], "r", lazy.spawn("kitty sh -c 'ranger'"), desc="Launch ranger"),

    # Multimedia
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="mute"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="subir volumen"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="bajar volumen"),
    Key([], "Pause", lazy.spawn("playerctl play-pause"), desc="play/pause everywhere"), # "Pause" is how my HP ProBook Regonize the pause key, u can change it
    
    # Brightness - For some reason, the brightness keys doesn't works in my HP ProBook
    Key(["control"], "F6", lazy.spawn("brightnessctl set +10%"), desc="subirbrillo"),
    Key(["control"], "F5", lazy.spawn("brightnessctl set 10%-"), desc="bajarbrillo"),

    # SCREENSHOTS
    Key([], "Print", lazy.spawn("scrot -e 'mv $f ~/Imágenes/SCREENSHOTS/'"), desc="tomar screenshot y guardar en carpeta de capturas"),
    Key(["control"], "Print", lazy.spawn("scrot -s '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"), desc="sec. de la pantalla"),
]
