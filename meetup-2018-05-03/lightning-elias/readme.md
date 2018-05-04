# Some Python tools worth mentioning

## Jupyter Lab
First of all: [Jupyter Lab](https://github.com/jupyterlab/jupyterlab) is out. At the moment, it's just a slightly better view of notebooks with better syntax highlighting and support for more file types, but it' growing quickly. So, best to jump on and use it now:

```
pip install jupyterlab
jupyter lab
```

## TQDM
`tqdm` is a tiny, but very useful library that displays a simple progress bar (see the [tqdm notebook](./tqdm.ipynb))

```
pip install tqdm
```

## SQLite + Pandas
`pandas` has a nice interface to use SQL. The [sqlite notebook](./sqlite.ipynb) shows some of these features, combined with `sqlite3`, which allows SQL-like features without setting up a data base. [mock.db] is a self-contained database file using SQLite

```
pip install pandas sqlite
```

## Multiprocessing
Parallelising code with python is easy. Use the libraries `multiprocessing` and `multithreading` (same interface!) and you're good to go in 3 lines of code (see the [sqlite notebook](./sqlite.ipynb))
