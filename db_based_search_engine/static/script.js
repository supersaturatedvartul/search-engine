let search = document.getElementById('searchbtn');

search.addEventListener('click',async function () {
    let query = document.getElementById('searchinput').value;

    let response = await fetch(`/search?q=${query}`);
    let data = await response.json()
    console.log(data);
})