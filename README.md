# Guanta
Where are my taxes? (WAMTA)


## Dependencies
To install pipreqs:
```sh
pip install pipreqs
```
Generate requirents.txt
```sh
pipreqs .
```
Install dependencies
```sh
cd ocds-ec-client
pip install -r requirements.txt
```

## Flow

### Consume OCDS header
```sh
python main.py $buyer_name
```
### Consume OCDS details
```sh
python ocds.py
```