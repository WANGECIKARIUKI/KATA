//create a variable

arr1 = ["Telescopes", "Glasses", "Eyes", "Monocles"];

//create a function that will take the array of strings as arguments

function sortedArray(arr) {
    //sort the array from smallest to largest
    sort1 = function(a,b){
        return a.length - b.length}
    sorted = arr.sort(sort1);

    return sorted
}
console.log(sortedArray(arr1));