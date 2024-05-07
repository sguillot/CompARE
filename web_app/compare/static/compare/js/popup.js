function showPopup(element, popupClass, prim, sec, desc, ref_list, primLabel, secLabel) {
    let references = ref_list.split(',');

    // Determine which labels to display based on attribute names
    let primLabelText = primLabel === "mprim" ? "Primary Dependency" : "Primary Assumption";
    let secLabelText = secLabel === "msec" ? "Secondary Dependency" : "Secondary Assumption";

    // Create the HTML content for the pop-up
    let popupContent = `
        <div class="${popupClass}">
            <p><strong>${primLabelText}:</strong> ${prim}</p>
            <p><strong>${secLabelText}:</strong> ${sec}</p>
            <p><strong>Description:</strong> ${desc}</p>
            <p><strong>References:</strong></p>
            <ul>
                ${references.map(ref => `<li>${ref}</li>`).join('')}
            </ul>
        </div>
    `;

    // Create the pop-up element
    let popup = document.createElement('div');
    popup.className = `${popupClass}-container`;
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

function hidePopup(className) {
    // Remove the pop-up element
    let popup = document.querySelector('.' + className);
    if (popup) {
        popup.remove();
    }
}
