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
    console.log(similarity)
    console.log("Similarity:", similarity.toFixed(2) + "%");
    texto.value=""
});


function compareTextsLetterByLetter(text1, text2) {
    // Check if texts have same length
    text1 = text1.toUpperCase();
    text2 = text2.toUpperCase();
    // Calculate the number of matching characters
    let matchingCount = 0;
    for (let i = 0; i < text1.length; i++) {
        if (text1[i] === text2[i]) {
            matchingCount++;
        }
    }

    // Calculate percentage of similarity
    const similarityPercentage = (matchingCount / text1.length) * 100;

    return similarityPercentage;
}