from assignment9 import User


class Privileges:
    """Stores privileges for an admin user."""

    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "can add post",
                "can delete post",
                "can ban user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
