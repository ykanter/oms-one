import duckdb as duck
import flet as ft

def main(page : ft.Page):
    page.add(ft.Text(duck.sql("SELECT 'Life Universe' as question, 42 AS answer").df()))


ft.app(main)