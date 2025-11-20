class User:
    def __init__(self, user_id, name, email, currency="RUB"):
        self.user_id = user_id  # Уникальный идентификатор пользователя
        self.name = name  # Имя пользователя
        self.email = email  # Email для уведомлений
        self.currency = currency  # Основная валюта (RUB, USD, EUR)
        self.accounts = []  # Список объектов Account (счета пользователя)
        self.categories = []  # Список объектов Category (категории пользователя)
        self.budgets = []  # Список объектов Budget (бюджеты пользователя)
        self.goals = []  # Список объектов Goal (цели пользователя)

class Account:
    def __init__(self, account_id, user_id, name, account_type, initial_balance=0.0):
        self.account_id = account_id  # Уникальный идентификатор счета
        self.user_id = user_id  # ID владельца счета (связь с User)
        self.name = name  # Название счета (например, "Сбербанк", "Наличные")
        self.account_type = account_type  # Тип: "cash", "debit_card", "credit_card", "savings"
        self.current_balance = initial_balance  # Текущий баланс на счете
        self.transactions = []  # Список объектов Transaction, связанных с этим счетом

class Category:
    def __init__(self, category_id, user_id, name, category_type, parent_id=None):
        self.category_id = category_id  # Уникальный идентификатор категории
        self.user_id = user_id  # ID владельца категории
        self.name = name  # Название категории ("Еда", "Развлечения")
        self.category_type = category_type  # Тип: "income" (доход) или "expense" (расход)
        self.parent_id = parent_id  # ID родительской категории (для создания иерархии, например, "Еда" -> "Продукты")

class Transaction:
    def __init__(self, transaction_id, account_id, category_id, amount, date, type, description=""):
        self.transaction_id = transaction_id  # Уникальный идентификатор транзакции
        self.account_id = account_id  # ID счета, с которым связана операция
        self.category_id = category_id  # ID категории
        self.amount = amount  # Сумма операции (всегда положительная)
        self.date = date  # Дата и время операции (объект datetime)
        self.type = type  # Тип: "income" или "expense" (дублирует тип категории для скорости)
        self.description = description  # Необязательное описание (например, "Купил хлеб в Пятерочке")

class Budget:
    def __init__(self, budget_id, user_id, category_id, amount, period):
        self.budget_id = budget_id  # Уникальный идентификатор бюджета
        self.user_id = user_id  # ID пользователя
        self.category_id = category_id  # ID категории, для которой установлен бюджет
        self.amount = amount  # Планируемая сумма расходов за период
        self.period = period  # Период: "monthly", "weekly", "yearly"
        self.spent = 0.0  # Фактически потраченная сумма (будет вычисляться)
        
class Goal:
    def __init__(self, goal_id, user_id, name, target_amount, current_amount=0.0, deadline=None):
        self.goal_id = goal_id  # Уникальный идентификатор цели
        self.user_id = user_id  # ID пользователя
        self.name = name  # Название цели ("На новый ноутбук")
        self.target_amount = target_amount  # Целевая сумма
        self.current_amount = current_amount  # Текущая накопленная сумма
        self.deadline = deadline  # Опциональная дата, к которой нужно накопить

from datetime import datetime, timedelta
from typing import List, Dict

class User:
    def __init__(self, user_id: int, name: str, email: str, currency: str = "RUB"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.currency = currency
        self.accounts: List['Account'] = []
        self.categories: List['Category'] = []
        self.budgets: List['Budget'] = []
        self.goals: List['Goal'] = []
    
    def __str__(self):
        return f"Пользователь: {self.name} (ID: {self.user_id})"

class Category:
    def __init__(self, category_id: int, user_id: int, name: str, category_type: str, parent_id: int = None):
        self.category_id = category_id
        self.user_id = user_id
        self.name = name
        self.category_type = category_type  # 'income' или 'expense'
        self.parent_id = parent_id
    
    def __str__(self):
        type_str = "Доход" if self.category_type == 'income' else "Расход"
        return f"Категория: {self.name} ({type_str})"

class Account:
    def __init__(self, account_id: int, user_id: int, name: str, account_type: str, initial_balance: float = 0.0):
        self.account_id = account_id
        self.user_id = user_id
        self.name = name
        self.account_type = account_type
        self.current_balance = initial_balance
        self.transactions: List['Transaction'] = []
    
    def __str__(self):
        return f"Счет: {self.name} | Баланс: {self.current_balance:.2f} | Тип: {self.account_type}"

class Transaction:
    def __init__(self, transaction_id: int, account_id: int, category_id: int, 
                 amount: float, date: datetime, transaction_type: str, description: str = ""):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.category_id = category_id
        self.amount = amount
        self.date = date
        self.type = transaction_type
        self.description = description
    
    def __str__(self):
        type_symbol = "+" if self.type == 'income' else "-"
        return f"Транзакция {self.transaction_id}: {type_symbol}{self.amount:.2f} | {self.description}"

class Budget:
    def __init__(self, budget_id: int, user_id: int, category_id: int, amount: float, period: str):
        self.budget_id = budget_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.period = period
        self.spent = 0.0
    
    def __str__(self):
        return f"Бюджет: {self.amount:.2f} на {self.period} | Потрачено: {self.spent:.2f}"

class Goal:
    def __init__(self, goal_id: int, user_id: int, name: str, target_amount: float, 
                 current_amount: float = 0.0, deadline: datetime = None):
        self.goal_id = goal_id
        self.user_id = user_id
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.deadline = deadline
    
    def __str__(self):
        progress = (self.current_amount / self.target_amount) * 100
        deadline_str = self.deadline.strftime("%d.%m.%Y") if self.deadline else "Не установлен"
        return f"Цель: {self.name} | Прогресс: {progress:.1f}% ({self.current_amount:.2f}/{self.target_amount:.2f}) | До: {deadline_str}"

class FinanceManager:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.categories: Dict[int, Category] = {}
        self.accounts: Dict[int, Account] = {}
        self.transactions: Dict[int, Transaction] = {}
        self.budgets: Dict[int, Budget] = {}
        self.goals: Dict[int, Goal] = {}
        
        # Счетчики для генерации ID
        self.user_counter = 1
        self.category_counter = 1
        self.account_counter = 1
        self.transaction_counter = 1
        self.budget_counter = 1
        self.goal_counter = 1
    
    def create_user(self, name: str, email: str, currency: str = "RUB") -> User:
        user = User(self.user_counter, name, email, currency)
        self.users[user.user_id] = user
        self.user_counter += 1
        
        # Создаем стандартные категории для пользователя
        self._create_default_categories(user.user_id)
        return user
    
    def _create_default_categories(self, user_id: int):
        expense_categories = ["Продукты", "Транспорт", "Развлечения", "Одежда", "Здоровье"]
        income_categories = ["Зарплата", "Премия", "Инвестиции", "Подарки"]
        
        for category_name in expense_categories:
            category = Category(self.category_counter, user_id, category_name, 'expense')
            self.categories[category.category_id] = category
            self.users[user_id].categories.append(category)
            self.category_counter += 1
        
        for category_name in income_categories:
            category = Category(self.category_counter, user_id, category_name, 'income')
            self.categories[category.category_id] = category
            self.users[user_id].categories.append(category)
            self.category_counter += 1
    
    def create_account(self, user_id: int, name: str, account_type: str, initial_balance: float = 0.0) -> Account:
        account = Account(self.account_counter, user_id, name, account_type, initial_balance)
        self.accounts[account.account_id] = account
        self.users[user_id].accounts.append(account)
        self.account_counter += 1
        return account
    
    def add_transaction(self, account_id: int, category_id: int, amount: float, 
                       transaction_type: str, description: str = "") -> Transaction:
        transaction = Transaction(
            self.transaction_counter, account_id, category_id, amount, 
            datetime.now(), transaction_type, description
        )
        
        self.transactions[transaction.transaction_id] = transaction
        
        # Обновляем баланс счета
        account = self.accounts[account_id]
        account.transactions.append(transaction)
        
        if transaction_type == 'income':
            account.current_balance += amount
        else:  # expense
            account.current_balance -= amount
        
        # Обновляем бюджет, если это расход
        if transaction_type == 'expense':
            self._update_budget(category_id, amount)
        
        self.transaction_counter += 1
        return transaction
    
    def _update_budget(self, category_id: int, amount: float):
        """Обновляет потраченную сумму в бюджетах для данной категории"""
        for budget in self.budgets.values():
            if budget.category_id == category_id:
                budget.spent += amount
    
    def create_budget(self, user_id: int, category_id: int, amount: float, period: str) -> Budget:
        budget = Budget(self.budget_counter, user_id, category_id, amount, period)
        self.budgets[budget.budget_id] = budget
        self.users[user_id].budgets.append(budget)
        self.budget_counter += 1
        return budget
    
    def create_goal(self, user_id: int, name: str, target_amount: float, 
                   deadline: datetime = None) -> Goal:
        goal = Goal(self.goal_counter, user_id, name, target_amount, 0.0, deadline)
        self.goals[goal.goal_id] = goal
        self.users[user_id].goals.append(goal)
        self.goal_counter += 1
        return goal
    
    def add_to_goal(self, goal_id: int, amount: float):
        """Пополнение финансовой цели"""
        if goal_id in self.goals:
            self.goals[goal_id].current_amount += amount
    
    def get_user_financial_summary(self, user_id: int) -> Dict:
        """Получение финансовой сводки пользователя"""
        user = self.users[user_id]
        total_balance = sum(account.current_balance for account in user.accounts)
        
        # Расчет доходов и расходов за текущий месяц
        current_month = datetime.now().month
        monthly_income = 0
        monthly_expenses = 0
        
        for account in user.accounts:
            for transaction in account.transactions:
                if transaction.date.month == current_month:
                    if transaction.type == 'income':
                        monthly_income += transaction.amount
                    else:
                        monthly_expenses += transaction.amount
        
        return {
            'total_balance': total_balance,
            'monthly_income': monthly_income,
            'monthly_expenses': monthly_expenses,
            'savings': monthly_income - monthly_expenses,
            'accounts_count': len(user.accounts),
            'goals_count': len(user.goals)
        }

def main():
    # Создание менеджера финансов
    finance_manager = FinanceManager()
    
    # Создание пользователя
    user = finance_manager.create_user("Иван Петров", "ivan@example.com", "RUB")
    print(f"Создан: {user}")
    print()
    
    # Создание счетов
    cash_account = finance_manager.create_account(user.user_id, "Наличные", "cash", 5000.0)
    card_account = finance_manager.create_account(user.user_id, "Основная карта", "debit_card", 15000.0)
    savings_account = finance_manager.create_account(user.user_id, "Накопительный счет", "savings", 30000.0)
    
    print("Созданные счета:")
    for account in user.accounts:
        print(f"  - {account}")
    print()
    
    # Добавление транзакций
    print("Добавление транзакций:")
    
    # Находим ID категорий
    salary_category_id = next(cat.category_id for cat in user.categories if cat.name == "Зарплата")
    products_category_id = next(cat.category_id for cat in user.categories if cat.name == "Продукты")
    transport_category_id = next(cat.category_id for cat in user.categories if cat.name == "Транспорт")
    entertainment_category_id = next(cat.category_id for cat in user.categories if cat.name == "Развлечения")
    
    # Доходы
    salary_transaction = finance_manager.add_transaction(
        card_account.account_id, salary_category_id, 50000.0, 'income', "Зарплата за октябрь"
    )
    print(f"  - {salary_transaction}")
    
    # Расходы
    products_transaction = finance_manager.add_transaction(
        cash_account.account_id, products_category_id, 2500.0, 'expense', "Продукты на неделю"
    )
    print(f"  - {products_transaction}")
    
    transport_transaction = finance_manager.add_transaction(
        card_account.account_id, transport_category_id, 1500.0, 'expense', "Проездной на месяц"
    )
    print(f"  - {transport_transaction}")
    
    entertainment_transaction = finance_manager.add_transaction(
        card_account.account_id, entertainment_category_id, 3000.0, 'expense', "Поход в кино"
    )
    print(f"  - {entertainment_transaction}")
    print()
    
    # Создание бюджета
    products_budget = finance_manager.create_budget(
        user.user_id, products_category_id, 10000.0, "monthly"
    )
    print(f"Создан бюджет: {products_budget}")
    print()
    
    # Создание финансовой цели
    vacation_goal = finance_manager.create_goal(
        user.user_id, "Отпуск в Турции", 100000.0, 
        datetime.now() + timedelta(days=180)
    )
    
    # Пополнение цели
    finance_manager.add_to_goal(vacation_goal.goal_id, 15000.0)
    print(f"Создана цель: {vacation_goal}")
    print()
    
    # Финансовая сводка
    summary = finance_manager.get_user_financial_summary(user.user_id)
    print("ФИНАНСОВАЯ СВОДКА:")
    print(f"Общий баланс: {summary['total_balance']:.2f} {user.currency}")
    print(f"Доходы за месяц: {summary['monthly_income']:.2f} {user.currency}")
    print(f"Расходы за месяц: {summary['monthly_expenses']:.2f} {user.currency}")
    print(f"Накопления за месяц: {summary['savings']:.2f} {user.currency}")
    print(f"Количество счетов: {summary['accounts_count']}")
    print(f"Количество целей: {summary['goals_count']}")

if __name__ == "__main__":
    main()

class AdvancedFinanceManager(FinanceManager):
    def __init__(self):
        super().__init__()
    
    def delete_account(self, account_id: int) -> bool:
        """Удаление счета (только если баланс нулевой)"""
        if account_id in self.accounts:
            account = self.accounts[account_id]
            if account.current_balance == 0 and not account.transactions:
                # Удаляем счет из пользователя
                user = self.users[account.user_id]
                user.accounts = [acc for acc in user.accounts if acc.account_id != account_id]
                
                # Удаляем счет из общего словаря
                del self.accounts[account_id]
                return True
        return False
    
    def transfer_between_accounts(self, from_account_id: int, to_account_id: int, amount: float) -> bool:
        """Перевод средств между счетами"""
        if from_account_id not in self.accounts or to_account_id not in self.accounts:
            return False
        
        from_account = self.accounts[from_account_id]
        to_account = self.accounts[to_account_id]
        
        if from_account.current_balance < amount:
            return False
        
        # Создаем транзакции перевода
        transfer_category_id = next(
            (cat.category_id for cat in self.categories.values() 
             if cat.name == "Переводы" and cat.user_id == from_account.user_id), 
            None
        )
        
        if not transfer_category_id:
            # Создаем категорию "Переводы" если её нет
            transfer_category = Category(
                self.category_counter, from_account.user_id, "Переводы", "expense"
            )
            self.categories[transfer_category.category_id] = transfer_category
            transfer_category_id = transfer_category.category_id
            self.category_counter += 1
        
        # Списание со счета отправителя
        self.add_transaction(
            from_account_id, transfer_category_id, amount, 'expense', 
            f"Перевод на счет {to_account.name}"
        )
        
        # Зачисление на счет получателя
        self.add_transaction(
            to_account_id, transfer_category_id, amount, 'income',
            f"Перевод со счета {from_account.name}"
        )
        
        return True
    
    def get_category_statistics(self, user_id: int, period_days: int = 30) -> Dict[str, float]:
        """Статистика по категориям расходов за указанный период"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=period_days)
        
        category_stats = {}
        
        for account in self.users[user_id].accounts:
            for transaction in account.transactions:
                if (transaction.type == 'expense' and 
                    start_date <= transaction.date <= end_date):
                    
                    category_name = self.categories[transaction.category_id].name
                    if category_name not in category_stats:
                        category_stats[category_name] = 0.0
                    category_stats[category_name] += transaction.amount
        
        return category_stats
    
    def close_goal(self, goal_id: int) -> bool:
        """Завершение финансовой цели и перевод средств на счет"""
        if goal_id not in self.goals:
            return False
        
        goal = self.goals[goal_id]
        user_id = goal.user_id
        
        if goal.current_amount < goal.target_amount:
            print(f"Цель не достигнута! Не хватает {goal.target_amount - goal.current_amount:.2f}")
            return False
        
        # Находим накопительный счет пользователя
        savings_account = next(
            (acc for acc in self.users[user_id].accounts if acc.account_type == 'savings'), 
            None
        )
        
        if not savings_account:
            savings_account = self.create_account(user_id, "Сбережения", "savings")
        
        # Переводим средства на счет
        savings_account.current_balance += goal.current_amount
        
        print(f"Цель '{goal.name}' достигнута! {goal.current_amount:.2f} переведено на счет {savings_account.name}")
        
        # Удаляем цель
        user = self.users[user_id]
        user.goals = [g for g in user.goals if g.goal_id != goal_id]
        del self.goals[goal_id]
        
        return True

def demonstrate_advanced_features():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАСШИРЕННЫХ ВОЗМОЖНОСТЕЙ")
    print("=" * 50)
    
    finance_manager = AdvancedFinanceManager()
    
    # Создание пользователя и счетов
    user = finance_manager.create_user("Анна Сидорова", "anna@example.com")
    main_account = finance_manager.create_account(user.user_id, "Основной", "debit_card", 20000.0)
    savings_account = finance_manager.create_account(user.user_id, "Накопления", "savings", 5000.0)
    
    print("Начальное состояние счетов:")
    for account in user.accounts:
        print(f"  - {account}")
    print()
    
    # Демонстрация перевода между счетами
    print("Перевод 3000 руб с основного счета на накопительный:")
    finance_manager.transfer_between_accounts(
        main_account.account_id, savings_account.account_id, 3000.0
    )
    
    for account in user.accounts:
        print(f"  - {account}")
    print()
    
    # Добавление нескольких транзакций для статистики
    categories = {cat.name: cat.category_id for cat in user.categories}
    
    finance_manager.add_transaction(
        main_account.account_id, categories["Продукты"], 1500.0, 'expense', "Супермаркет"
    )
    finance_manager.add_transaction(
        main_account.account_id, categories["Транспорт"], 500.0, 'expense', "Такси"
    )
    finance_manager.add_transaction(
        main_account.account_id, categories["Развлечения"], 2000.0, 'expense', "Ресторан"
    )
    finance_manager.add_transaction(
        main_account.account_id, categories["Продукты"], 800.0, 'expense', "Рынок"
    )
    
    # Статистика по категориям
    stats = finance_manager.get_category_statistics(user.user_id)
    print("СТАТИСТИКА РАСХОДОВ ПО КАТЕГОРИЯМ:")
    for category, amount in stats.items():
        print(f"  - {category}: {amount:.2f} руб")
    print()
    
    # Работа с целями
    print("РАБОТА С ФИНАНСОВЫМИ ЦЕЛЯМИ:")
    laptop_goal = finance_manager.create_goal(
        user.user_id, "Новый ноутбук", 50000.0, 
        datetime.now() + timedelta(days=90)
    )
    
    # Пополнение цели несколькими взносами
    finance_manager.add_to_goal(laptop_goal.goal_id, 10000.0)
    finance_manager.add_to_goal(laptop_goal.goal_id, 15000.0)
    finance_manager.add_to_goal(laptop_goal.goal_id, 25000.0)
    
    print(f"Текущее состояние цели: {laptop_goal}")
    
    # Попытка завершить цель (не хватает средств)
    finance_manager.close_goal(laptop_goal.goal_id)
    print()
    
    # Дополняем до полной суммы и завершаем цель
    finance_manager.add_to_goal(laptop_goal.goal_id, 10000.0)
    finance_manager.close_goal(laptop_goal.goal_id)
    print()
    
    print("Финальное состояние счетов:")
    for account in user.accounts:
        print(f"  - {account}")

if __name__ == "__main__":
    # Запуск основной демонстрации
    main()
    
    # Запуск демонстрации расширенных возможностей
    demonstrate_advanced_features()

