async function rankResumes(){

let jobDesc = document.getElementById("jobDesc").value
let files = document.getElementById("resumes").files

let formData = new FormData()

formData.append("job_description", jobDesc)

for(let file of files){
formData.append("resumes", file)
}

let response = await fetch("http://127.0.0.1:8000/rank",{
method:"POST",
body:formData
})

let data = await response.json()

console.log(data)   // ⭐ important for debugging

let results = document.getElementById("results")

results.innerHTML = ""

data.forEach((candidate,index)=>{

let card = document.createElement("div")
card.className = "result-card"

card.innerHTML = `
<h3>Rank #${index+1}</h3>
<p><b>Name:</b> ${candidate.name}</p>
<p><b>Match Score:</b> ${candidate.score}</p>
`

results.appendChild(card)

})

}