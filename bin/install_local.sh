python3 setup.py build
python3 setup.py install --record .datas/install_record.txt
# for pyenv
if [ ! -d "~/.pyenv" ]; then
pyenv rehash && hash -r
fi
