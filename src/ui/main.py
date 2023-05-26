from pathlib import Path

from textual import on, log
from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.reactive import reactive
from textual.widgets import Header, Footer, Select, Label, Button, DirectoryTree

from src.decompress import decompress


class TarManApp(App):
    """A Textual app to manage tarfile operations."""
    CSS_PATH = "styles.css"
    selected_file = reactive("")

    BINDINGS = [
        ("q", "quit", "Exit")
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Vertical(
            DirectoryTree("./", id="tree"),
            Button(self.selected_file, id="selected_file_label"),
        )
        yield Footer()

    def on_mount(self):
        self.all_files = list(str(Path.cwd().glob("*.tar.gz")))

    def on_tree_node_highlighted(self, event: DirectoryTree.NodeHighlighted):
        self.selected_file = str(event.node.label)
        self.query_one("#selected_file_label", expect_type=Button).label = f"Extract {str(event.node.label)}"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        chosen_file_path = Path(self.selected_file)
        if chosen_file_path.exists() and chosen_file_path.is_file():
            tarball_path = chosen_file_path
            destination = chosen_file_path.cwd() / chosen_file_path.stem.split(".")[0]
            decompress(destination, tarball_path)
        else:
            log(f"ERROR: FILE NOT FOUND {self.selected_file}")
            log(Path(self.selected_file).absolute())

    def action_quit(self):
        self.exit()


if __name__ == "__main__":
    app = TarManApp()
    app.run()
