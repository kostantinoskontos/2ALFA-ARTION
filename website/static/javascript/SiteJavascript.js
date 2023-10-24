function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function hideOrShowImages(category) {
  // Get all images with class "Product_images"
  const images = document.querySelectorAll(".Product_images");

  // Loop through all images and hide/show them based on the category
  images.forEach((image) => {
    const imageCategory = image.id;

    if (category === "all" || category === imageCategory) {
      image.style.display = "block"; // Show images in the selected category or 'all'
    } else {
      image.style.display = "none"; // Hide images in other categories
    }
  });
  AOS.refresh();
}

function googleTranslateElementInit() {
  new google.translate.TranslateElement(
    {
      pageLanguage: "el", // Set the default display language to English
      autoDisplay: false, // We'll manually trigger the translation
      includedLanguages: "el,fr,en,bg,it,de",
    },
    "google_translate_element"
  );
}

function removeFromCart(itemId) {
  var url = "/removeFromCart/" + itemId;
  window.location.href = url;
}
