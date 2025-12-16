# Етап 6: Клас, стани, фінальна версія

class CoffeeMachine:
    # Рецепти (вода, молоко, зерна, ціна)
    RECIPES = {
        '1': {'water': 250, 'milk': 0, 'beans': 16, 'price': 4, 'name': 'espresso'},
        '2': {'water': 350, 'milk': 75, 'beans': 20, 'price': 7, 'name': 'latte'},
        '3': {'water': 200, 'milk': 100, 'beans': 12, 'price': 6, 'name': 'cappuccino'}
    }

    # Стан автомата
    STATE_MAIN = "choosing an action"
    STATE_BUY = "choosing a coffee type"
    STATE_FILL_WATER = "adding water"
    STATE_FILL_MILK = "adding milk"
    STATE_FILL_BEANS = "adding coffee beans"
    STATE_FILL_CUPS = "adding disposable cups"

    def __init__(self):
        # Початкові ресурси
        self.resources = {
            'water': 400,
            'milk': 540,
            'beans': 120,
            'cups': 9,
            'money': 550
        }
        self.state = self.STATE_MAIN
        self.fill_temp = {}  # Для тимчасового зберігання введених значень при fill

    def _display_resources(self):
        """Виводить поточний стан кавомашини."""
        print("\nThe coffee machine has:")
        print(f"{self.resources['water']} of water")
        print(f"{self.resources['milk']} of milk")
        print(f"{self.resources['beans']} of coffee beans")
        print(f"{self.resources['cups']} of disposable cups")
        print(f"{self.resources['money']} of money")

    def _check_and_make_coffee(self, choice):
        """Перевіряє ресурси і готує каву."""
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
            # Зменшення ресурсів
            self.resources['water'] -= recipe['water']
            self.resources['milk'] -= recipe['milk']
            self.resources['beans'] -= recipe['beans']
            self.resources['cups'] -= 1
            self.resources['money'] += recipe['price']

    def _process_buy(self, user_input):
        """Обробляє введення користувача в стані buy."""
        if user_input == 'back':
            self.state = self.STATE_MAIN
        elif user_input in self.RECIPES:
            self._check_and_make_coffee(user_input)
            self.state = self.STATE_MAIN # Повернення до головного меню
        else:
            # Повторний запит, якщо введення невалідне
            print("Invalid choice. Please choose 1, 2, 3 or back:")
            return

    def _process_fill(self, user_input):
        """Обробляє введення користувача в стані fill."""
        try:
            value = int(user_input)
        except ValueError:
            # Припускаємо, що введення завжди коректне (згідно з прикладами)
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

            # Додаємо всі накопичені ресурси
            for key, val in self.fill_temp.items():
                self.resources[key] += val

            self.fill_temp = {}
            self.state = self.STATE_MAIN # Повернення до головного меню

    def process_input(self, user_input):
        """Основний метод обробки введення."""
        if user_input == 'exit':
            return False  # Сигнал для завершення зовнішнього циклу

        if self.state == self.STATE_MAIN:
            if user_input == 'buy':
                self.state = self.STATE_BUY
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            elif user_input == 'fill':
                self.state = self.STATE_FILL_WATER
                print("Write how many ml of water do you want to add:")
            elif user_input == 'take':
                print(f"I gave you {self.resources['money']}")
                self.resources['money'] = 0
            elif user_input == 'remaining':
                self._display_resources()
            # Інакше (невідома команда в main state) - ігноруємо

        elif self.state == self.STATE_BUY:
            self._process_buy(user_input)

        elif self.state.startswith("adding"): # Обробка всіх станів fill
            self._process_fill(user_input)

        return True # Продовжувати роботу

# --- ГОЛОВНА ПРОГРАМА ---

coffee_machine = CoffeeMachine()

while True:
    # Виводимо наступний запит залежно від стану
    if coffee_machine.state == CoffeeMachine.STATE_MAIN:
        user_input = input("Write action (buy, fill, take, remaining, exit):\n")
    elif coffee_machine.state == CoffeeMachine.STATE_BUY:
        user_input = input() # Запит вже був виведений у process_input
    elif coffee_machine.state.startswith("adding"):
        user_input = input() # Запит вже був виведений у process_input
    else:
        # Недосяжний стан
        break

    if not coffee_machine.process_input(user_input):
        break