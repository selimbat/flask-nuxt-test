## Setup

Afin de setup le projet, il suffit de lancer le docker-compose qui contient la base de donnée :

```
$ docker-compose up -d
```

### API

Le provisionning de la base de donnée doit être lancé :

```
(venv) $ python provisionning.py
```

Afin de lancer le backend, il reste alors :

```
(venv) $ python run.py
```

### UI

L'UI se lance classiquement avec :

```
$ cd ui/
$ npm install
$ npm run dev
```