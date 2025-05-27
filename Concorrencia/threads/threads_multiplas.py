import threading
import time


def main():
    threads = [
        threading.Thread(target=contar, args=('Elefante', 10)),
        threading.Thread(target=contar, args=('Buraco', 8)),
        threading.Thread(target=contar, args=('Moeda', 7)),
        threading.Thread(target=contar, args=('Pato', 6))
    ]

    # Adição ao pool de thread prontos para execução.
    [th.start() for th in threads]

    print('Podemos fazer outras coisas no programa enaquanto a thread vai executando.')
    print('Geek University' * 2)

    # Avisa para ficar aguardando aqui até a thread terminar a execução.
    [th.join() for th in threads]

    print('Pronto')


def contar(nome, numero):
    for n in range(1, numero + 1):
        print(f'{n} {nome}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
