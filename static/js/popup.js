const openTagButtons = document.querySelectorAll('[data-tag-target]')
const closeTagButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')


openTagButtons.forEach(button => {
    button.addEventListener('click', () => {
        const tag = document.querySelector(button.dataset.tagTarget)
        openTag(tag)
        
       
    })
})

closeTagButtons.forEach(button => {
    button.addEventListener('click', () => {
        const tag = button.closest('.tag')
        closeTag(tag)
        document.documentElement.style.overflow = 'scroll';
        document.body.scroll = "yes";
    })
})

function openTag(tag){
    if(tag == null) return
    tag.classList.add('active')
    overlay.classList.add('active')
}
function closeTag(tag){
    if(tag == null) return
    tag.classList.remove('active')
    overlay.classList.remove('active')
}