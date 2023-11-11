from dataclasses import dataclass
from abc import ABC, abstractmethod
from faker import Faker

faker = Faker('pl_PL')


@dataclass
class Post:
    id: int
    title: str
    content: str


class IPotstService(ABC):
    @abstractmethod
    def list(self) -> list[Post]:
        pass


class FakePostService(IPotstService):
    id = 0

    def list() -> list[Post]:
        n=25
        return [FakePostService.create_post() for _ in range(n)]
    @classmethod
    def create_post(cls) -> Post:
        post = Post(
            id=cls.id,
            title=faker.text(30),
            content=faker.text(500)
        )

        cls.id +=1
        return post
