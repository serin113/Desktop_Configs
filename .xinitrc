#!/bin/sh

xrdb -merge ~/.Xresources
source /etc/X11/xinit/xinitrc.d/50-systemd-user.sh
export GDK_SCALE=1
export GDK_DPI_SCALE=1
export QT_SCREEN_SCALE_FACTORS=1
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_SCALE_FACTOR=1
#xrandr --dpi 226
#xrandr --dpi 113
xrandr --dpi 96
exec i3
