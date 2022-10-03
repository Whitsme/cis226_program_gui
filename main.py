"""
Aaron Whitaker
10/02/2022
CRN: 10235
CIS226: Advanced Python Programming
Aprox Time: 20 hours
"""

import hashlib
import string
# standard library imports

from rich import box
from rich.align import Align
from rich.box import DOUBLE
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
from rich.table import Table
# rich imports

from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Button, ButtonPressed
# textual imports

hash = [None]
guessing_list = [None]
guess_list = [None]
# lists for storing user input, hash guesses, and the final password guess

class Guessing(Widget):
    # displays contents of guessing_list in tui

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)
    # mouse reactive stuff not used

    def __init__(self, title: str):
        # sets title
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        # mouse reactive stuff not used
        self.mouse_over = True

    def on_leave(self) -> None:
        # mouse reactive stuff not used
        self.mouse_over = False
   
    def on_mount(self):
        # calls func to write to tui and is supposed to refresh and get more guesses, but I ran out time
        self.guess_writer()
        self.set_interval(1.0, self.guess_writer)
        self.refresh()

    def guess_writer(self):
        # preps table to panel for writing to tui
        guess_out = guessing_list 
        table = Table(
            show_header=True,
            header_style="bold",
            box=None,
            padding=(0, 1),
            expand=True,
        )

        table.add_column("", justify="left", style="green", no_wrap=True, ratio=1)

        for g in guess_out:
            table.add_row(g)

        self.panel = Panel(
            table,
            title=f"[b]guesses[/]",
            title_align="left",
            border_style="white",
            box=box.SQUARE,
        )

        self.refresh()

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "guesses":
            renderable = self.content
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return self.panel

class Guess(Widget):
    # write guess to tui if one is found
    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)
    # mouse reactive stuff not used

    def __init__(self, title: str):
        # set title
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        # mouse reactive stuff not used
        self.mouse_over = True

    def on_leave(self) -> None:
        # mouse reactive stuff not used
        self.mouse_over = False
   
    def on_mount(self):
        self.guess_found()

    def guess_found(self):
        try:
            found_it = guess_list[0]
        except:
            found_it = "*"
        table = Table(
            show_header=True,
            header_style="bold",
            box=None,
            padding=(0, 1),
            expand=True,
        )

        table.add_column("", justify="left", style="green", no_wrap=True, ratio=1)

        table.add_row(found_it)

        self.panel = Panel(
            table,
            title=f"[b]guess[/]",
            title_align="left",
            border_style="red",
            box=box.SQUARE,
        )

        self.refresh()

    def render(self) -> RenderableType:
        renderable = None
        if self.title.lower() == "guesses":
            renderable = self.content
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        return self.panel

class InputText(Widget):

    title: Reactive[RenderableType] = Reactive("")
    content: Reactive[RenderableType] = Reactive("")
    mouse_over: Reactive[RenderableType] = Reactive(False)
    # mouse reactive stuff not used

    def __init__(self, title: str):
        super().__init__(title)
        self.title = title

    def on_enter(self) -> None:
        # mouse reactive stuff not used
        self.mouse_over = True

    def on_leave(self) -> None:
        # mouse reactive stuff not used
        self.mouse_over = False

    def on_key(self, event: events.Key) -> None:
        # handles input from user
        if self.mouse_over == True:
            if event.key == "ctrl+h":
                self.content = self.content[:-1]
            else:
                self.content += event.key

    def render(self) -> RenderableType:
        # renders input box to tui
        renderable = None
        if self.title.lower() == "password":
            renderable = self.content
        else:
            renderable = Align.left(Text(self.content, style="bold"))
        hash.clear()
        hash.append(self.content)
        return Panel(
            renderable,
            title="Input MD5 hash below",
            title_align="center",
            height=3,
            style="bold white on rgb(50,57,50)",
            border_style=Style(color="green"),
            box=DOUBLE,
        )

class MainApp(App):
    # runs button click events and passes hash input to the hash cracker code below for password guess
    hash: Reactive[RenderableType] = Reactive(False)
    password: Reactive[RenderableType] = Reactive("")

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        # button click events and hash cracker
        assert isinstance(message.sender, Button)
        button_name = message.sender.name
        self.password = hash
        if button_name == "file":
            if self.quit_label.visible == False:
                self.quit_label.visible = True
            else:
                self.quit_label.visible = False
        elif button_name == "help":
            if self.about_label.visible == False:
                self.about_label.visible = True
            else:
                self.about_label.visible = False
        elif button_name == "quit":
            self.exit()
        elif button_name == "about":
            if self.about_panel.visible == False:
                self.about_panel.visible = True
            else:
                self.about_panel.visible = False
        elif button_name == "hash_button":
            if self.about_panel.visible == True:
                self.about_panel.visible = False
            if self.password != None:
                hashed = self.password
                variations = string.ascii_lowercase + str('@')
                total_tries = 0 
                for first_letter in variations:
                    for second_letter in variations:
                        for third_letter in variations:
                            password_guess = first_letter + second_letter + third_letter 
                            hash_guess = hashlib.md5(password_guess.encode()).hexdigest()
                            total_tries += 1 
                            pw_guess = "Guessing: {} - {}".format(password_guess, hash_guess)
                            guessing_list.append(pw_guess)
                            if hash_guess == hashed:
                                guess_list.append("The password must be {}, we found it after {} tries!".format(password_guess, total_tries)) 

    async def on_mount(self) -> None:
        # sets up the tui
        grid = await self.view.dock_grid(edge="left")

        label_style = "green on black"
        bar_style = "bold red on white"
        # some style sets

        self.hash = InputText("password")
        self.guessing = Guessing("guesses")
        self.guess = Guess("guess")
        # pulling in the classes above

        file_label = Button(label="file", name="file", style="bold black on rgb(165,165,165)")
        help_label = Button(label="help", name="help", style="bold black on rgb(165,165,165)")
        quit_label = Button(label="quit", name="quit", style="bold white on red")
        about_label = Button(label="about", name="about", style="bold black on yellow")
        about_panel = Button(label="Welcome to the MD5 Cracker!\nPlease input your hash to receive a password guess.", name="about_panel", style="bold white")
        # builds buttons

        self.quit_label = quit_label
        self.about_label = about_label
        self.about_panel = about_panel
        # sets up the buttons to be callable

        quit_label.visible = False
        about_label.visible = False
        about_panel.visible = False
        # hides the above buttons

        grid.set_align("center", "center")
        grid.set_gap(1, 1)
        grid.add_column(fraction=5, name="1")
        grid.add_column(fraction=5, name="2")
        grid.add_column(fraction=5, name="3")
        grid.add_column(fraction=5, name="4")
        grid.add_column(fraction=5, name="5")
        grid.add_column(fraction=5, name="6")
        grid.add_column(fraction=5, name="7")
        grid.add_column(fraction=5, name="8")
        grid.add_column(fraction=5, name="9")
        grid.add_column(fraction=5, name="10")
        grid.add_column(fraction=5, name="11")
        grid.add_column(fraction=5, name="12")
        grid.add_column(fraction=5, name="13")
        grid.add_column(fraction=5, name="14")
        grid.add_column(fraction=5, name="15")
        grid.add_column(fraction=5, name="16")
        grid.add_column(fraction=5, name="17")
        grid.add_column(fraction=5, name="18")
        grid.add_column(fraction=5, name="19")
        grid.add_column(fraction=5, name="20")
        grid.add_row(size=1, name="r0")
        grid.add_row(size=3, name="r1")
        grid.add_row(size=1, name="r7")
        grid.add_row(size=1, name="r2")
        grid.add_row(size=3, name="r3")
        grid.add_row(size=1, name="r4")
        grid.add_row(size=20, name="r5")
        grid.add_row(size=3, name="r6")
        grid.add_areas(
            area0a="5-start|15-end,r0",
            area1="5-start|11-end,r1",
            area2a="12-start|15-end,r1",
            area2b="7-start|9-end,r7",
            area2c="13-start|14-end,r7",
            area3a="5-start|15-end,r2",
            area3b="6-start|13-end,r3",
            area3c="5,r2-start|r4-end",
            area3d="14-start|15-end,r2-start|r4-end",
            area3e="5-start|15-end,r4",
            area4="5-start|15-end,r5",
            area5="5-start|15-end,r5",
            area6="5-start|15-end,r6",
        )
        grid.place(
            area0a=grid.add_widget(Button(label="MD5 Cracker", name="md5_cracker", style=label_style)),
            area1=grid.add_widget(file_label),
            area2a=grid.add_widget(help_label),
            area2b=grid.add_widget(quit_label),
            area2c=grid.add_widget(about_label),
            area3a=grid.add_widget(Button(label="--->          ", name="hash_top", style=bar_style)),
            area3b=grid.add_widget(self.hash),
            area3c=grid.add_widget(Button(label="", name="hash_left", style=bar_style)),
            area3d=grid.add_widget(Button(label="CRACK", name="hash_button", style=bar_style)),
            area3e=grid.add_widget(Button(label="--->          ", name="hash_bottom", style=bar_style)),
            area4=grid.add_widget(self.guessing),
            area5=grid.add_widget(about_panel),
            area6=grid.add_widget(self.guess),
        )
        # builds the grid

        await self.view.dock(self.guessing)

if __name__ == "__main__":
    MainApp.run(log="tui.log")


"""
Design: I intended to use the Textual Library (https://github.com/Textualize/textual) to build a TUI (text user interface). 
Develop: I did use the Textual Library, but the lack of documentation and existing examples made it quite challenging. It was a lot of trial and error.
Test: Nothing, there are not tests available for the Textual Library. I found this out late in the process. 
Documentation: The above code is a TUI for the MD5 Cracker program provided in the last python class. It attempts to output a password guess based on the hash provided. 
"""