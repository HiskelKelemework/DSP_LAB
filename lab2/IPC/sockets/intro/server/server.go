package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"sync"
)

func incomingHandler(socket net.Conn) {
	for {
		serverMsg, _ := bufio.NewReader(socket).ReadString('\n')
		fmt.Println("server: ", serverMsg)
	}
}

func outgoingHandler(socket net.Conn) {
	for {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Text to send: ")
		clientMsg, _ := reader.ReadString('\n')
		writer := bufio.NewWriter(socket)
		writer.WriteString(clientMsg + "\n")
		writer.Flush()
	}
}

func main() {
	l, _ := net.Listen("tcp", "127.0.0.1:8000")

	sock, _ := l.Accept()

	var wg sync.WaitGroup
	wg.Add(2)

	go incomingHandler(sock)
	go outgoingHandler(sock)

	wg.Wait()
}
