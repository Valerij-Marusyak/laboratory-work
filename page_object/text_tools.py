from typing import List


def extract_price(text: str) -> str:
   """ извлекает из строки цену """
   split_by_lines: List[str] = text.split("\n")
   first_price_lines = split_by_lines[0].split(' ')
   first_price = first_price_lines[0][1:]
   first_price_without_punctuation = first_price.replace(",", "")
   return first_price_without_punctuation
