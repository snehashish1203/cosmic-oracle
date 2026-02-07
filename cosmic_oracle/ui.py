from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.live import Live

console = Console()

def printer(text):
    console.print(text)
    

def question_panel():
    printer("\nAsk your question, mortal [bold red][0 to exit][/bold red]:")
    question = Prompt.ask("> ")
    if question == "0":
        printer("\n[bold red]The Oracle returns to silence...[/bold red]")
        return 0
    return question

def animated_prophecy_panel(text, delay=0.05):
    rendered = ""

    with Live("", refresh_per_second=30, console=console) as live:
        for char in text:
            rendered += char
            panel = Panel(rendered, title="Prophecy", style="bold red")
            live.update(panel)
            sleep(delay)
    printer("")

def show_banner():
    banner = Panel(
        Align.center("🔮  THE COSMIC DECISION ORACLE  🔮"),
        style="bold magenta",
    )
    printer(banner)

def menu():
    printer("[1][white]Ask another question!![/white]")
    printer("[0][bold red]Exit[/bold red]")
    try:
        select = int(Prompt.ask("Enter choice"))
    except ValueError:
        return 1 

    return select

def loader():
    with console.status("[bold magenta]Consulting the Cosmic Database..."):
        sleep(3)

    with console.status("[bold cyan]Interpreting celestial signals..."):
        sleep(1)
