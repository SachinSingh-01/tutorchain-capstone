# tutorchain/logging_utils.py
from rich.console import Console
from rich.traceback import install
install()

console = Console()

def log_info(message: str):
    console.log(f"[bold cyan]INFO:[/bold cyan] {message}")

def log_event(event_name: str, details: dict):
    console.log(f"[bold green]EVENT:[/bold green] {event_name} → {details}")

def log_error(message: str):
    console.log(f"[bold red]ERROR:[/bold red] {message}")
