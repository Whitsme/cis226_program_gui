import hashlib
import string

from rich.align import Align
from rich.box import DOUBLE
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget

from rich.panel import Panel

from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Button, ButtonPressed
from textual.views import GridView

# class Submit(Button):

#     clicked: Reactive[RenderableType] = Reactive(False)

#     def on_click(self) -> None:
#         self.clicked = True

class FileMenu(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "File":
            renderable = "".join(map("[b]File[/b]", self.content))
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title=self.title,
            title_align="center",
            height=3,
            style="bold black on rgb(165,165,165)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class ShowQuit(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "Quit":
            renderable = "".join(map("[b]Quit[/b]", self.content))
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title=self.title,
            title_align="center",
            height=3,
            style="bold white on rgb(255,159,7)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class HelpMenu(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)
    
    def __init__(self, title: str):
        super().__init__(title)
        self.title = title
     
    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "Help":
            renderable = "".join(map("[b]Help[/b]", self.content))
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title=self.title,
            title_align="center",
            height=3,
            style="bold black on rgb(165,165,165)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class ShowAbout(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "About":
            renderable = "".join(map("[b]About[/b]", self.content))
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title=self.title,
            title_align="center",
            height=3,
            style="bold white on rgb(50,57,50)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class InputText(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_key(self, event: events.Key) -> None:
        if self.mouse_over == True:
            if event.key == "ctrl+h":
                self.content = self.content[:-1]
            else:
                self.content += event.key

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "password":
            renderable = "".join(map(lambda char: "*", self.content))
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title=self.title,
            title_align="center",
            height=3,
            style="bold white on rgb(50,57,50)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class HashCrack(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)

    password = ""

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_key(self, event: events.Key) -> None:
        if self.mouse_over == True:
            if event.key == "ctrl+h":
                self.content = self.content[:-1]
            else:
                self.content += event.key

    def validate_title(self, value) -> None:
        try:
            return value.lower()
        except (AttributeError, TypeError):
            raise AssertionError("title attribute should be a string.")
    


    def render(self, password) -> RenderableType:
        renderable = None
        if self.title.lower() == "hash":
            renderable = "".join(map(lambda char: "*", self.content))
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return Panel(
            renderable,
            title=self.title,
            title_align="center",
            height=3,
            style="bold white on rgb(50,57,50)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class MenuGrid(GridView):
    
    async def on_mount(self) -> None:
        # define input fields
        self.file = FileMenu("file")
        self.help = HelpMenu("help")
        # self.quit = ShowQuit("quit")
        # self.about = ShowAbout("about")
        self.grid.set_align("center", "center")
        self.grid.set_gap(1, 1)
        self.grid.add_column("column", repeat=2, size=40)
        self.grid.add_row("row", repeat=2, size=3)
        label_style = "bold white on rgb(60,60,60)"
        file_label = Button(label="file", name="file_label", style=label_style)
        help_label = Button(label="help", name="help_label", style=label_style)
        # quit_label = Button(label="quit", name="quit_label", style=label_style)
        # about_label = Button(label="about", name="about_label", style=label_style)
        self.grid.add_widget(file_label)
        self.grid.add_widget(help_label)
        # self.grid.add_widget(quit_label)
        # self.grid.add_widget(about_label)
    
    async def on_menu_click(self) -> None:
        self.quit = ShowQuit("quit")
        self.about = ShowAbout("about")
        self.grid.set_align("center", "center")
        self.grid.set_gap(1, 1)
        self.grid.add_column("column", repeat=2, size=40)
        self.grid.add_row("row", repeat=2, size=3)
        label_style = "bold white on rgb(60,60,60)"
        quit_label = Button(label="quit", name="quit_label", style=label_style)
        about_label = Button(label="about", name="about_label", style=label_style)
        self.grid.add_widget(quit_label)
        self.grid.add_widget(about_label)

class InputGrid(GridView):
    password: Reactive[RenderableType] = Reactive("")

    async def on_mount(self) -> None:
        self.password = InputText("password")
        # self.hash = HashIt("hash")
        self.grid.set_align("center")
        self.grid.set_gap(1, 1)
        self.grid.add_column("column", repeat=1, size=80)
        self.grid.add_row("row", repeat=2, size=3)
        button_style = "bold red on white"
        label_style = "bold white on rgb(60,60,60)"
        password_label = Button(label="password", name="password_label", style=label_style)
        self.grid.add_widget(self.password)
        self.grid.add_widget(Button(label="hash", name="hash_button", style=button_style))

class MainApp(App):
    hash: Reactive[RenderableType] = Reactive(False)
    password: Reactive[RenderableType] = Reactive("")

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        assert isinstance(message.sender, Button)
        button_name = message.sender.name
        self.password = self.input_grid.password.content
        # if button_name == "hash" and self.hash:
        #     self.hash_button.clicked = False
        #     self.password = self.password_field.content
        if button_name == "file":
            pass
        elif button_name == "help":
            pass
        elif button_name == "hash":
            if self.password != "":
                hash = self.password
                variations = string.ascii_lowercase + str('@')
                total_tries = 0 
                for first_letter in variations:
                    for second_letter in variations:
                        for third_letter in variations:
                            password_guess = first_letter + second_letter + third_letter 
                            hash_guess = hashlib.md5(password_guess.encode()).hexdigest()
                            total_tries += 1 
                            print("Guessing: {} - {}".format(password_guess, hash_guess))
                            if hash_guess == hash:
                                print("The password must be {}, we found it after {} tries!".format(
                                    password_guess, total_tries))
                                return 

                

    async def on_mount(self) -> None:
        self.menu_grid = MenuGrid()
        self.input_grid = InputGrid()
        await self.view.dock(self.menu_grid, self.input_grid)


if __name__ == "__main__":
    MainApp.run()
