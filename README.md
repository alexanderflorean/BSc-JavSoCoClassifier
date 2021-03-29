# BSc-JavSoCoClassifier
A BSc project to find software architectural concerns in Java source code through Machine Learning  
The environment use Python 3.8.5  


To start working in the environment, run following to install required packages:   
`pip3 install -r requirements.txt`

---

#### preprocess settings
The preprocess settings are defined in the `config.yaml`, where each setting
contains a list of lists. 
The first item describes what to extract from the raw source 
file, then the following strings is the parsing of the said extraction.  

E.g. `[['lib', 'tow', 'jk', 'scw','lc', 'stem'],['pac', 'tow', 'jk']]`  
First list, extracts the imports, tokenizes the words, removes java keywords, 
separate composite words, lower case, then stemmize the words.  
Second list, extracts packages, tokenizes them, remove java keywords.  

All the settings are described down below.  

```
settings = [
        ['extraction', 'parsing' ... ,'parsing],
        ...,
        ['extraction', 'parsing']
    ]
```
#### Extraction options
* Raw data: 'raw'
* Classes: 'c'
* Public methods: 'pm'
* Public variables/objects: 'pv'
* Import: 'lib'
* Packages: 'pac'
* Comments: 'com'
* Clear chosen settings from list: 'clear'

#### Parsing options
* Lower case: 'lc'
* Remove single characters:  'sc'
* Remove stop words: 'sw'
* Remove java keywords: 'jk'
* Remove numbers: 'nu'
* Separate compound words: 'scw'
* Stem words: 'stem'
* Clear chosen settings from list: 'clear'

___
