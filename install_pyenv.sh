#!/bin/bash
PY_VERSION="3.6.2"

sudo yum -y install git
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install $PY_VERSION
pyenv global $PY_VERSION
exec $SHELL -l
