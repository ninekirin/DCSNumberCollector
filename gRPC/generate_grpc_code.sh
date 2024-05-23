#!/bin/bash

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. dcs_number_collector.proto