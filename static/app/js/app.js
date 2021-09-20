window.addEventListener('scroll', ()=>{
    let navbar = document.getElementById("navbarr")
    navbar.classList.toggle("sticky", window.scrollY>0)
})

let ui = document.querySelector('.ui-container')
let marketing = document.querySelector('.marketing-container')
let ecommerce = document.querySelector('.ecommerce-container')
let copyright = document.querySelector('.copyright-container')
let heci = document.querySelector('.heci')
window.addEventListener('scroll', ()=>{
    ui.classList.toggle('animation', window.scrollY>100)
    marketing.classList.toggle('animation', window.scrollY>100)
    ecommerce.classList.toggle('animation', window.scrollY>100)
    copyright.classList.toggle('animation', window.scrollY>100)
})


let hamburgerIcon = document.querySelector('.logo-symbol svg')
let menu = document.querySelector('.hamburger')

// hamburgerIcon.addEventListener('click', ()=>{
//     menu.style.display='block'
// })

// hamburgerIcon.addEventListener('click,' (=>{
//     menu.classList.toggle('open')
// }))

let menuStatus = true

hamburgerIcon.addEventListener('click', ()=>{
    if(menuStatus){
        menu.style.display = 'block'
        menuStatus=false
    }else{menu.style.display = 'none'
            menuStatus = true}
})
