deleteSnippet = document.querySelectorAll('.delete-snippet')
saveSnippet = document.querySelectorAll('.save-snippet')

function deleteSnippetFunction(){
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
}

function saveSnippetFunction(){
    saveSnippet = document.querySelectorAll('.save-snippet')
    for (let button of saveSnippet) {
        button.addEventListener('click', event => {
            const snippetElement = event.target.parentElement.parentElement
            const saveUrl = `/snippet/${event.target.id}/save`
            fetch (saveUrl, {
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                console.log(data['code'])
                renderSnippet(data)
            })
        })
    }
}

function renderSnippet(data) {
    
    let snipContainer = document.querySelector('.snip-container')
        snipContainer.className = 'snip-container'

    let div = document.createElement('div')
        div.className = "one-snip"

    let saveButtonDiv = document.createElement('div')
        saveButtonDiv.className = 'save-button'

    let saveButton = document.createElement('button')
        saveButton.className = 'save-snippet'
        saveButton.id = `${data['pk']}`
        saveButton.innerHTML = "SAVE SNIPPET"
        console.log(saveButton)

    let editDeleteButtonDiv = document.createElement('div')
        editDeleteButtonDiv.className = "edit-delete-button"

    // let delButton = document.createElement('button')
    //     delButton.className = 'delete-snippet'
    //     delButton.id = `${data['pk']}`
    //     delButton.innerHTML = "DELETE SNIPPET"
    //     console.log(delButton)

    // let editButton = document.createElement('button')
    //     editButton.className = 'edit-snippet'
    //     editButton.id = `${data['pk']}`
    //     editButton.innerHTML = "EDIT SNIPPET"

    let termTimelineDiv = document.createElement('div')
        termTimelineDiv.className ="terminal-timeline"

    let termCardDiv = document.createElement('div')
        termCardDiv.className = "terminal-card"
    
    let snipTitle = document.createElement('header')
        snipTitle.innerHTML = `${data['title']}`

    let snipLang = document.createElement('p')
        snipLang.className = "terminal-alert terminal-alert-primary"
        snipLang.innerHTML = `${data['language']}`

    let uploadP = document.createElement('p')
        uploadP.innerHTML = `${data['user']}`

    let preTag = document.createElement('pre')

    let codeTag = document.createElement('code')
        codeTag.className = `language-${data['language']}`
        codeTag.innerHTML = `${data['code']}`
    
    Prism.highlightElement(preTag)
    Prism.highlightElement(codeTag)

    // editDeleteButtonDiv.appendChild(editButton)
    // editDeleteButtonDiv.appendChild(delButton)
    saveButtonDiv.appendChild(saveButton)
    
    preTag.appendChild(codeTag)

    termCardDiv.appendChild(snipTitle)
    termCardDiv.appendChild(snipLang)
    termCardDiv.appendChild(uploadP)
    termCardDiv.appendChild(preTag)

    termTimelineDiv.appendChild(termCardDiv)

    div.appendChild(saveButtonDiv)
    // div.appendChild(editDeleteButtonDiv)
    div.appendChild(termTimelineDiv)

    snipContainer.appendChild(div)




    deleteSnippetFunction()
    saveSnippetFunction()

}

deleteSnippetFunction()
saveSnippetFunction()