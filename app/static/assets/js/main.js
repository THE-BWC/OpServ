const navigationBackdrop = document.createElement('div');
navigationBackdrop.classList.add('fixed', 'inset-0', 'bg-black', 'bg-opacity-50', 'z-10');

// JQuery toggle navigation drawer
$(document).ready(function() {
    $('#drawer-navigation-toggle').click(function() {
        $('#drawer-navigation').toggleClass('transform-none');
        $('body').append(navigationBackdrop);
    });

    let drawerNavigation = $('#drawer-navigation');
    // If you click the backdrop, close the drawer
    $(navigationBackdrop).click(function() {
        drawerNavigation.toggleClass('transform-none');
        navigationBackdrop.remove();
        // if drawer doesn't have -translate-x-full then add it
        if (!drawerNavigation.hasClass('-translate-x-full')) {
            drawerNavigation.addClass('-translate-x-full');
        }
    });

    let searchModal = $('#search-modal');
    // JQuery toggle search modal
    $('#search-modal-toggle').click(function() {
        searchModal.toggleClass('hidden');
        searchModal.toggleClass('flex');
    });

    // If you click anything outside the first child of the search modal, close the search modal
    searchModal.click(function(event) {
        if (event.target === this) {
            searchModal.toggleClass('hidden');
            searchModal.toggleClass('flex');
        }
    });
});

function copyToClipboard(text) {
    try {
        navigator.clipboard.writeText(text).then(() => {
            console.log('Copied to clipboard: ', text);
        });
    } catch (err) {
        console.error('Failed to copy: ', err);
    }
}

function toggleAttending(id){
    //show the member attendance
    let attending = $('#attending'+id);
    let viewAttending = $('#viewAttending'+id);

    // if attending has class 'hidden' then remove it
    if(attending.hasClass('show')) {
        attending.removeClass('show');
        attending.addClass('hidden');
        viewAttending.text("View Member Attendance");
    } else {
        attending.removeClass('hidden');
        attending.addClass('show');
        viewAttending.text("Hide Member Attendance");
    }
}

function attend(operation_id, status, leader_id){
    let note;
    if(status === 1) { note = "attending" }
    if(status === 2) { note = "maybe attending" }
    if(status === 3) { note = "not attending" }
    let result = confirm("Do you wish to RSVP as " + note + "?");
    if(result){
        $.post("/opserv/ajaxLibrary.php",{
            "attendance": status,
            "operation_id": operation_id,
            "leader_id": leader_id
        });
    }
}

function openTab(ev, tabName) {
    // if tab is already active, close it
    if (!document.getElementById(tabName).className.includes('hidden')) {
        document.getElementById(tabName).classList.add('hidden');
        ev.className = ev.className.replace(' bg-dark', '');
        return;
    }

    let tabButtonsWrapper = document.querySelectorAll('[data-tabs-wrapper="true"]');
    tabButtonsWrapper.forEach(function (tabButtonWrapper) {
        // Get all buttons under the wrapper
        let tabButtons = tabButtonWrapper.getElementsByTagName('button');
        for (let i = 0; i < tabButtons.length; i++) {
            tabButtons[i].className = tabButtons[i].className.replace(' bg-dark', '');
        }
    })

    let tabContentsWrapper = document.querySelectorAll('[data-tabs-contents-wrapper="true"]');
    tabContentsWrapper.forEach(function (tabContent) {
        // Get all tab contents under the wrapper
        let tabContents = tabContent.children;
        for (let i = 0; i < tabContents.length; i++) {
            tabContents[i].classList.add('hidden');
        }
    })

    document.getElementById(tabName).classList.remove('hidden');
    ev.className += ' bg-dark';
}
