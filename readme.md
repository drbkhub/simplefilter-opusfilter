# Overview

filtering wikimatrix (EN/RU) with opusfilter ([docs](https://helsinki-nlp.github.io/OpusFilter/index.html))


## Used: 
1. ```HtmlTagFilter```
2. ```AlphabetRatioFilter```
3. ```LongWordFilter```
4. ```TerminalPunctuationFilter```
5. ```NonZeroNumeralsFilter```
6. ```LongestCommonSubstringFilter```
7. ```SimilarityFilter```
8. ```LanguageIDFilter```
9. ```CharacterScoreFilter```
10. ```NonPairedBracketsFilter``` (custom.py)
11. ```LatinCyrillicWordNormalizer``` (custom.py)


# Run

```bash
$ . setvariables.sh # use venv in root of project path
$ opusfilter --overwrite simple_filter.yml
```
## output files:

```datasets/WikiMatrix.en-ru.result.ru```
```datasets/WikiMatrix.en-ru.result.en```

# Installation
```bash
# on linux and python 3.8.16 works well
pip install -r requirements.txt
```
before running, set a variable in the project root to use custom filters in  ```custom.py```


```bash
export PYTHONPATH=$(pwd)
```

For using word alignment filters:
```bash
# root directory, which contains the Python scripts align.py and makepriors.py
export EFLOMAL_PATH=
```





# Optional libraries and tools

For using n-gram language model filters, you need to install VariKN (https://github.com/vsiivola/variKN) and its Python wrapper. Include the library files compiled to build/lib/python to your Python library path (e.g. by setting the PYTHONPATH environment variable).

For using word alignment filters, you need to install elfomal (https://github.com/robertostling/eflomal) and set environment variable EFLOMAL_PATH to eflomal's root directory, which contains the Python scripts align.py and makepriors.py.
