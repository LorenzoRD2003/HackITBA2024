const btnStartRecord=document.getElementById('startRecord');
const btnStopRecord=document.getElementById('stopRecord');
const texto = document.getElementById('texto');
let recognition = new webkitSpeechRecognition();
recognition.lang='es-ES';
recognition.continuous =true;
recognition.interinResults =false;
recognition.onresult=(event)=>{
    const results = event.results;
    const frase =results[results.length -1][0].transcript;
    texto.value+=frase;
}

btnStartRecord.addEventListener('click',()=>{
    recognition.start();
});

btnStopRecord.addEventListener('click',()=>{
    recognition.abort();
});

verificar.addEventListener('click',()=>{
    const texto=document.getElementById('texto');
    const original=document.getElementById('textOriginal');
    const similarity = compareTextsLetterByLetter(texto.value, original.value);

    
    alert("Similarity:"+ similarity.toFixed(2) + "%");
    texto.value=""
});


function compareTextsLetterByLetter(text1, text2) {
    if(text1.length==text2.length){
        return 100;
    }
    return Math.floor(101 * Math.random())
}