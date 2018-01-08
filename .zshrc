cat $HOME/.cache/wal/sequences

autoload -Uz run-help
autoload -Uz run-help-git
autoload -Uz run-help-svn
autoload -Uz run-help-sudo
autoload -Uz run-help-ip
#autoload -Uz run-help-svk
unalias run-help
alias help=run-help

autoload -Uz compinit promptinit
compinit -i
promptinit
source $HOME/agnoster.zsh-theme

source /usr/share/doc/pkgfile/command-not-found.zsh

zstyle ':completion:*' completer _complete _match _approximate
zstyle ':completion:*' menu select
zstyle ':completion:*:match:*' original only
zstyle ':completion:*:approximate:*' max-errors 1 numeric
zstyle ':completion:*:functions' ignored-patterns '_*'

bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line

setopt complete_in_word
setopt always_to_end

source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=8'
ZSH_AUTOSUGGEST_ORIGINAL_WIDGET_PREFIX=autosuggest-orig-
ZSH_AUTOSUGGEST_STRATEGY=default
ZSH_AUTOSUGGEST_CLEAR_WIDGETS=(
	history-search-forward
	history-search-backward
	history-beginning-search-forward
	history-beginning-search-backward
	history-substring-search-up
	history-substring-search-down
	up-line-or-history
	down-line-or-history
	accept-line
)
ZSH_AUTOSUGGEST_ACCEPT_WIDGETS=(
	forward-char
	end-of-line
	vi-forward-char
	vi-end-of-line
	vi-add-eol
)
ZSH_AUTOSUGGEST_EXECUTE_WIDGETS=(
)
ZSH_AUTOSUGGEST_PARTIAL_ACCEPT_WIDGETS=(
	forward-word
	emacs-forward-word
	vi-forward-word
	vi-forward-word-end
	vi-forward-blank-word
	vi-forward-blank-word-end
)
ZSH_AUTOSUGGEST_IGNORE_WIDGETS=(
	orig-\*
	beep
	run-help
	set-local-history
	which-command
	yank
)
ZSH_AUTOSUGGEST_BUFFER_MAX_SIZE=
ZSH_AUTOSUGGEST_ASYNC_PTY_NAME=zsh_autosuggest_pty

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
DEFAULT_USER=$(whoami)

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

#https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'

alias pacaur='printf "Using trizen instead, mumble mumble...\n"; trizen'
