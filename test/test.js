function togglePreview1() {
  var preview = document.getElementById("preview1");
  preview.style.visibility =
    preview.style.visibility === "hidden" ? "visible" : "hidden";
  preview.style.opacity = preview.style.opacity === "0" ? "1" : "0";
}

function closePreview1() {
  var preview = document.getElementById("preview1");
  preview.style.visibility = "hidden";
  preview.style.opacity = "0";
}

function togglePreview2() {
  var preview = document.getElementById("preview2");
  preview.style.visibility =
    preview.style.visibility === "hidden" ? "visible" : "hidden";
  preview.style.opacity = preview.style.opacity === "0" ? "1" : "0";
}

function closePreview2() {
  var preview = document.getElementById("preview2");
  preview.style.visibility = "hidden";
  preview.style.opacity = "0";
}
