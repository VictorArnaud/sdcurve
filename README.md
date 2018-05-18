# sdcurve

Microserviço de curvas de crescimento baseados na Altura, Peso, IMC e Perímetro Cefálico de crianças com Síndrome de
Down do sexo masculino ou feminino de 0 a 36 meses e de 3 a 18 anos.

[![Build Status](https://travis-ci.com/VictorArnaud/sdcurve.svg?branch=master)](https://travis-ci.com/VictorArnaud/sdcurve)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/36d1be48a24f42109ae26e2997a6c079)](https://www.codacy.com/app/VictorArnaud/sdcurve?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=VictorArnaud/sdcurve&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/36d1be48a24f42109ae26e2997a6c079)](https://www.codacy.com/app/VictorArnaud/sdcurve?utm_source=github.com&utm_medium=referral&utm_content=VictorArnaud/sdcurve&utm_campaign=Badge_Coverage)

## Instalação

Pega o repositório do github: ```git clone https://github.com/VictorArnaud/sdcurve.git```

Instalar dependencias para rodar o python3 e pip3

```
sudo apt-get update

sudo apt-get install -y python3-dev sqlite python3-pip libpq-dev
sudo apt-get install -y gettext
```

Criar o ambiente virtual de desenvolvimento (virtualenvwrapper)

```
sudo pip3 install --upgrade pip
sudo pip3 install virtualenvwrapper
```

No arquivo .bashrc do link insira:

```
WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

* Para criar um ambiente virtual: ```mkvirtualenv <venv_name>```

* Para entrar no ambiente virtual: ```workon <venv_name>```

* Para sair do ambiente virtual: ```deactivate```

* Para remover o ambiente virtual: ```rmvirtualenv <venv_name>```

Instalar dependencias do projeto dentro do ambiente virtual

```
pip install -r requeriments.txt
```

Rodar comandos para popular o banco de dados

```
python3 manage.py migrations
python3 manage.py migrate
```

Rode o servidor

```
python3 manage.py runserver 0.0.0.0:8000
```

## Como usar

Esse microserviço disponibiliza de todas as curvas de crescimento necessárias para que o médico possa acompanhar melhor
seus pacientes com síndrome de down.

### Todos os endpoints disponibilizam:

* [x] Título da curva (title)

* [x] Eixo X da curva, ou seja, as idades (ages)

* [x] Os percentis gerados para peso, estatura e perímetro cefálico (percentis_3, percentis_10, percentis_25, percentis_50, percentis_75, percentis_90 e percentis_97)

* [x] Os percentis gerados para IMC (percentis_5, percentis_10, percentis_25, percentis_50, percentis_75, percentis_85, percentis_90 e percentis_95)

* [x] Um atributo chamado "graphic" tendo uma reorganização dos dados acima para plotagem em APIS de gráficos como [Google Charts](https://developers.google.com/chart/interactive/docs/)

* [x] Resultado de um consulta aos gráficos, por exemplo, ao inserir o peso, idade, sexo e intervalo de idade (0 a 36 meses ou 3 a 18 anos) da criança o resultado será se a criança está no peso médio (0), acima do peso médio (1) ou abaixo do peso médio (-1) estipulado pelos valores dentro dos percentis, ou seja, entre os percentis_3 e percentis_97 a crianças está com o peso na medida normal, abaixo do percentis_3 está com o peso abaixo da média e acima do percentis_97 está com o peso acima da média normal.

**OBS**: Em estatística descritiva, os percentis são medidas que dividem a amostra ordenada (por ordem crescente dos
dados) em 100 partes, cada uma com uma percentagem de dados aproximadamente igual.

### Endpoints para curva de crescimento (Altura)

* /api/growth-curve/height/male-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/height/male-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
  ```

* /api/growth-curve/height/female-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/height/female-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/height/result/

  ```
  Entradas:
    - height (cm): Altura da criança
    - age: Idade da criança.
    - gender: 'M' (Masculino) ou 'F' (Feminino).
    - interval: 'months' (0 a 36 meses) ou 'years' (3 a 18 anos).

  Saídas:
    -  0: Se a criança está na altura média.
    -  1: Se a criança está acima da altura média.
    - -1: Se a criança está abaixo da altura média.
  ```

### Endpoints para curva de crescimento (Peso)

* /api/growth-curve/weight/male-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/weight/male-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/weight/female-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/weight/female-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/weight/result/

  ```
  Entradas:
    - weight (kg): Peso da criança
    - age: Idade da criança.
    - gender: 'M' (Masculino) ou 'F' (Feminino).
    - interval: 'months' (0 a 36 meses) ou 'years' (3 a 18 anos).

  Saídas:
    -  0: Se a criança está no peso médio.
    -  1: Se a criança está acima do peso médio.
    - -1: Se a criança está abaixo do peso médio.
  ```

### Endpoints para curva de crescimento (IMC)

* /api/growth-curve/imc/male-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 5%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_85: Curva de 85%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 95%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/imc/male-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 5%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_85: Curva de 85%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 95%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/imc/female-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 5%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_85: Curva de 85%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 95%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/imc/female-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 5%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_85: Curva de 85%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 95%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/imc/result/

  ```
  Entradas:
    - height (m): Altura da criança
    - weight (kg): Peso da criança
    - age: Idade da criança.
    - gender: 'M' (Masculino) ou 'F' (Feminino).
    - interval: 'months' (0 a 36 meses) ou 'years' (3 a 18 anos).

  Saídas:
    -  0: Se a criança está no IMC médio.
    -  1: Se a criança está acima do IMC médio.
    - -1: Se a criança está abaixo do IMC médio.
  ```

### Endpoints para curva de crescimento (perímetro cefálico)

* /api/growth-curve/perimeter/male-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/perimeter/male-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/perimeter/female-years/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/perimeter/female-months/

  ```
  Entradas: N/A

  Saídas:
    - title: Título da curva.
    - ages: Idades do eixo X da curva
    - percentis_3: Curva de 3%
    - percentis_10: Curva de 10%
    - percentis_25: Curva de 25%
    - percentis_50: Curva de 50%
    - percentis_75: Curva de 75%
    - percentis_90: Curva de 90%
    - percentis_97: Curva de 97%
    - graphic: Reordenação dos dados para plotagem.
  ```

* /api/growth-curve/perimeter/result/

  ```
  Entradas:
    - perimeter (cm): Perímetro cefálico da criança
    - age: Idade da criança.
    - gender: 'M' (Masculino) ou 'F' (Feminino).
    - interval: 'months' (0 a 36 meses) ou 'years' (3 a 18 anos).

  Saídas:
    -  0: Se a criança está no perímetro cefálico médio.
    -  1: Se a criança está acima do perímetro cefálico médio.
    - -1: Se a criança está abaixo do perímetro cefálico médio.
  ```

### Refêrencia

BERTAPELLI FABIO. **Curvas de referência de crescimento para crinças e adolescentes com síndrome de down com idade entre 0
e 20 anos**. Tese de doutorado na Universidade de Campinas, Faculdade de Ciências Médicas. Campinha, SP. 2016
