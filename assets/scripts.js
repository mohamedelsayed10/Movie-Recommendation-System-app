// assets/scripts.js

// JavaScript function to handle image click event and toggle zoom effect
function toggleZoom(image) {
    if (image.classList.contains("zoom-in")) {
        image.classList.remove("zoom-in");
        image.classList.add("zoom-out");
    } else {
        var allImages = document.getElementsByClassName("movie-image");
        for (var i = 0; i < allImages.length; i++) {
            allImages[i].classList.remove("zoom-in");
            allImages[i].classList.add("zoom-out");
        }
        image.classList.remove("zoom-out");
        image.classList.add("zoom-in");
    }
}
