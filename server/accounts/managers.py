from typing import Any
from django.db.models import Manager as BaseManager

from random import randint


class CustomAccountManager(BaseManager):
    def generate_account_number(self):
        starting_number = randint(31, 55)
        remaining_numbers = "".join([str(randint(0, 9)) for _ in range(13)])
        return f"{starting_number}{remaining_numbers}"

    def create(self, **kwargs: Any) -> Any:
        kwargs["account_number"] = self.generate_account_number()
        return super().create(**kwargs)
