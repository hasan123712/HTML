let score = 600
console.log(typeof(score))


let name = "Bob"
console.log(typeof(name))


let gameover = true
console.log(typeof(gameover))


// convert

let value = "23424"
console.log(typeof(value))

let tree = Number(value)
console.log(tree)
console.log(typeof(tree))

// replace

let greet = "Hello my name is Hasan"

console.log(greet.replace("Hasan", "bob"))

console.log(greet.search("name"))

// try..catch


let input = "abc"

try{
    let number = Number(input)
    if(isNaN(Number)){
        throw "invalid number entered"
    }
}
catch(error){
    console.log(error)
}