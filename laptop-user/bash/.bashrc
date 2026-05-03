#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

fastfetch

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

alias neofetch="fastfetch"
. "$HOME/.cargo/env"

alias heaptrack="heaptrack -o /tmp/heaptrack.gz"

export TERM=xterm
export CARGO_BUILD_JOBS=6

export PATH="$PATH:/home/goldy/.local/bin"