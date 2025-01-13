if __name__ == "__main__":
    telephone_book = {"William A. Lathan" : "405-709-1865",
                    "John K. Miller" : "402-709-8568",
                    "Hortensia E. Foster" : "606-481",
                    "Amanda D. Newland" : "319-243-5613",
                    "Brooke P. Askew" : "307-687-2982"}
    print(len(telephone_book))
    x = input("Enter function: ")
    if x == "extend":
        for i in range(10):
            telephone_book[i, "example"] = 8956876
print(len(telephone_book))