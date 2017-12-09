(wal -rt &)

autoload -Uz run-help
autoload -Uz run-help-git
autoload -Uz run-help-svn
autoload -Uz run-help-sudo
autoload -Uz run-help-ip
#autoload -Uz run-help-svk
unalias run-help
alias help=run-help

autoload -Uz compinit promptinit
compinit
promptinit
source $HOME/agnoster.zsh-theme

source /usr/share/doc/pkgfile/command-not-found.zsh

zstyle ':completion:*' completer _complete _match _approximate
zstyle ':completion:*' menu select
zstyle ':completion:*:match:*' original only
zstyle ':completion:*:approximate:*' max-errors 1 numeric
zstyle ':completion:*:functions' ignored-patterns '_*'

source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
DEFAULT_USER=vulpes

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
