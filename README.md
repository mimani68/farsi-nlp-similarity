# NLP find similarity of two text

# A) Preprocessing and dictionary creation

```bash
python3 farsi-preprocessing.py > dataset/<TOPIC>-preproccesed.txt
```

# B) Find similarity in `<TOPIC>.txt` file

```bash
python3 similarity-gensim.py > <TOPIC>-result.txt
```