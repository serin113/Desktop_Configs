(wal -rt &)

# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

autoload -Uz run-help
autoload -Uz run-help-git
autoload -Uz run-help-svn
#autoload -Uz run-help-svk
unalias run-help
alias help=run-help

autoload -Uz promptinit
promptinit
prompt agnoster

#source /usr/share/doc/pkgfile/command-not-found.zsh

zstyle ':completion:*' completer _complete _match _approximate
zstyle ':completion:*:match:*' original only
zstyle ':completion:*:approximate:*' max-errors 1 numeric
zstyle ':completion:*:functions' ignored-patterns '_*'

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias xyzzy='echo Nothing happens.'
alias java='java -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true'

alias search='sudo updatedb; locate'

#screenfetch -L
