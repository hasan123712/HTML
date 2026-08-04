let player = "king"



let guess = 3

if(player === ""){
    console.log("please enter yur name here")
}
else if(guess < 1 || guess > 5){
    console.log("guess must be between 1 nd 5")
}
else{
    console.log("welcome", player)
}


let lucky_number = Math.floor(Math.random()*5)+1
console.log("your guess", guess)
console.log("lucky_number", lucky_number)

if(guess === lucky_number){
    console.log("congatulations, you won the lucky draw")
}
else{
    console.log("sorry better luck next time")
}

let seconds = 0

let timer = setInterval(()=>{
    seconds++
    console.log("time:", seconds, "seconds")
    
    if(seconds == 5){
        clearInterval(timer)
        console.log("game finished")
    }
}, 1000)