<?php
function randomize($Name){
	/*	Logic: Generating a random number and concatinating it with name
		Using call by value, rand() and concat operator
		combine the name and number
		return the combined string.
	*/
	$GeneratedNumber = rand(6,15); //rand() function takes the min and max and genereates a random integer between the range
	$string = $Name ; //assigning the string with name
	$string .= " ";  // concat operator to insert space between name and number
	$string .= $GeneratedNumber; //concatinating the number at the end
	return $string;// returning the string
	
}
$nameAndNumber = randomize("Rohit"); //Function randmize as call by value, the result is stored in $nameAnd Number
echo $nameAndNumber; // Printing the concatenated name and number
