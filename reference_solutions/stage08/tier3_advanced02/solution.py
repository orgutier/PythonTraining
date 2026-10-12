class ResourceGuard:
    def __enter__(self):
        self.active = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.active = False
        return False


class Transaction:
    def __enter__(self):
        self.committed = False
        self.rolled_back = False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.committed = True
        else:
            self.rolled_back = True
        return False


class SuppressAll:
    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True
