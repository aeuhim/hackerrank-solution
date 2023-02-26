'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;
process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';
    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

function main() {
    // Enter your code here
    let i: number;
    let d: number;
    let s: string;
    i = parseInt(readLine())
    d = parseFloat(readLine())
    s = readLine()
    console.log(4 + i)
    console.log((4 + d).toFixed(1))
    console.log("HackerRank " + s)
}