import typer
from loguru import logger
from rich.console import Console
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import version
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.example import ExampleClass

# Configure Loguru Logger
logger.add("log.log", level="TRACE", rotation="50 MB")

# Configure Rich Console
console = Console()

# Configure Typer
app = typer.Typer(
    name="{{ cookiecutter.project_name }}",
    help="{{ cookiecutter.project_description }}",
    add_completion=False,
)


# Print Current Version
def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]{{ cookiecutter.project_name }}[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


# Typer Commands
@app.command()
def main(
    profile: str = typer.Option(..., help="Profile to load."),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the {{ cookiecutter.project_name }} package.",
    ),
) -> None:
    
    # Example Entry Point
    console.print(ExampleClass().print_name(name="Ron Paul"))
    logger.info(f"Example Entry Point! {profile=}")


    # Example #DIV/0 Logging Error (caught by @logger.catch decorator)
    ExampleClass().example_divide_by_zero()


if __name__ == "__main__":
    app()
