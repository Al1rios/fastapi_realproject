async function load_animals(){
    const response = await axios.get('http://localhost:8000/animals')
        
    const animals = response.data

         
    const list_one = document.getElementById("list_animals")

    list_one.innerHTML = ''

    animals.forEach(animal => {
        const item = document.createElement('li')
        item.innerText = animal.name

        list_one.appendChild(item)
    });

    
}

function management_form(){
    const form_animal = document.getElementById('list_animals')

    const input_name = document.getElementById('name')

    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const name_animal = input_name.value
        await axios.post('http://localhost:8000/animals', {
            name: name_animal,
            age: 12,
            sex: 'female',
            color: 'brown'
        })
        load_animals()
        alert('Animal added success')
    }

}


function app() {
    console.log('App Initialized')
    load_animals()
    management_form()
}

app()