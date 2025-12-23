# Етап 3: Визначення всіх тварин, створення списку та запит вводу

# --- Зображення тварин (ASCII Art) ---

camel = r"""
The camel habitat...
___.-''''-.
/___ @ |
',,,,. | _.'''''''._
' | / \
| \ _.-' \
| '.-' '-.
| ',
| '',
',,-, ':;
',,| ;,, ,' ;;
! ; !'',,,',',,,,'! ; ;:
: ; ! ! ! ! ; ; :;
; ; ! ! ! ! ; ; ;,
; ; ! ! ! ! ; ;
; ; ! ! ! ! ; ;
;,, !,! !,! ;,;
/_I L_I L_I /_I
Look at that!"""

lion = r"""
The lion habitat...
,w.
,YWMMw ,M ,
_.---.._ __..---._.'MMMMMw,wMWmW,
_.-"" ''' YP"WMMMMMMMMMb,
.-' __.' .' MMMMW^WMMMM;
_, .'.-'"; `, /` .--"" :MMM[==MWMW^;
,mM^" ,-'.' / ; ; / , MMMMb_wMW" @\
,MM:. .'.-' .' ; `\ ; `, MMMMMMMW `"=./`-,
WMMm__,-'.' / _.\ F'''-+,, ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-' ,-' _.--"" `-, ; \ ; ;MMMMMMMMMMW^``; __|
/ .' ; ; ) )`{ \ `"^W^`, \ :
/ .' / ( .' / Ww._ `. `"
/ Y, `, `-,=,_{ ; MMMP`""-, `-._.-,
(--, ) `,_ / `) \/"") ^" `-, -;"\:
The lion is roaring!"""

deer = r"""
The deer habitat...
/| |\
`__\\ //__'
|| ||
\__`\ |'__/
`_\\ //_'
_.,:---;,._
\_: :_/
|@. .@|
| |
,\.-./ \
;;`-' `---__________-----.-.
;;; \_\
';;; |
; | ;
\ \ \ | /
\_, \ / \ |\
|';| |,,,,,,,,/ \ \ \_
| | | \ / |
\ \ | | / \ |
| || | | | | |
| || | | | | |
| || | | | | |
|_||_| |_| |_|

/_//_/ /_/ /_/
Pretty good!"""

goose = r"""
The goose habitat...

_
,-"" "".
,' ____ `.
,' ,' `. `._
(`. _..--.._ ,' ,' \ \
(`-.\ .-"" ""' / ( d _b
(`._ `-"" ,._ ( `-( \
<_ ` ( <`< \ `-._\
<`- (__< < :
(__ (_<_< ;
`------------------------------------------
Beautiful!"""

bat = r"""
The bat habitat...
_________________ _________________
~-. \ |\___/| / .-~
~-. \ / o o \ / .-~
> \\ W // <
/ /~---~\ \
/_ | | _\
~-. | | .-~
; \ / i
/___ /\ /\ ___\
~-. / \_/ \ .-~
V V
It's doing fine."""

rabbit = r"""
The rabbit habitat...
,
/| __
/ | ,-~ /
Y :| // /
| jj /( .^
>-"~"-v"
/ Y
jo o |
( ~T~ j
>._-' _./
/ "~" |
Y _, |
/| ;-"~ _ l
/ l/ ,-"~ \
\//\/ .- \
Y / Y
l I !
]\ _\ /"\
(" ~----( ~ Y. )
It looks fine!"""

# --- Основна логіка Етапу 4 (З циклом і виходом) ---

# Створення списку (індекси: 0-camel, 1-lion, 2-deer, 3-goose, 4-bat, 5-rabbit)
animals = [camel, lion, deer, goose, bat, rabbit]

# Головний цикл програми
while True:
    # Запитуємо ввід від користувача
    user_input = input("Please enter the number of the habitat you would like to view: ")

    # Перевірка на умову виходу (якщо введено 'exit')
    if user_input.lower() == 'exit':
        break # Вихід з циклу while

    try:
        # Перетворюємо введений рядок на число (індекс)
        index = int(user_input)

        # Перевірка на допустимий діапазон індексу
        if 0 <= index < len(animals):
            print(animals[index])
        else:
            print(f"Error: Habitat number {index} is out of range (0-{len(animals)-1}).")

    except ValueError:
        # Обробка, якщо користувач ввів не число і не 'exit'
        print("Error: Please enter a number or 'exit'.")

# Повідомлення про завершення роботи програми (виконується після виходу з циклу)
print("See you later!")