// Handling Edit Button
editBtn = document.querySelector("#editBtn");
editBtn.addEventListener('click', function () {
    if (editBtn.textContent === "Edit Table") {
        editBtn.textContent = "Cancel Edit";
        toggleEdit();
    } else {
        editBtn.textContent = "Edit Table";
        openedForUpdate.forEach(function (formNo) {
            toggleUpdate(formNo);
        });
        toggleEdit();
        openedForUpdate = [];
    }
});

// Handling Update Button
let openedForUpdate = [];
updateBtns = document.querySelectorAll("#updateBtn");
updateBtns.forEach(function (updateBtn) {
    updateBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const formNo = filterFormNo(event.target.classList);
        openedForUpdate.push(formNo);
        toggleUpdate(formNo);
    })
})

// Handling Cancel Button
cancelBtns = document.querySelectorAll("#cancelBtn");
cancelBtns.forEach(function (cancelBtn) {
    cancelBtn.addEventListener('click', function (event) {
        event.preventDefault();
        const formNo = filterFormNo(event.target.classList);
        openedForUpdate = openedForUpdate.filter(function (value) {
            return !(value === formNo);
        })
        toggleUpdate(formNo);
    })
})



// ----- Helping Functions Below -----
function filterFormNo(stringArray) {
    stringArray = Array.from(stringArray);
    let filteredStrings = [];
    for (const str of stringArray) {
        let isReqStr = true;
        if (str.length === 0 || str[0] !== "f") {
            isReqStr = false;
        } else {
            for (let i = 1; i < str.length; i++) {
                if (str.charCodeAt(i) < 48 || str.charCodeAt(i) > 57) {
                    isReqStr = false;
                    break;
                }
            }
        }
        if (isReqStr) {
            filteredStrings.push(str);
        }
    }
    return filteredStrings[0];
}

function toggleUpdate(formNo) {
    document.querySelectorAll(`.${formNo}`).forEach(function (element) {
        class_list = element.classList;
        if (class_list.contains("d-none")) {
            class_list.remove("d-none");
        } else {
            class_list.add("d-none");
        }
    });
}

function toggleEdit() {
    document.querySelectorAll(".edit-options").forEach(function (element) {
        class_list = element.classList;
        if (class_list.contains("d-none")) {
            class_list.remove("d-none");
        } else {
            class_list.add("d-none");
        }
    });
}
