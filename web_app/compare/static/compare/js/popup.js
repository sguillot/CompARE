function showModelPopup(element, mprim, msec, mdesc, mref_list) {

    let references = mref_list.split(',');
    // Create the HTML content for the pop-up
    let popupContent = `
        <div class="model-popup">
            <p><strong>Primary Dependency:</strong> ${mprim}</p>
            <p><strong>Secondary Dependency:</strong> ${msec}</p>
            <p><strong>Description:</strong> ${mdesc}</p>
            <p><strong>References:</strong></p>
            <ul>
                ${references.map(ref => `<li>${ref}</li>`).join('')}
            </ul>
        </div>
    `;

    // Create the pop-up element
    let popup = document.createElement('div');
    popup.className = 'model-popup-container';
    popup.innerHTML = popupContent;

    // Append pop-up to the body
    document.body.appendChild(popup);

    // Position the pop-up below the hovered element
    positionPopup(element, popup);
}

function positionPopup(element, popup) {
    let rect = element.getBoundingClientRect();
    let scrollTop = window.scrollY || document.documentElement.scrollTop;
    let scrollLeft = window.scrollX || document.documentElement.scrollLeft;

    popup.style.top = rect.bottom + scrollTop + 'px';
    popup.style.left = rect.left + scrollLeft + 'px';
}

function hideModelPopup() {
    // Remove the pop-up element
    let popup = document.querySelector('.model-popup-container');
    if (popup) {
        popup.remove();
    }
}