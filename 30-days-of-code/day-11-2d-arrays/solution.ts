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

    let arr: number[][] = Array(6);

    for (let i: number = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }
    
    let result: number = Number.NEGATIVE_INFINITY
    for (let idx: number = 0; idx < 4; idx++) {
        for(let jdx: number = 0; jdx < 4; jdx++) {
            let sum: number = 0;
            sum += arr[idx+0][jdx+0] + arr[idx+0][jdx+1] + arr[idx+0][jdx+2]
            sum += arr[idx+1][jdx+1]
            sum += arr[idx+2][jdx+0] + arr[idx+2][jdx+1] + arr[idx+2][jdx+2]
            if (result < sum) {
                result = sum
            }
        }
    }
    console.log(result)
}
