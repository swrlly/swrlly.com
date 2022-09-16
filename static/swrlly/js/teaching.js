// does not account for zooming out less than 100%
function ModifyIconFont() {
    let icons = document.querySelectorAll(".center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth >= 1200) {
            icons[i].style["font-size"] = "40px";
        }
        else {
            icons[i].style["font-size"] = "3.448275862069vw";
        }
    }
    icons = document.querySelectorAll(".center-text-over-image");
    for (let i = 0; i< icons.length; i++) {
        let boxHeight = icons[i].offsetHeight;
        let boxWidth = icons[i].offsetWidth;
        let backgroundBoxHeight = icons[i].previousElementSibling.offsetHeight;
        let backgroundBoxWidth = icons[i].previousElementSibling.offsetWidth;
        icons[i].style.top = ((backgroundBoxHeight - boxHeight) / 2) + "px";
        icons[i].style.left = ((backgroundBoxWidth - boxWidth) / 2) + "px";
    }

    icons = document.querySelectorAll(".large-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth >= 1200) {
            icons[i].style["font-size"] = "80px";
        }
        else {
            icons[i].style["font-size"] = "6.896551724138vw";
        }
    }
    icons = document.querySelectorAll(".large-center-text-over-image");
    for (let i = 0; i< icons.length; i++) {
        let boxHeight = icons[i].offsetHeight;
        let boxWidth = icons[i].offsetWidth;
        let backgroundBoxHeight = icons[i].previousElementSibling.offsetHeight;
        let backgroundBoxWidth = icons[i].previousElementSibling.offsetWidth;
        icons[i].style.top = ((backgroundBoxHeight - boxHeight) / 2) + "px";
        icons[i].style.left = ((backgroundBoxWidth - boxWidth) / 2) + "px";
    }
    
    icons = document.querySelectorAll(".small-center-text-over-image");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth >= 1200) {
            icons[i].style["font-size"] = "20px";
        }
        else {
            icons[i].style["font-size"] = "1.7241379310345vw";
        }
    }
    icons = document.querySelectorAll(".small-center-text-over-image");
    for (let i = 0; i< icons.length; i++) {
        let boxHeight = icons[i].offsetHeight;
        let boxWidth = icons[i].offsetWidth;
        let backgroundBoxHeight = icons[i].previousElementSibling.offsetHeight;
        let backgroundBoxWidth = icons[i].previousElementSibling.offsetWidth;
        icons[i].style.top = ((backgroundBoxHeight - boxHeight) / 2) + "px";
        icons[i].style.left = ((backgroundBoxWidth - boxWidth) / 2) + "px";
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



