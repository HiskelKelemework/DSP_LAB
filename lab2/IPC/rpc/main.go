package main

import (
	"fmt"
	"net"
	"net/http"
	"net/rpc"
)

func main() {
	arith := new(Arith)
	rpc.Register(arith)
	rpc.HandleHTTP()

	l, e := net.Listen("tcp", ":1234")
	if e != nil {
		fmt.Println("encountered an error")
		return
	}
	go http.Serve(l, nil)
}
