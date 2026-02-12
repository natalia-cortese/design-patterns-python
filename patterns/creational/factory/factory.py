"""
Factory pattern example: User Factory

The Factory delegates the creation of objects to a dedicated factory.
The client asks the factory for a user type without knowing the concrete class.
Useful when you have multiple types of the same abstraction (e.g. Admin, Guest, RegularUser).
"""

from abc import ABC, abstractmethod


class User(ABC):
    """Abstract base class for all user types."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @abstractmethod
    def get_permissions(self) -> list[str]:
        """Return the list of permissions for this user type."""
        pass

    @abstractmethod
    def get_greeting(self) -> str:
        """Return a greeting message for this user type."""
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, email={self.email!r})"


class Admin(User):
    """Administrator user with full access."""

    def get_permissions(self) -> list[str]:
        return ["read", "write", "delete", "manage_users", "manage_settings"]

    def get_greeting(self) -> str:
        return f"Welcome, Admin {self.name}. You have full access."


class RegularUser(User):
    """Standard user with limited access."""

    def get_permissions(self) -> list[str]:
        return ["read", "write"]

    def get_greeting(self) -> str:
        return f"Hello, {self.name}. You can read and write content."


class Guest(User):
    """Guest user with read-only access."""

    def get_permissions(self) -> list[str]:
        return ["read"]

    def get_greeting(self) -> str:
        return f"Hi, {self.name}. You have read-only access."


class UserFactory:
    """
    Factory that creates the appropriate User subclass based on user type.
    The client does not need to know the concrete classes.
    """

    _user_types: dict[str, type[User]] = {
        "admin": Admin,
        "regular": RegularUser,
        "guest": Guest,
    }

    @classmethod
    def create_user(cls, user_type: str, name: str, email: str) -> User:
        """
        Create a user of the given type.

        Args:
            user_type: One of "admin", "regular", "guest"
            name: User's name
            email: User's email

        Returns:
            An instance of the corresponding User subclass

        Raises:
            ValueError: If user_type is not recognized
        """
        user_class = cls._user_types.get(user_type.lower())
        if user_class is None:
            raise ValueError(
                f"Unknown user type: {user_type}. "
                f"Valid types: {list(cls._user_types.keys())}"
            )
        return user_class(name=name, email=email)


if __name__ == "__main__":
    # Client code: we ask the factory for users without knowing the concrete classes
    admin = UserFactory.create_user("admin", "Alice", "alice@example.com")
    regular = UserFactory.create_user("regular", "Bob", "bob@example.com")
    guest = UserFactory.create_user("guest", "Charlie", "charlie@example.com")

    for user in [admin, regular, guest]:
        print(user)
        print(f"  Permissions: {user.get_permissions()}")
        print(f"  Greeting: {user.get_greeting()}")
        print()

    # Invalid type raises ValueError
    try:
        UserFactory.create_user("superuser", "Dave", "dave@example.com")
    except ValueError as e:
        print(f"Expected error: {e}")
