const addButton = document.getElementById('add-friend') // show form
const add = document.getElementById('add') // submit form
const addForm = document.getElementById('add-form')
const friends = document.getElementById('friends')

// view post
const post = document.getElementById('post')
const modal = document.getElementById('modal')
const image = document.getElementById('image')

window.addEventListener('load',() => {
    console.log('loaded');
    addButton.addEventListener('click', () => {
        addForm.style.display = 'flex'
        addButton.style.display = 'none'
        friends.style.display = 'none'
    })

    add.addEventListener('click', () => {
        friends.style.display = 'flex'
    })

    post.addEventListener('click', () => {
        alert(image.src)
        // modal.style.display = 'flex'
    })
})
