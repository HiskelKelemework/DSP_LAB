package client

import (
	"fmt"
	"net/rpc"
)

func main() {
	client, err := rpc.DialHTTP("tcp", "127.0.0.1:1234")

	if err != nil {
		fmt.Println("an error occured, could not connect")
		return
	}

	var reply int
	args := server.Args{A: 12, B: 15}
	client.Call("Arith.Multiply", &args, &reply)
}
