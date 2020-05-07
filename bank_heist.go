package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {
rand.Seed(time.Now().UnixNano())
var isHeistOn bool
isHeistOn = true
eludedGuards := rand.Intn(100)

if eludedGuards >= 50 {
  fmt.Println("Looks like you've managed to make it past the guards. Good job, but remember, this is the first step.")
} else {
  isHeistOn = false
  fmt.Println("Plan a better disguise next time?")
}
openedVault := rand.Intn(100)
if isHeistOn && openedVault >= 70 {
  fmt.Println("Grab and GO!")
} else if isHeistOn {
  isHeistOn = false
  fmt.Println("The vault can't be opened")
}

if isHeistOn {
  leftSafely:= 0
  switch leftSafely {
    case 0:
    isHeistOn = false
    fmt.Print("Looks like you tripped an alarm... run?")
    case 1:
    isHeistOn = false 
    fmt.Print("Turns out vault doors don't open from the inside...")  
  case 2:
     // Code for another failure
  case 3:
     // Code for another failure
  default:
    fmt.Println("Start the getaway car!") 
  }
}
if isHeistOn {
  amStolen := 10000 + rand.Intn(1000000)
   fmt.Println("Huhuhul", amStolen)  
}

fmt.Println("isHeistOn is currently:", isHeistOn)
}
