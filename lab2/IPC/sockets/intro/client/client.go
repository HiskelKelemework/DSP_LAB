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
	sock, err := net.Dial("tcp", "127.0.0.1:8000")
	if err != nil {
		fmt.Println("an error occured, couldn't connect to server")
		fmt.Print(err)
		return
	}

	var wg sync.WaitGroup
	wg.Add(2)
	go incomingHandler(sock)
	go outgoingHandler(sock)
	wg.Wait()
}
