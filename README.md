# Pandas Trainer

A terminal app for learning pandas through interactive exercises.

Requires [uv](https://docs.astral.sh/uv/).

## Install

```bash
git clone https://github.com/sandropa/learn-pandas.git ~/.local/src/learn-pandas
echo 'alias learn-pandas="uv run --project ~/.local/src/learn-pandas python ~/.local/src/learn-pandas/main.py"' >> ~/.bashrc
source ~/.bashrc
```

## Update

```bash
cd ~/.local/src/learn-pandas && git pull
```

## Usage

```
learn-pandas
learn-pandas -l 5        # start at level 5
learn-pandas --level 10   # start at level 10
```

Type your pandas solution in the REPL, then `submit` to check it.

`hint` for a hint, `help` for all commands, `q` to quit.
