
def greeting(name: str, lang: str) -> str:
    return f"Привет, {name}! Отличный выбор! {lang} — хороший старт."

def ask_age() -> int:
    while True:
        raw = input("Сколько тебе лет? ").strip()
        if not raw:
            return 17
        try:
            return int(raw)
        except ValueError:
            print("Нужно целое число, попробуй ещё раз.")

def is_adult(age: int) -> bool:
    return age >= 18

def main() -> None:
    name = input("Как тебя зовут? ").strip() or "Незнакомец"
    lang = input("Какой твой любимый язык? ").strip() or "Python"
    status = "совершеннолетний" if is_adult(age) else "несовершеннолетний"
    print(f"Ты {status}.")
    print(greeting(name, lang))
    print(is_adult(age))


if __name__ == "__main__":
    main()
    