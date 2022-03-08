#calculator.py

import click

@click.command()
@click.argument('x', type=int, nargs=-1)
def add(x):
    """Returns a sum of numbers"""
    click.echo(sum(x))

@click.command()
@click.argument('x', type=int, nargs=-1)
def subtract(x):
    """Subtracts given set of numbers"""
    result = x[0]
    for i in x[1:]:
        result = result-i
    click.echo(result)
