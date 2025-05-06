"""Command-line interface for The One Ring RPG tools."""

import click
from rich.console import Console
from rich.table import Table
from .mechanics import roll_skill_test

console = Console()

@click.group()
def cli():
    """The One Ring RPG Game Master Tools."""
    pass

@cli.command()
@click.option('--skill', '-s', required=True, type=int, help='Skill rating of the character (1-6)')
@click.option('--tn', '-t', required=True, type=int, help='Target number for the test')
@click.option('--advantage', '-a', is_flag=True, help='Whether the character has advantage')
@click.option('--disadvantage', '-d', is_flag=True, help='Whether the character has disadvantage')
def resolve_action(skill: int, tn: int, advantage: bool, disadvantage: bool):
    """Resolve a skill test in The One Ring RPG."""
    try:
        result = roll_skill_test(skill, tn, advantage, disadvantage)
        
        # Create a table for the result
        table = Table(title="Skill Test Result")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")
        
        # Add rows to the table
        table.add_row("Success", "Yes" if result.success else "No")
        table.add_row("Skill Roll", str(result.roll))
        table.add_row("Feat Roll", str(result.feat_roll))
        table.add_row("Total", str(result.roll + result.skill_rating))
        table.add_row("Target Number", str(result.target_number))
        table.add_row("Skill Rating", str(result.skill_rating))
        
        if result.great_success:
            table.add_row("Great Success", "Yes")
        if result.extraordinary_success:
            table.add_row("Extraordinary Success", "Yes")
        if result.gandalf_rune:
            table.add_row("Gandalf Rune", "Yes")
        if result.sauron_rune:
            table.add_row("Sauron Rune", "Yes")
            
        console.print(table)
        
    except ValueError as e:
        console.print(f"[red]Error:[/red] {str(e)}")

if __name__ == '__main__':
    cli() 