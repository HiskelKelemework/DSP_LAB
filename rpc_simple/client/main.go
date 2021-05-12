package main

import (
	"fmt"
	"log"
	"net/rpc"
)

type Args struct {
	Num1 int
	Num2 int
}

func main() {
	var reply int

	client, err := rpc.DialHTTP("tcp", "localhost:4040")

	if err != nil {
		log.Fatal("Connection error: ", err)
	}

	args := Args{9, 4}

	client.Call("API.Add", args, &reply)

	fmt.Println("sum is: ", reply)
}
