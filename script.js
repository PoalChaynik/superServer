const API = 'http://127.0.0.1:81'

let myMsg = document.querySelector('.myMsg')
let chatMsg = document.querySelector('.chatazinas')
let vards = document.querySelector('.vards')

function sutitZinu(){
    console.log('sutitzinu() darbojas')
    chatMsg.innerHTML += '<br/>' + myMsg.value
    fetch(API+'/send/'+vards.value+'/'+myMsg.value)
}

async function loadChatMsg(){
    let dataFromServer = await fetch(API + '/read')
    let data = await dataFromServer.text()
    
    chatMsg.innerHTML = data
}

// setInterval(loadChatMsg,1499)

async function loadChatMsgJson(){
    let dataFromServer = await fetch(API + '/read')
    let data = await dataFromServer.json()

    chatMsg.innerHTML = ''

    i=0;
    while(i < await data.length){
        chatMsg.innerHTML = chatMsg.innerHTML + '['+data[i]['laiks'] + '] '+ data[i]['vards'] + ': ' + data[i]['zina'] + '<br/>'
        i+=1;
    }
} 

setInterval(loadChatMsgJson,999)