async function load_animals(){
    const response = await axios.get('http://localhost:8000/animals')
        
    const animals = response.data
        
    const list_one = document.getElementById("list_animals")

    animals.forEach(animal => {
        const item = document.createElement('li')
        item.innerText = animal.name

        list_one.appendChild(item)
    });

    
}


function app() {
    console.log('App Initialized')
    load_animals()
}

app()