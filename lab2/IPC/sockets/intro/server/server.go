package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	l, _ := net.Listen("tcp", "127.0.0.1:8000")

	// for {
	sock, _ := l.Accept()
	message, _ := bufio.NewReader(sock).ReadString('\n')
	fmt.Println("client: ", message)
	// fmt.Fprintf(sock, "hello from server")
	fmt.Fprintf(sock, "hello from server via bufio\n")
	sock.Close()
	// }
}
