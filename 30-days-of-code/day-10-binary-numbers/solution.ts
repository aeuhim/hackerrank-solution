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
    const n: number = parseInt(readLine().trim(), 10);
    const binary: string = n.toString(2)
    let max_count: number = 0
    let counter: number = 0;
    for (let bit of binary) {
        if (bit === '1') {
            counter++
        }
        if (max_count < counter) {
            max_count = counter
        }
        if (bit === '1') {
            continue
        }
        counter = 0
    }
    console.log(max_count)
}
