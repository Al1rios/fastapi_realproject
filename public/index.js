
function load_animals(){
    axios.get('https://al1rios-fastapi-realproject-7v7vr9w4fx94q-8000.githubpreview.dev/docs#/default/list_animals_animals_get').then(response == console.log(response.data))
}


function app() {
    console.log('App Initialized')
    load_animals()
}

app()