package main

import (
	"log"
	"net"
	"net/http"
	"net/rpc"
)

type Args struct {
	Num1 int
	Num2 int
}

type API int

func (a *API) Add(args Args, reply *int) error {
	*reply = args.Num1 + args.Num2
	return nil
}

func (a *API) Sub(args Args, reply *int) error {
	*reply = args.Num1 - args.Num2
	return nil
}

func main() {
	api := new(API)
	err := rpc.Register(api)
	if err != nil {
		log.Fatal("error registering API", err)
	}

	rpc.HandleHTTP()

	listener, err := net.Listen("tcp", ":4040")

	if err != nil {
		log.Fatal("Listener error", err)
	}
	log.Printf("serving rpc on port %d", 4040)
	http.Serve(listener, nil)

	if err != nil {
		log.Fatal("error serving: ", err)
	}
}
