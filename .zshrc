# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH=/Users/user1/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="powerlevel9k/powerlevel9k"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-syntax-highlighting zsh-history-substring-search fasd colored-man-pages colorize)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
alias ohmyzsh="subl ~/.oh-my-zsh"

# For compilers to find zlib you may need to set:
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/zlib/lib"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/zlib/include"

# For pkg-config to find zlib you may need to set:
export PKG_CONFIG_PATH="${PKG_CONFIG_PATH} /usr/local/opt/zlib/lib/pkgconfig"

# Set DEFAULT_USER to your regular username to hide the “user@hostname” info when you’re logged in as yourself on your local machine.
# DEFAULT_USER="user1"

# Powerlevel9k settings. P9K_LEFT_PROMPT_ELEMENTS=(dir vcs)
P9K_LEFT_PROMPT_ELEMENTS=(dir vcs)
P9K_RIGHT_PROMPT_ELEMENTS=(time)

# Key bindings.
bindkey "[D" backward-word
bindkey "[C" forward-word

# Alises.
# open ~/.zshrc in using the default editor specified in $EDITOR
alias ec="subl $HOME/.zshrc"
# source ~/.zshrc
alias sc="source $HOME/.zshrc"
alias c="cat "
alias ll="ls -la"
alias pogoda="curl \"http://wttr.in/Krakow?lang=en\""
alias whenhome="python3 /Users/user1/work/scripts/whenhome.py"
alias wh="python3 /Users/user1/work/scripts/whenhome.py"
alias rmtrws="sh /Users/user1/work/scripts/rmtrws.sh"
alias regex="markdown-cli /Users/user1/work/scripts/REGEX.md"

SPACING="------------------------------------------------------------------------------------------------------------------"
PROVISIONING_HELP1="Xcode inserts the provisioning profile used to sign the application within the .app bundle."
PROVISIONING_HELP2="To find it, rename your .ipa to .zip, uncompress it with Finder, find the .app file in /Payload."
PROVISIONING_HELP3="\"Show Package Contents\" on the .app file and find the provisioning profile with the name embedded.mobileprovision."
PROVISIONING_HELP4="https://stackoverflow.com/questions/14881126/how-to-tell-what-profile-signing-certificate-was-used-to-sign-ipa"
alias provinfo="echo $SPACING && echo $PROVISIONING_HELP1 && echo $PROVISIONING_HELP2 && echo $PROVISIONING_HELP3 && echo $PROVISIONING_HELP4 && echo $SPACING && security cms -D -i "

# Java stuff.
# alias set-jdk6="export JAVA_HOME=$(/usr/libexec/java_home -v 1.6)"
alias jdk7="export JAVA_HOME=$(/usr/libexec/java_home -v 1.7)"
alias jdk8="export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)"
alias jdk11="export JAVA_HOME=$(/usr/libexec/java_home -v 11)"
alias jdk15="export JAVA_HOME=$(/usr/libexec/java_home -v 15)"
export JAVA_HOME=$(/usr/libexec/java_home -v 1.11)

# Android stuff.
export ANDROID_HOME=/Users/user1/Library/Android/sdk
export PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools"
export GRADLE_HOME="$HOME/.gradle"
alias nexus5x="~/Library/Android/sdk/tools/emulator -avd Nexus_5X_API_26"
alias aliases="tail -n +\`awk '/Alises/{print NR}' ~/.zshrc\` ~/.zshrc"
alias tab="open . -a iterm"

timezsh() {
  shell=${1-$SHELL}
  for i in $(seq 1 10); do /usr/bin/time $shell -i -c exit; done
}
