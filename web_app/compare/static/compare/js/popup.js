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

    // Position the pop-up below the hovered element
    let rect = element.getBoundingClientRect();
    popup.style.top = rect.bottom + 'px';
    popup.style.left = rect.left + 'px';

    // Append pop-up to the body
    document.body.appendChild(popup);
}

function hideModelPopup() {
    // Remove the pop-up element
    let popup = document.querySelector('.model-popup-container');
    if (popup) {
        popup.remove();
    }
}