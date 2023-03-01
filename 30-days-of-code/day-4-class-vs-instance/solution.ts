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

class Person {
    age: number
    constructor(initialAge: number) {
        if (initialAge < 0) {
            console.log("Age is not valid, setting age to 0.")
            this.age = 0
            return this
        }
        this.age = initialAge
    }
    yearPasses(): void {
        this.age += 1
    }
    amIOld(): void {
        if (this.age < 13) {
            console.log("You are young.")
            return
        }
        if (13 <= this.age && this.age < 18) {
            console.log("You are a teenager.")
            return
        }
        console.log("You are old.")
    }
    
}

function main() {
    // Enter your code here
    let case_count: number = parseInt(readLine())
    let person: Person;
    for (let itr = 0; itr < case_count; itr++)  {
        person = new Person(parseInt(readLine()))
        person.amIOld()
        person.yearPasses()
        person.yearPasses()
        person.yearPasses()
        person.amIOld()
        console.log()
    }
}
