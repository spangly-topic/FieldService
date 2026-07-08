# === Stage 35: Add active user switching and user-specific records ===
# Project: FieldService
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.email!r})"


class UserService:
    _users = {}

    @classmethod
    def register(cls, user):
        cls._users[user.email] = user

    @classmethod
    def get_active(cls):
        return cls._active_user

    @classmethod
    def set_active(cls, email):
        if email not in cls._users:
            raise KeyError(f"No registered user with email {email!r}")
        cls._active_user = cls._users[email]

    @classmethod
    def list_users(cls):
        return dict(sorted(cls._users.items()))


class FieldRecord:
    _records = {}

    def __init__(self, record_id, title, author_email, body="", created_at=None):
        self.record_id = record_id
        self.title = title
        self.author_email = author_email
        self.body = body
        self.created_at = created_at or datetime.now()

    @property
    def active_user(self):
        return UserService.get_active()

    @classmethod
    def create(cls, record_id, title, body=""):
        user = UserService.get_active()
        if not user:
            raise RuntimeError("No active user. Register and set one first.")
        rec = cls(record_id, title, user.email, body)
        cls._records[record_id] = rec
        return rec

    @classmethod
    def get(cls, record_id):
        if record_id not in cls._records:
            raise KeyError(f"Record {record_id!r} does not exist")
        return cls._records[record_id]


class FieldBook:
    _book = []

    @classmethod
    def add_record(cls, rec):
        cls._book.append(rec)
        if len(cls._book) > 100:
            cls._book.pop(0)

    @classmethod
    def list_records(cls):
        return list(cls._book)

    @classmethod
    def search(cls, query):
        q = query.lower()
        return [r for r in cls._book if q in r.title.lower() or q in r.body.lower()]


def main():
    UserService.register(User("Alice", "alice@example.com"))
    UserService.register(User("Bob", "bob@example.com"))
    UserService.set_active("alice@example.com")

    rec1 = FieldRecord.create(1, "Site A Inspection", "Body of inspection...")
    rec2 = FieldRecord.create(2, "Follow-up with Bob", "Waiting for his reply.")
    print(rec1)
    print(FieldBook.list_records())
