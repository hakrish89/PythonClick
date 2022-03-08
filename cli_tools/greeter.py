# greeter.py

import click

@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.option('--lang', help = 'Specify English(EN) or Espanyol (ES)', default='EN'
              ,type=click.Choice(['EN','ES']))
def greet(first_name, last_name, lang):
    """Displays a greeting to the user"""
    greeting = 'Hola' if lang=='ES' else 'Hello'
    click.echo(f"{greeting}, {first_name} {last_name}!")
