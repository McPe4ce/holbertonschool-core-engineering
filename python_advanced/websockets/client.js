// TODO: implement the WebSocket client

logs = document.getElementById("log")
form = document.getElementById("form")
textzone = document.getElementById("textzone")
sendBtn = document.getElementById("sendBtn")
statusDot = document.getElementById("statusDot")

const socket = new WebSocket(`ws://${location.host}/ws`)

socket.addEventListener("open", () => {
    statusDot.classList.add("open")
    sendBtn.disabled = false
})

socket.addEventListener("close", () => {
    statusDot.classList.add("closed")
    sendBtn.disabled = true
})

socket.addEventListener("error", () => {
    let par = document.createElement("p")
    par.textContent = "Connection error"
    par.classList.add("info")
    logs.appendChild(par)
})


socket.addEventListener("message", (event) => {
    let par = document.createElement("p")
    par.textContent = event.data
    par.classList.add("received")
    logs.appendChild(par)
})

form.addEventListener("submit", (event) => {
    event.preventDefault()
    message = textzone.value
    socket.send(message)
    
    let par = document.createElement("p")
    par.textContent = message
    par.classList.add("sent")
    logs.appendChild(par)

    textzone.value = ""
})

socket