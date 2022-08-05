# EDDN forwarder

This application gets ZeroMQ messages frmo EDDN and forwards them
into a local networks. The forwarder receives a single data stream
from EDDN, even if multiple applications uses the EDDN messages.
The local applications just connect to the local port of the forwarder.

## Usage
The application is started with the command ./start.sh. Local applications
connect to tcp://localhost:9501 instead of tcp://eddn.edcd.io:9500.