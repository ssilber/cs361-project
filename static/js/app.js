
/* Get relevant assets*/
const cards = document.getElementsByClassName("club-card")
const dropdown = document.getElementById("club");
const goButton = document.getElementById("selectClub");

/* Determine if a club has already been selected based on highlighting */
function clubAlreadySelected(cards) {
    for (const card of cards) {
        if (card.classList.contains('highlight')) {
            return true
        }
    }
    return false
}

/* Remove all current card highlighting */
function removeHighlighting(cards) {
    for (const card of cards) {
        if (card.classList.contains('highlight')) {
            card.classList.remove('highlight');
        }
    }
}


/* Highlight/unhighlight cards when clicked, and set the dropdown to the correct value */
for (const card of cards) {
    card.addEventListener('click', (event) => {

        /* remove all highlighting*/
        removeHighlighting(cards)

        /* add highlighting */
        card.classList.add('highlight')

        /* Set the dropdown value to the selected card */
        dropdown.value = card.id
    });
}

/* Highlight/unhighlight cards when using dropdown */
dropdown.addEventListener('change', (event) => {
    dropdown_value = dropdown.value

    /* remove all highlighting*/
    removeHighlighting(cards)

    /* highlight card based on dropdown selection */
    for (const card of cards) {
        if (card.id === dropdown_value) {
            card.classList.add('highlight');
        }
    }
});
