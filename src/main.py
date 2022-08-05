import zmq

EDDN = "tcp://eddn.edcd.io:9500"
__timeoutEDDN = 60000

def main():

    try:
        context = zmq.Context()

        # Socket for imbound traffic
        frontend = context.socket(zmq.SUB)
        frontend.setsockopt(zmq.SUBSCRIBE, b"")
        frontend.setsockopt(zmq.RCVTIMEO, __timeoutEDDN)

        # Socket for outbound traffic
        backend = context.socket(zmq.PUB)
        backend.bind("tcp://*:9501")

        while True:
            frontend.connect(EDDN)

            while True:
                msg = frontend.recv()

                if msg == False:
                    frontend.disconnect(EDDN)
                    break
                
                backend.send(msg)

    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()