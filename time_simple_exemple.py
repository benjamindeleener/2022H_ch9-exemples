from time import time

def temps_repeat(repetitions):
    def decorateur_temps(func):
        def wrapper(*args, **kwargs):
            temps = []
            for _ in range(repetitions):
                begin = time()
                resultat = func(*args, **kwargs)
                end = time()
                temps.append(end-begin)
            print(f'Cela a pris {sum(temps)/repetitions} secondes!')
            return resultat
        return wrapper
    return decorateur_temps

@temps_repeat(repetitions=100)
def some_function():
    some_list = [i for i in range(1000)]

    new_list = []
    for elem in some_list:
        new_list.append([i for i in range(elem)])


some_function()
