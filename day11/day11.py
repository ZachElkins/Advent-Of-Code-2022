from helpers.file_reader import FileReader
from pathlib import Path
from copy import deepcopy


def op_to_fn(text):
    details = text.split()
    op, value = details[-2], details[-1]
    if op == "*":
        if value == "old":
            return lambda x: x*x
        return lambda x: x*int(value)
    if op == "+":
        if value == "old":
            return lambda x: x+x
        return lambda x: x+int(value)


def test_dict_to_fn(test):
    divisor = int(test["criteria"].split()[-1])
    return lambda x: int(test['true']) if x % divisor == 0 else int(test['false'])


def get_monkeys(lines):
    monkeys = []
    test = {}
    for line in lines:
        if line.startswith("Monkey"):
            monkeys.append({"name": int(line.split()[1][:-1])})
        elif line.startswith("Starting"):
            monkeys[-1]["items"] = list(map(lambda x: int(x), line.split(":")[1].split(",")))
        elif line.startswith("Operation"):
            monkeys[-1]["op"] = op_to_fn(line.split(":")[1])
        elif line.startswith("Test"):
            test = {"criteria": line.split(":")[1].strip()}
        elif line.strip().startswith("If"):
            test[line.split()[1][:-1]] = line.split(":")[1].strip().split()[-1]
        else:
            monkeys[-1]["test"] = test_dict_to_fn(test)
            monkeys[-1]["inspected"] = 0
            
    monkeys[-1]["test"] = test_dict_to_fn(test)
    monkeys[-1]["inspected"] = 0

    return monkeys


def get_monkey_buisness(monkeys):
    inspections = [monkey['inspected'] for monkey in monkeys]
    inspections.sort()
    monkey_buisness = inspections[-1] * inspections[-2]
    return monkey_buisness


def part_one(monkeys):
    for _ in range(20):
        for m in range(len(monkeys)):
            while monkeys[m]["items"]:
                worry = monkeys[m]["op"](monkeys[m]["items"].pop(0))
                worry = worry//3
                throw_to = monkeys[m]["test"](worry)
                monkeys[throw_to]["items"].append(worry)
                monkeys[m]["inspected"] += 1

    print(f"After 20 rounds the monkey buisness reached {get_monkey_buisness(monkeys)}.")


def part_two(monkeys):
    for _ in range(10000):
        for m in range(len(monkeys)):
            while monkeys[m]["items"]:
                worry = monkeys[m]["op"](monkeys[m]["items"].pop(0))
                # Prime factorization of 9699690 2, 3, 5, 7, 11, 13, 17, 19
                # which is all the values being checked in the monkey's operation
                # this lets us avoid very big numbers
                worry = worry % 9699690
                throw_to = monkeys[m]["test"](worry)
                monkeys[throw_to]["items"].append(worry)
                monkeys[m]["inspected"] += 1

    print(f"After 10000 rounds the monkey buisness reached {get_monkey_buisness(monkeys)}.")

    
def main():
    lines = FileReader.read_lines(Path(__file__).parent.absolute())
    monkeys = get_monkeys(lines)
    
    part_one(deepcopy(monkeys))
    part_two(monkeys)


if __name__ == "__main__":
    main()