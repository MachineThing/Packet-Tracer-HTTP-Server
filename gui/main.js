function update(type, text) {
	var node = document.createElement("li");
	switch(type) {
		case "3":
			node.style.color = "red";
			break;
		case "2":
			node.style.color = "yellow";
			break;
		case "1":
			node.style.color = "blue";
			break;
		default:
			node.style.color = "black";
			break;
	}
	node.appendChild(document.createTextNode(text));
	document.getElementById("log").appendChild(node);
}
