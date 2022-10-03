from rich.table import Table

from textual import events
from textual.app import App
from textual.widgets import ScrollView


class MyApp(App):
    """An example of a very simple Textual App"""

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:

        self.body = body = ScrollView(auto_width=True)

        await self.view.dock(body)

        async def add_content():
            table = Table(title="Demo")

            for i in range(20):
                table.add_column(f"Col {i + 1}", style="magenta")
            for i in range(100):
                table.add_row(*[f"cell {i},{j}" for j in range(20)])

            await body.update(table)

        await self.call_later(add_content)


MyApp.run(title="Simple App", log="textual.log")


# class FileMenu(Widget):
#     title: Reactive[RenderableType] = Reactive("")
#     content: Reactive[RenderableType] = Reactive("")
#     mouse_over: Reactive[RenderableType] = Reactive(False)

#     def __init__(self, title: str):
#         super().__init__(title)
#         self.title = title

#     def on_enter(self) -> None:
#         self.mouse_over = True

#     def on_leave(self) -> None:
#         self.mouse_over = False

#     def on_mount(self):
#         self.panel = Panel(
#                 title="File",
#                 title_alight="center",
#             )

# class ShowQuit(Widget):
#     title: Reactive[RenderableType] = Reactive("")
#     content: Reactive[RenderableType] = Reactive("")
#     mouse_over: Reactive[RenderableType] = Reactive(False)

#     def __init__(self, title: str):
#         super().__init__(title)
#         self.title = title

#     def on_enter(self) -> None:
#         self.mouse_over = True

#     def on_leave(self) -> None:
#         self.mouse_over = False

#     def on_mount(self):
#         self.panel = Panel(
#                 title="Quit",
#                 title_alight="center",
#             )

# class HelpMenu(Widget):

#     title: Reactive[RenderableType] = Reactive("")
#     content: Reactive[RenderableType] = Reactive("")
#     mouse_over: Reactive[RenderableType] = Reactive(False)
    
#     def __init__(self, title: str):
#         super().__init__(title)
#         self.title = title
     
#     def on_enter(self) -> None:
#         self.mouse_over = True

#     def on_leave(self) -> None:
#         self.mouse_over = False

#     def on_mount(self):
#         self.panel = Panel(
#                 title="Help",
#                 title_alight="center",
#             )

# class ShowAbout(Widget):

#     title: Reactive[RenderableType] = Reactive("")
#     content: Reactive[RenderableType] = Reactive("")
#     mouse_over: Reactive[RenderableType] = Reactive(False)

#     def __init__(self, title: str):
#         super().__init__(title)
#         self.title = title

#     def on_enter(self) -> None:
#         self.mouse_over = True

#     def on_leave(self) -> None:
#         self.mouse_over = False

#     def on_mount(self):
#         self.panel = Panel(
#                 title="About",
#                 title_alight="center",
#             )