#!/bin/bash

# build for linux
# GOPATH: /opt/Golang
docker run --rm -v "$PWD":/usr/src/myapp -v /opt/Golang/src:/go/src -w /usr/src/myapp golang:latest go build -buildmode=c-shared -o go-palette-linux.so pyapi.go

# build for mac
go build -buildmode=c-shared -o go-palette-mac.so pyapi.go

# copy to pypalette
cp *.so ../pypalette/
