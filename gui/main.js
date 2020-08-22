function update(type, text) {
	var node = document.createElement("li");
	switch(type) {
		case "error":
			node.style.color = "red";
			break;
		case "warning":
			node.style.color = "yellow";
			break;
		case "info":
			node.style.color = "blue";
			break;
		default:
			node.style.color = "black";
			break;
	}
	node.appendChild(document.createTextNode(text));
	document.getElementById("log").appendChild(node);
}
