if [[ ! $DISPLAY && $XDG_VTNR -eq 1 ]]; then
  exec startx
elif [[ ! $DISPLAY && $XDG_VTNR -eq 2 ]]; then
  exec startx $HOME/.xinitrc-2
fi
