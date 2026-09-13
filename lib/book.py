#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count):
        if not title.strip():
            raise ValueError("Title is mandatory")

        if not isinstance(page_count, int) or isinstance(page_count, bool):
            raise ValueError("page_count must be an integer")

        if page_count < 0:
            raise ValueError("Please enter a valid page count")

                
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        