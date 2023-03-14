# Comenzi pentru a porni proiectul:
1. `pip install -r requirements.txt`
2. `python manage.py makemigrations`

### Detalii:

Deja este prezenta o baza de date in acest proiect cu date create.
Este create un superadmin cu credentialele:

- Username: denis
- Password: 1

### Sarcina

- [ ] Trebuie sa intri in admin si sa adaugi un debitor
- [ ] In postman apelezi ruta `http://localhost:8000/debitors/` cu metoda `GET`, trebuie sa returneze:

``` 
{
    "debitors": []
}
```

- [ ] Datele care le salvam in baza de date nu sunt destule, mai avem nevoie sa salvam si anul nasterii (birthdate), pentru asta trebuie sa adaugam un camp nou
- [ ] Daca ai adaugat campul acum cand apelezi metoda get la ruta `http://localhost:8000/debitors/` o sa observi ca noul camp nu-i prezent in date despre debitor, trebuie adaugat

