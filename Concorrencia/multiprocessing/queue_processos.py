import multiprocessing


def ping(queue):
    queue.put('Geek')  # Alcocação do dado na queue


def pong(queue):
    msg = queue.get()  # aguarda até que haja um dado na queue

    print(f'{msg} University')


def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    # Processos concorrentes
    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
