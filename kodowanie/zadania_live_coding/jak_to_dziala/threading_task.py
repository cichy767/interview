from threading import Thread

count = 0


def adder(x):
    global count
    for _ in range(x):
        count += 1


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = Thread(target=adder, args=(100000,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

print(count)