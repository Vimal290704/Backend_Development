from django.db import models # type: ignore

# Create your models here.
class Feature:
    id: int
    name: str
    details: str
    is_true: bool