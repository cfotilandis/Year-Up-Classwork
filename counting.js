
function doCount(nameBox,numBox,incBox){
	finalAnswer = "<p> Hello " + nameBox + "</p>"
		
	numBreak=""

	maxVal = 100

	lowerVal = 3
	
	var nameRestrict=regex=/^[a-zA-Z '-]+$/;
	//determines what text is allowed in the name box.

	if(!nameBox || !numBox){
		alert("*Please enter information in both the name and number box!*");
		console.log("The user didn't enter any information in one or both of the boxes")
		info.reset();
		document.info.nameBox.focus();
		document.getElementById("answer").innerHTML = ""	
		//If no data is entered.
	} else {
		

	if(isNaN(numBox)){
		alert("*Please enter a proper number!*");
		console.log(nameBox +" tried to not enter a number.  They entered " + numBox + " instead.")
		info.reset();
		document.info.numBox.focus();
		document.getElementById("answer").innerHTML = ""
		//if "not a number" is in the number box
	} else {

	if(isNaN(incBox)){
		alert("*Please enter a number for the increment.*")
		console.log(nameBox +" tried to not enter a number for the increment.  They entered " + incBox + " instead.")
		info.reset();
		document.info.numBox.focus();
		document.getElementById("answer").innerHTML = ""
		//If the increment box is a number or not.
	} else {

	if(numBox < lowerVal) {
		alert("*Please enter a number greater than " + lowerVal + "!*");
		console.log(nameBox +" tried to not enter a number that was too low.  They entered " + numBox + " instead.")
		info.reset();
		document.info.numBox.focus();
		document.getElementById("answer").innerHTML = ""
		//if the number entered is lower than the lower value
	} else {


	if(!nameBox.match(nameRestrict)){
		alert("*Please enter a proper name!*")
		console.log("The user tried to enter " + nameBox + " instead of a name")
		info.reset();
		document.info.nameBox.focus();
		document.getElementById("answer").innerHTML = ""
		//if the name contains symbols/numbers.
	} else {

	
	//Final step.  Checks to see if the number entered is between the values.  If it's greater, the function should still perform but with the max value instead of their number.
	if(numBox>maxVal){
		
		numBox = maxVal
		alert("*Please put a number lower than " + maxVal + "!  Your number has been adjusted to " + maxVal + ".*")
		console.log(nameBox +" tried to enter a number higher than " + maxVal)
		document.info.numBox.value = maxVal
		document.info.numBox.focus();
		//if they enter a number greater than the maximum value
		} else {
		console.log(nameBox + " entered " + numBox)
		}
	
	if(numBox % 2 == 0 ){
			 startNum = 0
		} else {
			 startNum = 1
		}
	//function to choose whether to start at "1" or "0" depending on if its odd or even.
	
	
	if(!incBox){
		incBox = 2
	} 

	incBox=parseInt(incBox)
	for(i=startNum;i<=numBox;i+=incBox){

				numBreak= numBreak + i + "<br>"

		//function that types out each number until it hits the entered number.
		}
		document.getElementById("answer").innerHTML = finalAnswer + "The number entered is: " + numBox + "<br>" + numBreak;
		//show data, only if everything works EXCEPT for if the value is more than the max value.
		}
		}
}
}
}
}


