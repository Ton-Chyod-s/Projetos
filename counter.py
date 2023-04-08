import flet as ft


def main(page: ft.Page):
    page.title = "to testando"
    page.add(
        ft.OutlinedButton(text="Print",on_click=print('lol')),
    )

ft.app(target=main)