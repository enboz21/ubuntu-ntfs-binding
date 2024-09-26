#!/bin/bash
mkdir ~/.local/bin
echo Which one
echo 1.TR  2.EN
read a
if [ $a -eq 1 ]; then
  cp tr.py binding
  mv binding ~/.local/bin/
  chmod +x ~/.local/bin/binding
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

elif [ $a -eq 2  ]; then
  cp en.py binding
  mv binding ~/.local/bin/
  chmod +x ~/.local/bin/binding
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
fi