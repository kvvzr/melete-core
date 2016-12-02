# melete-core
Automatic Composition from Japanese Lyrics

## Installation

### Ubuntu

```
# install unidic
$ apt install mecab libmecab-dev
$ wget -O unidic-mecab-2.1.2_src.zip "http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Funidic%2F58338%2Funidic-mecab_kana-accent-2.1.2_src.zip"
$ unzip unidic-mecab-2.1.2_src.zip
$ cd unidic-mecab_kana-accent-2.1.2_src
$ ./configure
$ make
$ sudo make install
$ vi /etc/mecabrc
# dicdir = /usr/lib/mecab/dic/unidic

# install melete-core
$ pip install git+https://github.com/kvvzr/melete-core
```
