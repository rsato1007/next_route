let userRouteEl = document.querySelector(".user_routes");
let userReviewEl = document.querySelector(".user_reviews");
const userReviewButtonEl = document.querySelector(".user_reviews_button");
const userRouteButtonEl = document.querySelector(".user_routes_button");
const writeReviewButtonEl = document.querySelector(".write-review-button");
const writeReviewCancelButtonEl = document.querySelector(".write_review_cancel_button");
const editReviewButtonEl = document.querySelector('.edit-review-button');
const deleteReviewButtonEl = document.querySelector(".delete-review-button");
const deleteReviewCancelButtonEl = document.querySelector(".delete-review-cancel-button");
const editReviewCancelButtonEl = document.querySelector(".edit-review-cancel-button");
const editProfileButtonEl = document.querySelector(".edit_profile_button");
const editProfileCancelButtonEl = document.querySelector(".edit_profile_cancel_button");
const passwordInputEl = document.querySelector(".password-required");

const showElement = (domEl) => {
    domEl.classList.add('show');
    domEl.classList.remove("no-show");
}

const hideElement = (domEl) => {
    domEl.classList.remove('show');
    domEl.classList.add("no-show");
}

const greenButton = (domEl) => {
    domEl.classList.remove("profile-slider-white-option");
    domEl.classList.add("profile-slider-green-option");
}

const whiteButton = (domEl) => {
    domEl.classList.add("profile-slider-white-option");
    domEl.classList.remove("profile-slider-green-option");
}

const passWordValidation = (field1, field2) => {
    if (field1.value !== '') {
        field1.setAttribute('required', '');
        field2.setAttribute('required', '')
        if (field1.value !== field2.value) {
            const passwordMessageEl = document.querySelector(".password-message");
            showElement(passwordMessageEl);
        }
        else {
            const passwordMessageEl = document.querySelector(".password-message");
            hideElement(passwordMessageEl);
        }
    } else {
        field1.removeAttribute('required');
        field2.removeAttribute('required')
    }
}

if (userRouteButtonEl) {
    userRouteButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        hideElement(userReviewEl);
        showElement(userRouteEl);
        hideElement(document.querySelector(".user_reviews_header"));
        showElement(document.querySelector(".user_routes_header"));
        greenButton(document.querySelector(".user_routes_button"));
        whiteButton(document.querySelector(".user_reviews_button"));
    });
}

if (userReviewButtonEl) {
    userReviewButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        hideElement(userRouteEl);
        showElement(userReviewEl);
        hideElement(document.querySelector(".user_routes_header"));
        showElement(document.querySelector(".user_reviews_header"));
        greenButton(document.querySelector(".user_reviews_button"));
        whiteButton(document.querySelector(".user_routes_button"));
    });
}

if (writeReviewButtonEl) {
    writeReviewButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        const routeReviewContainEL = document.querySelector(".route-review-form-container");
        showElement(routeReviewContainEL);
    });
}

if(writeReviewCancelButtonEl) {
    writeReviewCancelButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        const routeReviewContainEL = document.querySelector(".route-review-form-container");
        hideElement(routeReviewContainEL);
    });
}

if (editReviewButtonEl) {
    editReviewButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        const editReviewFormEl = document.querySelector(".edit-review-form");
        showElement(editReviewFormEl);
    })
}

if (editReviewCancelButtonEl) {
    editReviewCancelButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        const editReviewFormEl = document.querySelector(".edit-review-form");
        hideElement(editReviewFormEl);
    })
}

if (deleteReviewButtonEl) {
    deleteReviewButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        const deleteReviewFormEl = document.querySelector(".delete-review-form-container");
        showElement(deleteReviewFormEl);
    })
}

if (deleteReviewCancelButtonEl) {
    deleteReviewCancelButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        const deleteReviewFormEl = document.querySelector(".delete-review-form-container");
        hideElement(deleteReviewFormEl);
    })
}

if (editProfileButtonEl) {
    editProfileButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        showElement(document.querySelector(".edit_profile_container"));
    })
}

if(editProfileCancelButtonEl) {
    editProfileCancelButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        hideElement(document.querySelector(".edit_profile_container"));
    })
}

if (passwordInputEl) {
    const passwordInputEl2 = document.getElementById("password_reenter");
    passwordInputEl.addEventListener('input', (e) => {
        e.preventDefault();
        passWordValidation(passwordInputEl, passwordInputEl2);
    })
    passwordInputEl2.addEventListener('input', (e) => {
        e.preventDefault();
        passWordValidation(passwordInputEl2, passwordInputEl);
    })
}