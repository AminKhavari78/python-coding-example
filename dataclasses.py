# A basic Data Class

# Importing dataclass module
import dataclasses
from contextlib import contextmanager

@dataclass
class GfgArticle():
    """A class for holding an article content"""

    # Attributes Declaration
    # using Type Hints

    title: str
    author: str
    language: str
    upvotes: int


# A DataClass object
article = GfgArticle("DataClasses",
                     "vibhu4agarwal",
                     "Python", 0)
print(article)