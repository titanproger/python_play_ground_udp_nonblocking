import errno
import socket
import random


def read_from_udp(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    sock.setblocking(0)

    print("####### Server is listening #######")

    while True:
        try:
            data, address = sock.recvfrom(4096)
            # print("Received: ", data.decode('utf-8'), "\n")
            print data.decode('utf-8')
            yield
        except socket.error, e:
            if e.errno != errno.EAGAIN:
                raise e
            yield


def send_random_int(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(('127.0.0.1', port))
    sock.setblocking(0)

    while True:
        data = str(random.randint(0, 1000)) + '\n'
        # print 'Sending: ', data
        # print 'Bytes to send: ', len(data)
        total_sent = 0
        while len(data):
            try:
                sent = sock.send(data)
                total_sent += sent
                data = data[sent:]
                # print 'Sending data'
                yield
            except socket.error, e:
                if e.errno != errno.EAGAIN:
                    raise e
                yield


# actually it is adoption of
# @link = https://medium.com/vaidikkapoor/understanding-non-blocking-i-o-with-python-part-1-ec31a2e2db9b
# Reinventing the wheel =)

if __name__ == '__main__':
    tasks = [
        send_random_int(port=11234),
        read_from_udp(port=11235),
    ]

    # We reinventing JavaScript event Loop =)))))
    # Use Generators
    # May be better use Node.js ?

    while len(tasks):
        new_tasks = []
        for task in tasks:
            try:
                resp = next(task)
                new_tasks.append(task)
            except StopIteration:
                # function completed
                pass

        tasks = new_tasks
