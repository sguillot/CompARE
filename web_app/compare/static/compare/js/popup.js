/**
 * Displays a pop-up with provided content below the specified element.
 * The pop-up includes primary and secondary labels, descriptions, and references.
 *
 * @param {HTMLElement} element - The element to position the pop-up relative to.
 * @param {string} popupClass - The class name for the pop-up.
 * @param {string} prim - The primary dependency or assumption.
 * @param {string} sec - The secondary dependency or assumption.
 * @param {string} desc - The description text.
 * @param {string} ref_list - A comma-separated list of references.
 * @param {string} primLabel - The label for the primary item (either "mprim" or another value).
 * @param {string} secLabel - The label for the secondary item (either "msec" or another value).
 */
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

/**
 * Positions the pop-up element below the specified element.
 * Adjusts the position based on the element's bounding rectangle and scroll position.
 *
 * @param {HTMLElement} element - The element to position the pop-up relative to.
 * @param {HTMLElement} popup - The pop-up element to be positioned.
 */
function positionPopup(element, popup) {
    let rect = element.getBoundingClientRect();
    let scrollTop = window.scrollY || document.documentElement.scrollTop;
    let scrollLeft = window.scrollX || document.documentElement.scrollLeft;

    popup.style.top = rect.bottom + scrollTop + 'px';
    popup.style.left = rect.left + scrollLeft + 'px';
}

/**
 * Hides and removes the pop-up element with the specified class name.
 *
 * @param {string} className - The class name of the pop-up to be removed.
 */
function hidePopup(className) {
    // Remove the pop-up element
    let popup = document.querySelector('.' + className);
    if (popup) {
        popup.remove();
    }
}
