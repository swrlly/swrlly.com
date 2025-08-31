const twitterUrl = "https://twitter.com/intent/tweet/";
const fbUrl = "https://www.facebook.com/sharer.php?u=<url>";
const redditUrl = "https://www.reddit.com/submit?url=<url>&title=<title>";
const linkedinUrl = "https://www.linkedin.com/sharing/share-offsite/?url=<url>";
const linkTarget = "_top";
const windowOptions = "menubar=no,status=no,height=750,width=500";

function extractTitleText() {
    return document.querySelector(".blog-title").innerText;
}

function extractWindowLink() {
    return window.location.href;
}

function openTwitterWindow(text, link) {
    const twitterQuery = `text=${text}&url=${link}`;
    return window.open(`${twitterUrl}?${twitterQuery}&`, linkTarget, windowOptions);
}

function registerShareButton() {
    const text = extractTitleText();
    const link = extractWindowLink();
    const twitterButton = document.querySelector("#button--twitter");
    twitterButton.addEventListener("click", () => openTwitterWindow(text, link));
}


console.log("window ready");
registerShareButton();


