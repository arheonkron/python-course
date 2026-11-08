
def greeting(name: str, lang: str) -> str:
    return f"Привет, {name}! Отличный выбор! {lang} — хороший старт."

def is_adult(age: int) -> bool:
    return age>=18

def main() -> None:
    name = input("Как тебя зовут? ").strip() or "Незнакомец"
    lang = input("Какой твой любимый язык? ").strip() or "Python"
    age = eval(input("Сколько тебе лет?") or "17")
    print(greeting(name, lang))
    print(is_adult(age))


if __name__ == "__main__":
    main()
    