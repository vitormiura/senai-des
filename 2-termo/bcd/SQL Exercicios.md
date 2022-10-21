# Exercicios SQL

1)
```txt
Plano relaciona com número.
```

3)  
```sql
SELECT associado.Nome, plano.Descricao
FROM associado 
INNER JOIN plano
ON associado.Plano = plano.Numero
```
3) 
```sql
SELECT COUNT(plano)
FROM associado
WHERE plano = 'B1';
```
4) 
```sql
SELECT * FROM associado 
INNER JOIN plano
ON associado.Plano = plano.Numero
```
5) 
```sql
SELECT * FROM associado 
WHERE cidade='COTIA'
OR cidade='DIADEMA'
```
6) 
```sql
SELECT associado.Nome, associado.Plano, plano.Valor from associado 
INNER JOIN plano on associado.Plano = plano.Numero 
WHERE associado.Cidade='BARUERI' AND associado.Plano='M1'
```
7) 
```sql
SELECT associado.Nome, associado.Plano, plano.Valor from associado
INNER JOIN plano on associado.Plano = plano.Numero 
WHERE associado.Cidade='SAO PAULO'
```
8) 
```sql
SELECT * from associado INNER JOIN plano on associado.Plano = plano.Numero WHERE associado.Nome LIKE '%SILVA%'
```
9) 
```sql
UPDATE plano SET plano.Valor = plano.Valor + (plano.Valor*0.1) WHERE plano.Numero = 'B1' OR plano.Numero = 'B2' OR plano.Numero = 'B3';
UPDATE plano SET plano.Valor = plano.Valor + (plano.Valor*0.05) WHERE plano.Numero = 'E1' OR plano.Numero = 'E2' OR plano.Numero = 'E3';
UPDATE plano SET plano.Valor = plano.Valor + (plano.Valor*0.03) WHERE plano.Numero = 'M1' OR plano.Numero = 'M2' OR plano.Numero = 'M3';
```
10) 
```sql
UPDATE associado 
SET associado.Plano = 'E3' 
WHERE associado.Nome = 'PEDRO JOSE DE OLIVEIRA';
```
11) 
```sql
SELECT COUNT(plano) FROM associado
WHERE plano = 'E3';
```
12) 
```sql
SELECT associado.Nome, plano.Valor FROM associado 
INNER JOIN plano ON plano.Numero = associado.Plano
WHERE associado.Plano = 'B1' OR associado.Plano = 'E1' OR associado.Plano = 'M1';
```
13) 
```sql
SELECT associado.Nome FROM associado
INNER JOIN plano ON plano.Numero = associado.Plano
WHERE plano.Descricao
LIKE 'EXECUTIVO%';
```
14) 
```sql
SELECT associado.Nome FROM associado
INNER JOIN plano ON plano.Numero = associado.Plano
WHERE plano.Descricao
LIKE 'BASICO%' or 'MASTER%';
```
15) 
```sql
DELETE FROM associado
WHERE associado.Cidade='SANTO ANDRE';
```
16) 
```sql
SELECT associado.Plano, associado.Nome, plano.Valor 
FROM associado
INNER JOIN plano ON plano.Numero = associado.Plano
WHERE associado.Cidade = 'SAO PAULO' AND associado.Plano = 'M2' OR associado.Plano = 'M3'
ORDER BY associado.Nome;
```
17) 
```sql
SELECT * FROM associado
INNER JOIN plano
ON associado.Plano = plano.Numero
ORDER BY associado.Plano
```
18) 
```sql
SELECT * FROM associado
INNER JOIN plano
ON associado.Plano = plano.Numero
ORDER BY associado.Plano ASC, associado.Nome DESC
```
19) 
```sql
SELECT * FROM associado
INNER JOIN plano
ON associado.Plano = plano.Numero
WHERE NOT plano.Descricao LIKE "MASTER%";
```
20) 
```sql
SELECT * FROM associado
INNER JOIN plano
ON associado.Plano = plano.Numero
ORDER BY associado.Nome
```
21) 
```sql
SELECT * FROM plano
WHERE plano.Valor BETWEEN 300 AND 500
```
22) 
```sql
SELECT * FROM associado
INNER JOIN plano
ON associado.Plano = plano.Numero
WHERE associado.Nome LIKE "%AMARAL%";
```
23) 
```sql
SELECT * FROM associado
WHERE associado.Cidade = "DIADEMA";
```
24) 
```sql
UPDATE plano
SET plano.Valor = plano.Valor + (plano.Valor*0.06)
WHERE plano.Numero = 'M1' OR plano.Numero = 'M2' OR plano.Numero = 'M3';
```
25) 
```sql
SELECT * from associado
WHERE associado.CEP LIKE "09%";
```