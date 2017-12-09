/*
* Solution to https://adventofcode.com/2017/day/2
*
* Run using: node day2.js
*/

const fs = require('fs')

fs.readFile('resources/day2-input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading input file", err)
    }
    const part1 = calculateChecksum(data, getDifference)
    const part2 = calculateChecksum(data, evenlyDivide)
    console.log(`Checksum part 1: ${part1}, checksum part 2: ${part2}`)
})

function calculateChecksum (data, calculateFn) {
    return data.split("\n")                     // get each row of the table
        .map(row => row.split("\t"))            // get each element of each row
        .map(row => row.map(i => parseInt(i)))
        .map(row => calculateFn(row))  
        .reduce((sum, i) => sum + i, 0)
}

/* 
* part 1: find the difference between the highest and
* lowest values
*/
function getDifference (numbers) {
    const sorted = numbers.sort((i, j) => i - j)
    return sorted[sorted.length-1] - sorted[0]
}

/* 
* part 2: find the two numbers that evently divide and
* return the result 
*/
function evenlyDivide (numbers) {
    let result = null
    let i = 0
    do {
        let j = 0
        do {
            let candidate = numbers[i]/numbers[j]
            result = isSolution(candidate) ? candidate : null
            j++
        } while (!result && j < numbers.length)
        i++
    } while (!result)
    return result
}

function isSolution(candidate) {
    return Number.isInteger(candidate) && candidate !== 1
}