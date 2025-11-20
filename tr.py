class User:
    def __init__(self):
        self.user_id: int = 0
        self.username: str = ""
        self.email: str = ""
        self.password_hash: str = ""
        self.currency: str = "RUB"
        self.language: str = "ru"
        self.timezone: str = "Europe/Moscow"
        self.created_date: datetime = datetime.now()
        self.last_login: datetime = datetime.now()

class Category:
    def __init__(self):
        self.category_id: int = 0
        self.user_id: int = 0
        self.name: str = ""
        self.type: str = ""  # "income" или "expense"
        self.parent_id: int = None
        self.color: str = "#3498db"
        self.icon: str = "default"
        self.budget_limit: float = 0.0
        self.is_active: bool = True

class Account:
    def __init__(self):
        self.account_id: int = 0
        self.user_id: int = 0
        self.name: str = ""
        self.type: str = ""  # "cash", "debit", "credit", "savings"
        self.balance: float = 0.0
        self.currency: str = "RUB"
        .account_number: str = ""
        .bank_name: str = ""
        .credit_limit: float = 0.0  # Для кредитных карт
        .is_archived: bool = False

class Transaction:
    def __init__(self):
        self.transaction_id: int = 0
        self.user_id: int = 0
        self.account_id: int = 0
        self.category_id: int = 0
        self.amount: float = 0.0
        self.type: str = ""  # "income", "expense", "transfer"
        self.description: str = ""
        self.date: datetime = datetime.now()
        self.location: str = ""
        self.tags: List[str] = []
        self.receipt_photo: str = ""  # Путь к фото чека
        self.is_recurring: bool = False
        .recurring_pattern: str = ""  # "daily", "weekly", "monthly"

class Budget:
    def __init__(self):
        self.budget_id: int = 0
        self.user_id: int = 0
        self.category_id: int = 0
        self.amount: float = 0.0
        self.period: str = ""  # "daily", "weekly", "monthly", "yearly"
        self.start_date: datetime = datetime.now()
        self.end_date: datetime = None
        self.notifications: bool = True
        self.actual_spent: float = 0.0

