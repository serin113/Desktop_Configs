#
# ~/.bashrc
#

# If not running interactively, don't do anything


#[[ $- != *i* ]] && return

export LC_ALL=en_PH.UTF-8
export LC_CTYPE=en_PH.UTF-8
export LANG=en_PH.UTF-8
LC_ALL=$LANG

[ -z "$PS1" ] && return

HISTCONTROL=ignoreboth
shopt -s histappend
HISTSIZE=2000
HISTFILESIZE=2000
shopt -s checkwinsize

source /usr/share/doc/pkgfile/command-not-found.bash

case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

man() {
    env \
    LESS_TERMCAP_mb=$'\e[01;31m' \
    LESS_TERMCAP_md=$'\e[01;31m' \
    LESS_TERMCAP_me=$'\e[0m' \
    LESS_TERMCAP_se=$'\e[0m' \
    LESS_TERMCAP_so=$'\e[01;44;33m' \
    LESS_TERMCAP_ue=$'\e[0m' \
    LESS_TERMCAP_us=$'\e[01;32m' \
    man "$@"
}

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

alias ll='ls -alF'
alias la='la -A'
alias l='ls -CF'

function nonzero_return() {
	RETVAL=$?
	[ $RETVAL -ne 0 ] && echo "$RETVAL "
}

#PS1="\[\e[1;31m\]\`nonzero_return\`\[\e[1;32m\]\u\[\e[0;32m\]@\[\e[1;32m\]\h\[\e[0m\] \[\e[0;39m\]\$(pwd)\[\e[0m\] \[\e[1;32m\]\$\[\e[0m\] "
#PS1="\[\e[1;31m\]\`nonzero_return\`\[\e[1;32m\]\u\[\e[0m\] \[\e[0;39m\]\$(pwd)\[\e[0m\] \[\e[1;32m\]\$\[\e[0m\] "
PS1="\[\e[1;31m\]\`nonzero_return\`\[\e[0;32m\]\u@\h\[\e[0m\] \[\e[32;49;7m\] \$(pwd) \[\e[0;27m\] \[\e[1;32m\]\$\[\e[0m\] "
PS2='\[\e[1;32m\]>\[\e[0m\] '

#PS1='[\u@\h \W]\$ '

alias xyzzy='echo Nothing happens.'
alias java='java -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true'

screenfetch
