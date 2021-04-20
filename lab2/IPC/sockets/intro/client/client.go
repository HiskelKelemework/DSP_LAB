package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	sock, err := net.Dial("tcp", "127.0.0.1:8000")
	if err != nil {
		fmt.Println("an error occured, couldn't connect to server")
		fmt.Print(err)
		return
	}

	clientMsg := "this is a message from the client\n"
	// fmt.Fprint(sock, clientMsg)
	writer := bufio.NewWriter(sock)
	writer.WriteString(clientMsg)
	writer.Flush()

	serverMsg, _ := bufio.NewReader(sock).ReadString('\n')
	fmt.Println("server: ", serverMsg)
}
