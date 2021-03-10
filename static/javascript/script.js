deleteSnippet = document.querySelectorAll('.delete-snippet')

for (let button of deleteSnippet){
    button.addEventListener('click', event => {
        const snippetElement = event.target.parentElement.parentElement
        console.log(event.target.parentElement)
        const deleteUrl = `/snippets/${event.target.id}/delete`
        fetch (deleteUrl, {
            headers: {
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest', 
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            snippetElement.remove()
        })
    })
}