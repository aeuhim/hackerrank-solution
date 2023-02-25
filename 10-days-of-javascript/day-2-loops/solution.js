'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowels = ""
    let consonants = ""
    for (let idx = 0; idx < s.length; idx++) {
        switch(s.charAt(idx)) {
            case "a":
            case "e":
            case "i":
            case "o":
            case "u":
                vowels += s.charAt(idx) + "\n"
                break
            default:
                consonants += s.charAt(idx) + "\n"
        }
    }
    console.log(vowels + consonants)
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}