// Very basic socket server
// https://golangr.com/

package main

import (
	"bufio"
	"fmt"
	"net"
)

func broadcast(sockets []net.Conn, socket net.Conn) {
	for {
		message, _ := bufio.NewReader(socket).ReadString('\n')

		for _, conn := range sockets {
			fmt.Print("Message Received:", string(message))
			fmt.Fprintf(conn, message+"\n")
		}
	}
}

func main() {
	fmt.Println("Start server...")
	sockets := []net.Conn{}

	// listen on port 8000
	ln, _ := net.Listen("tcp", ":8000")

	for {
		// accept connection
		conn, _ := ln.Accept()
		sockets = append(sockets, conn)

		go broadcast(sockets, conn)
	}
}
