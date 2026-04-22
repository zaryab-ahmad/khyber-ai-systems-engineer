import click

@click.command()
@click.option('--count', default=1, help='Number of times to run.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--color', type=click.Choice(['red', 'green', 'blue']), default='blue')
def hello(count, name, color):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.secho(f"Hello {name}! Sequence {x+1}", fg=color, bold=True)

if __name__ == '__main__':
    hello()
