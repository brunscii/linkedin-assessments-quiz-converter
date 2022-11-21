function wrong(e){
    e.target.style('background-color','red')
    console.log('hello')
}

document.querySelectorAll('.wrong-answer').forEach((b)=>
    b.addEventListener('click', (e)=>{
        console.log(e)
        b.classList.toggle('wrong')
    })
)
document.querySelectorAll('.correct-answer').forEach((b)=>
    b.addEventListener('click', (e)=>{
        console.log(e)
        b.classList.toggle('correct')
    })
)
