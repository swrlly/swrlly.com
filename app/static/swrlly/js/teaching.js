// does not account for zooming out less than 100%
function ModifyIconFont() {

    // get box width first later; better

    let icons = document.querySelectorAll(".center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth > 1200) {
            icons[i].style["font-size"] = "40px";
        }
        else if (window.innerWidth > 800) {
            icons[i].style["font-size"] = "3.8vw";
        }
        else {
            icons[i].style["font-size"] = "5.5vw";
        }
    }

    icons = document.querySelectorAll(".large-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth > 1200) {
            icons[i].style["font-size"] = "60px";
        }
        else if (window.innerWidth > 800) {
            icons[i].style["font-size"] = "6.33vw";
        }
        else {
            icons[i].style["font-size"] = "10vw";
        }
    }

    
    icons = document.querySelectorAll(".small-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth > 1200) {
            icons[i].style["font-size"] = "30px";
        }
        else if (window.innerWidth > 800) {
            icons[i].style["font-size"] = "2.2166vw";
        }
        else {
            icons[i].style["font-size"] = "3.5vw";//"1.7241379310345vw";
        }
    }


    icons = document.querySelectorAll(".vsmall-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth > 1200) {
            icons[i].style["font-size"] = "20px";
        }
        else if (window.innerWidth > 800) {
            icons[i].style["font-size"] = "1.8vw";
        }
        else {
            icons[i].style["font-size"] = "2.4vw";
        }
    }

    icons = document.querySelectorAll(".vvsmall-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth > 1200) {
            icons[i].style["font-size"] = "15px";
        }
        else if (window.innerWidth > 800) {
            icons[i].style["font-size"] = "1.35vw";
        }
        else {
            icons[i].style["font-size"] = "1.8vw";
        }
    }

    icons = document.querySelectorAll(".vvvsmall-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth > 1200) {
            icons[i].style["font-size"] = "11px";
        }
        else if (window.innerWidth > 800) {
            icons[i].style["font-size"] = "1vw";
        }
        else {
            icons[i].style["font-size"] = "1.7vw";
        }
    }
    icons = document.querySelectorAll(".center-text-over-image, .large-center-text-over-image, .small-center-text-over-image, .vsmall-center-text-over-image, .vvsmall-center-text-over-image, .vvvsmall-center-text-over-image");
    for (let i = 0; i< icons.length; i++) {
        let boxHeight = icons[i].offsetHeight;
        let boxWidth = icons[i].offsetWidth;
        let backgroundBoxHeight = icons[i].previousElementSibling.offsetHeight;
        let backgroundBoxWidth = icons[i].previousElementSibling.offsetWidth;
        icons[i].style.top = ((backgroundBoxHeight - boxHeight) / 2) + "px";
        icons[i].style.left = ((backgroundBoxWidth - boxWidth) / 2) + "px";
    }

}

function ShowSolution(event) {
    if (event.target.nextElementSibling.style.display != "block") {
        event.target.nextElementSibling.style.display = "block";
        event.target.innerHTML = "Hide Solution";
    }
    else {
        event.target.nextElementSibling.style.display = "none";
        event.target.innerHTML = "Show Solution";
    }
}

window.onresize = ModifyIconFont;
window.onload = () => {
    ModifyIconFont();
    let btns = document.querySelectorAll(".math-btn");
    for (let i = 0; i < btns.length; i++){
        btns[i].onclick = (event) => {ShowSolution(event)};
    }
}





