# Parse-tree-by-API (all code in views and utils)

### Example of .env:
> SECRET_KEY=PUT_YOUR_SECRET_KEY_WITHOUT_QUOTES
```bash
    pip install -r requirements.txt
```
```
    python manage.py migrate
```
```bash
    ./manage.py runserver
```

Basic Request: http://127.0.0.1:8000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )
