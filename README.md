# Find similarity of two text using `GENSIM`

## Dataset

### Marketing in `Farsi`

| Parameter | Number | File |
|:---:|:---:|:---:|
| Word count | 8677 | dataset/marketing.txt |
| line | 132 | dataset/marketing.txt |
| Dataset size | 80 kb | dataset/marketing.txt |

## Usage

### A) Preprocessing and dictionary creation

```bash
python3 preprocessing.py > dataset/<TOPIC>-preproccesed.txt
```

### B) Find similarity in `<TOPIC>.txt` file

```bash
python3 similarity.py > <TOPIC>-result.txt
```