def be_polite(fun):
    def polite_fun():
        print("please")
        fun()
    return polite_fun

@be_polite
def come_back():
    print("Come back!")

@be_polite
def leave():
    print("Now Leave")
