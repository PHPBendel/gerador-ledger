# Gerador de arquivo ledger

Só um pequeno projeto para facilitar a importação de extrato para o formato usado pelo [ledger cli](https://www.ledger-cli.org). A ordem das colunas do extrato precisam ser: data;descrição;valor. O delimitador delimitador do formato csv está definido como padrão para ";". 

O arquivo `accounts.py ` é um mapa para descrição a ser encontrada no extrato e em qual conta no ledger a entrada deve ser colocada. 

Exemplo: 
```
"RECARGA CELULAR" : "Expenses:Phone credits",
"MUSEU" : "Expenses:Entertainment",
"TURISMO" : "Expenses:Travel Expenses",
"ESFIHA" : "Expenses:Food",
"CAFE" : "Expenses:Food",
``` 
