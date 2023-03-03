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
    let T: number = parseInt(readLine())
    for (let ctr = 0; ctr < T; ctr++) {
        let odd: string = ""
        let even: string = ""
        let S: string = readLine()
        let placement = 1
        for (let idx = 0; idx < S.length; idx++) {
            if (placement++ % 2 != 0) {
                odd += S[idx]
                continue
            }
            even += S[idx]
        }
        console.log(odd, even)
    }
}