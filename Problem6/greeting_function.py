def generate_greeting(name, language="Korean", message=""):
    if language == "Korean":
        if message:
            print(f"안녕하세요, {name}님! {message}")
        else:
            print(f"안녕하세요, {name}님!")
    elif language == "English":
        if message:
            print(f"Hello, {name}! {message}")
        else:
            print(f"Hello, {name}!")
    else:
        print( "지원되지 않는 언어입니다.")
    
generate_greeting("김철수")
generate_greeting("John", language="English")
generate_greeting("이영희", message="좋은 하루 되세요!")
