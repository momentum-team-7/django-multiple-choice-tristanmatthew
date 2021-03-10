deleteSnippet = document.querySelectorAll('.delete-snippet')
saveSnippet = document.querySelectorAll('.save-snippet')

for (let button of deleteSnippet){
    deleteSnippet = document.querySelectorAll('.delete-snippet')
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

for (let button of saveSnippet) {
    saveSnippet = document.querySelectorAll('.save-snippet')
    button.addEventListener('click', event => {
        const snippetElement = event.target.parentElement.parentElement
        const saveUrl = event.target.dataset.url
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

function renderSnippet(data) {
    // lots of fucking code 

    
    Prism.highlightElement(preTag)
    Prism.highlightElement(codeTag)

    deleteSnippet()
    saveSnippet()

}

deleteSnippet()
saveSnippet()

<div class="snip-container">
  {% for snippet in snippets %}
  <div>
      <div class="save-button"> 
        <button class="save-snippet" id="{{snippet.pk}}">SAVE SNIPPET</button>
      </div>
    <div class="terminal-timeline">
      <div class="terminal-card">
        <header>{{snippet.title}}</header>
        <p class="terminal-alert terminal-alert-primary">{{snippet.language}}</p>
        <p>Uploaded by: {{snippet.user}}</p>
        <pre><code class="language-{{snippet.language}}">{{snippet.code}}</code></pre>
      </div>
    </div>
  </div>
  {% endfor %}
</div>