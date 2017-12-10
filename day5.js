/*
* Solution to https://adventofcode.com/2017/day/5
*
* Run using: node day5.js
*/

const fs = require('fs')

fs.readFile('./resources/day5-input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading input file", err)
    }
    const numSteps1 = processInput(data, adjustIdx_1)
    const numSteps2 = processInput(data, adjustIdx_2)
    console.log(`Num steps part 1: ${numSteps1}\nNum steps part 2: ${numSteps2}`)
})

function processInput (data, adjustIdx) {
    inputs = data.split("\n").map(i => parseInt(i))

    let idx = 0, count = 0
    while (idx < inputs.length - 1) {
        const jump = inputs[idx]
        const new_idx = idx + jump
        inputs[idx] = adjustIdx(jump)
        idx = new_idx
        count += 1   
    }
    return count
}

function adjustIdx_1 (offset) {
    return offset += 1
}

function adjustIdx_2 (offset) {
    return offset >= 3 ? offset -= 1 : offset += 1
}
