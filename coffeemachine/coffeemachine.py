"""
Модуль Coffee Machine.

Реалізує логіку роботи кавового автомата через систему станів.
Автомат підтримує купівлю напоїв, поповнення інгредієнтів та інкасацію.
"""

class CoffeeMachine:
    """
    Клас, що моделює роботу кавової машини як скінченного автомата.

    Машина зберігає ресурси (вода, молоко, зерна, стаканчики) та гроші.
    Вона перемикається між різними станами залежно від вводу користувача.
    """

    # Рецепти (вода, молоко, зерна, ціна, назва)
    RECIPES = {
        '1': {'water': 250, 'milk': 0, 'beans': 16, 'price': 4, 'name': 'espresso'},
        '2': {'water': 350, 'milk': 75, 'beans': 20, 'price': 7, 'name': 'latte'},
        '3': {'water': 200, 'milk': 100, 'beans': 12, 'price': 6, 'name': 'cappuccino'}
    }

    # Константи станів
    STATE_MAIN = "choosing an action"
    STATE_BUY = "choosing a coffee type"
    STATE_FILL_WATER = "adding water"
    STATE_FILL_MILK = "adding milk"
    STATE_FILL_BEANS = "adding coffee beans"
    STATE_FILL_CUPS = "adding disposable cups"

    def __init__(self):
        """Ініціалізує машину початковими ресурсами та встановлює головний стан."""
        self.resources = {
            'water': 400,
            'milk': 540,
            'beans': 120,
            'cups': 9,
            'money': 550
        }
        self.state = self.STATE_MAIN
        self.fill_temp = {}  # Тимчасовий буфер для поповнення ресурсів

    def _display_resources(self):
        """Виводить у консоль поточну кількість усіх доступних ресурсів та грошей."""
        print("\nThe coffee machine has:")
        print(f"{self.resources['water']} ml of water")
        print(f"{self.resources['milk']} ml of milk")
        print(f"{self.resources['beans']} g of coffee beans")
        print(f"{self.resources['cups']} disposable cups")
        print(f"${self.resources['money']} of money")

    def _check_and_make_coffee(self, choice: str):
        """
        Перевіряє наявність ресурсів для обраного напою та готує його.

        Args:
            choice (str): Ключ рецепту в словнику RECIPES.
        """
        recipe = self.RECIPES[choice]
        lacks = None

        if self.resources['water'] < recipe['water']:
            lacks = "water"
        elif self.resources['milk'] < recipe['milk']:
            lacks = "milk"
        elif self.resources['beans'] < recipe['beans']:
            lacks = "coffee beans"
        elif self.resources['cups'] < 1:
            lacks = "disposable cups"

        if lacks:
            print(f"Sorry, not enough {lacks}!")
        else:
            print("I have enough resources, making you a coffee!")
            self.resources['water'] -= recipe['water']
            self.resources['milk'] -= recipe['milk']
            self.resources['beans'] -= recipe['beans']
            self.resources['cups'] -= 1
            self.resources['money'] += recipe['price']

    def _process_buy(self, user_input: str):
        """
        Логіка обробки вибору напою.

        Args:
            user_input (str): Номер напою або команда 'back'.
        """
        if user_input == 'back':
            self.state = self.STATE_MAIN
        elif user_input in self.RECIPES:
            self._check_and_make_coffee(user_input)
            self.state = self.STATE_MAIN
        else:
            print("Invalid choice. Please choose 1, 2, 3 or back:")

    def _process_fill(self, user_input: str):
        """
        Покрокова обробка процесу поповнення ресурсів (Fill).

        Перемикає внутрішні стани від води до стаканчиків.

        Args:
            user_input (str): Кількість ресурсу, введена користувачем.
        """
        try:
            value = int(user_input)
        except ValueError:
            value = 0

        if self.state == self.STATE_FILL_WATER:
            self.fill_temp['water'] = value
            self.state = self.STATE_FILL_MILK
            print("Write how many ml of milk do you want to add:")
        elif self.state == self.STATE_FILL_MILK:
            self.fill_temp['milk'] = value
            self.state = self.STATE_FILL_BEANS
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == self.STATE_FILL_BEANS:
            self.fill_temp['beans'] = value
            self.state = self.STATE_FILL_CUPS
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state == self.STATE_FILL_CUPS:
            self.fill_temp['cups'] = value

            # Масове оновлення ресурсів
            for key, val in self.fill_temp.items():
                self.resources[key] += val

            self.fill_temp = {}
            self.state = self.STATE_MAIN

    def process_input(self, user_input: str) -> bool:
        """
        Головний вхідний пункт для взаємодії з машиною.

        Визначає, яку дію виконати залежно від поточного стану `self.state`.

        Args:
            user_input (str): Введення користувача з консолі.

        Returns:
            bool: True, якщо машина продовжує роботу, False, якщо отримано 'exit'.
        """
        if user_input == 'exit':
            return False

        if self.state == self.STATE_MAIN:
            if user_input == 'buy':
                self.state = self.STATE_BUY
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            elif user_input == 'fill':
                self.state = self.STATE_FILL_WATER
                print("Write how many ml of water do you want to add:")
            elif user_input == 'take':
                print(f"I gave you ${self.resources['money']}")
                self.resources['money'] = 0
            elif user_input == 'remaining':
                self._display_resources()

        elif self.state == self.STATE_BUY:
            self._process_buy(user_input)

        elif self.state.startswith("adding"):
            self._process_fill(user_input)

        return True

# --- ЗАПУСК ПРОГРАМИ ---

def main():
    """Створює екземпляр CoffeeMachine та запускає нескінченний цикл взаємодії."""
    coffee_machine = CoffeeMachine()

    while True:
        # Виводимо підказку тільки у головному стані
        if coffee_machine.state == CoffeeMachine.STATE_MAIN:
            user_input = input("Write action (buy, fill, take, remaining, exit):\n")
        else:
            user_input = input()

        if not coffee_machine.process_input(user_input):
            break

if __name__ == "__main__":
    main()