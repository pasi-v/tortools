"""Command-line interface for The One Ring RPG tools."""

import click
from rich.console import Console

console = Console()

@click.group()
def cli():
    """The One Ring RPG Game Master Tools."""
    pass

@cli.command()
@click.option('--skill', '-s', required=True, help='Skill rating of the character')
@click.option('--tn', '-t', required=True, type=int, help='Target number for the test')
@click.option('--advantage', '-a', is_flag=True, help='Whether the character has advantage')
@click.option('--disadvantage', '-d', is_flag=True, help='Whether the character has disadvantage')
def resolve_action(skill: int, tn: int, advantage: bool, disadvantage: bool):
    """Resolve a skill test in The One Ring RPG."""
    # TODO: Implement skill test resolution
    console.print(f"Resolving skill test with skill {skill} against TN {tn}")
    if advantage:
        console.print("With advantage")
    if disadvantage:
        console.print("With disadvantage")

if __name__ == '__main__':
    cli() 