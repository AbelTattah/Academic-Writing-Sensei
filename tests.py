from main import main
kofi = main.Kofi()

def test_ask_question():
    assert type(kofi.ask_question("What is academic writing?")) == str

def test_chat_completion():
    assert type(kofi.chat_completion([{"role":"user","content":"What is academic writing?"}])) == str

if __name__ == "__main__":
    test_ask_question()
    test_chat_completion()
    print("All tests passed!")