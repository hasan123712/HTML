let song = ["Dangerous", "Qalbi Fil Madina", "Nathional Treaasaures", "I am not afraid", "No Face"]

let num = [13, 45, 56 ,23, 45]

song.sort()
console.log(song)
song.reverse()
console.log(song)


num.sort(function(a,b){
    return a - b
})
console.log(num)

num.sort(function(a,b){
    return b - a
})
console.log(num)

let square = num.map(function(n){
    return n * n
})

console.log(square)
