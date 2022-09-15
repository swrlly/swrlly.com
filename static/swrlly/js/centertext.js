// does not account for zooming out less than 100%
function ModifyIconFont() {
    let icons = document.querySelectorAll(".centertextoverimage");
    for (let i = 0; i < icons.length; i++) {
        if (window.innerWidth >= 1200) {
            icons[i].style["font-size"] = "40px";
        }
        else {
            icons[i].style["font-size"] = "3.448275862069vw";
        }
    }
    icons = document.querySelectorAll(".centertextoverimage");
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
window.onload = ModifyIconFont;