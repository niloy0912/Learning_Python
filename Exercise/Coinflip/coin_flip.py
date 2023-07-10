entries = []
counter = int(0)
percentage_of_heads = int(0)

with open("Coinflips.txt", 'w') as file:
    while True:
        entry = input("Throw the coin and enter head o tail: ")
        entries.append(entry)
        match entry:
            case "head":
                counter = counter + 1
                percentage_of_heads = (counter / len(entries)) * 100
                print(f"Head: {percentage_of_heads}%")
                file.write(entry + '\n')
            case "tail":
                percentage_of_heads = (counter / len(entries)) * 100
                print(f"Head: {percentage_of_heads}%")
                file.write(entry + '\n')
            case "exit":
                break


