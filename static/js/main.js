console.log('I am here!')

// Event handler for the index.html button

// Get the element Id for the button and add event listener
document.getElementById('js-clicker').addEventListener('click',()=> {

    // Fetch birthday_list view which returns Birthday data
    fetch('/birthday_list/')
    
    // Then take the returned data and convert to JSON
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(JSON.stringify(data))
    })
})

// TODO:  Create a Model for Birthdays(Date, Name, Greeting)
// TODO:  Make migrations and migrate
// TODO:  Make an http request to the model to get birthday data
// TODO:  Make a view to send back birthday data