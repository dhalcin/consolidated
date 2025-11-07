#!/usr/bin/env python3
import flet as ft
import asyncio
from src.ui import main_app

if __name__ == '__main__':
    asyncio.run(ft.app_async(target=main_app))