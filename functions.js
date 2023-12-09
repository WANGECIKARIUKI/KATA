/*Instructions
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]*/

// create a function



function capitals(word){
    //create a variable with an empty array

    let arr = [];
    // for loop increment

    for (let i = 0; i < word.length; i++) {
        if(arr[i] === arr[i].toUpperCase()){
        arr.push(i);
    }
}
    return arr
}