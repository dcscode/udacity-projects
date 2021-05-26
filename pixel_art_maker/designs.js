// Select color input
let userColor = document.getElementById("colorPicker");

// Select size input
let canvasTable = document.getElementById("pixelCanvas");
let row = document.getElementById("inputHeight");
let column = document.getElementById("inputWidth");

// When size is submitted by the user, call makeGrid()
canvasSize = document.getElementById("sizePicker");


function makeGrid(row, column) {
	
	//clears table
	canvasTable.innerHTML = "";
	
	//makes table
	for(var i = 1; i <= row; i++){
		var canvasRow = canvasTable.insertRow();
		for(var j = 1; j <= column; j++){
			var canvasCell = canvasRow.insertCell();
			canvasCell.addEventListener("click",function(event){
				event.target.style.backgroundColor = userColor.value;
			})
		}
	}
};
//add unclick to clear

canvasSize.addEventListener("submit", function(event){
	event.preventDefault();
	let height = document.getElementById("inputHeight");
	let row = height.value;
	let width = document.getElementById("inputWidth");
	let column = width.value;
	makeGrid(row, column);
});
