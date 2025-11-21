#!/usr/bin/env python3
import flet as ft
import asyncio
from src.ui import main

if __name__ == '__main__':
    ft.app(target=main)
    #asyncio.run(ft.app_async(target=main_app))