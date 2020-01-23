package main

import "fmt"

type node struct {
	value int
	left  *node
	right *node
}

type tree struct {
	root *node
}

func (t *tree) insert(n *node) {
	if t.root == nil {
		t.root = n
		return
	}
	current_node := t.root

	for current_node == nil {
		if current_node.value < n.value {
			if current_node.left == nil {
				current_node.left = n
				fmt.Println("Inserted:", n.value)
				return
			} else {
				current_node = current_node.left
			}
		} else {
			if current_node.right == nil {
				current_node.right = n
				fmt.Println("Inserted:", n.value)
				return
			} else {
				current_node = current_node.right
			}
		}
	}

}

func main() {
	var t tree
	t.insert(&node{value: 5})
	t.insert(&node{value: 4})
	t.insert(&node{value: 6})
	fmt.Println(t.root.value)
	fmt.Println(t.root.left.value)
	fmt.Println(t.root.right.value)
}
