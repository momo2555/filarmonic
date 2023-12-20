from datagram.datagram_server import DatagramSocket


if __name__ == "__main__":
    detection = DatagramSocket()
    detection.run_server()
