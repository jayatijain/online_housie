from random import randint

from django.shortcuts import render

server_numbers = set()


def client(request):
    numbers = set()
    for n in range(15):
        added = 0
        while added == 0:
            nxt = randint(1, 100)
            if nxt not in numbers:
                numbers.add(nxt)
                added = 1
    return render(request, "housie/housie.html", {'numbers': sorted(numbers)})


def server(request):
    added = 0
    while added == 0:
        next_number = randint(1, 100)
        if next_number not in server_numbers:
            server_numbers.add(next_number)
            added = 1
    return render(request, "housie/housie_server.html",
                  {'next_number': next_number, 'server_numbers': sorted(server_numbers)})


def reset_housie(request):
    server_numbers.clear()
    next_number = randint(1, 100)
    server_numbers.add(next_number)
    return render(request, "housie/housie_server.html",
                  {'next_number': next_number, 'server_numbers': sorted(server_numbers)})
