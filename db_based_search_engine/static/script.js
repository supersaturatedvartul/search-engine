let searchbtn = document.getElementById('searchbtn');

searchbtn.addEventListener('click',async function () {
    let query = document.getElementById('searchinput').value;

    let response = await fetch(`/search?q=${query}`);
    let data = await response.json()
    console.log(data);

    let resultdiv = document.querySelector('.resultpage');
    resultdiv.innerHTML = "";

    if (!data.results || data.results.length === 0) {
        resultdiv.innerHTML = `<p>No Results for ${query}</p>`;
        return;
    }
    data.results.forEach(item => {
        let p = document.createElement('p');
        p.innerText = item.content + " (Score: " + item.score + ")";
        resultdiv.appendChild(p);
    });
});