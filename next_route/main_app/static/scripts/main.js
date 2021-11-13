let userRouteEl = document.querySelector(".user_routes");
let userReviewEl = document.querySelector(".user_reviews");
const userReviewButtonEl = document.querySelector(".user_reviews_button");
const userRouteButtonEl = document.querySelector(".user_routes_button");
const writeReviewButtonEl = document.querySelector(".write-review-button");
const editReviewButtonEl = document.querySelector('.edit-review-button');
const deleteReviewButtonEl = document.querySelector(".delete-review-button");
const deleteReviewCancelButtonEl = document.querySelector(".delete-review-cancel-button");
const editReviewCancelButtonEl = document.querySelector(".edit-review-cancel-button");
const editProfileButtonEl = document.querySelector(".edit_profile_button");
const editProfileCancelButtonEl = document.querySelector(".edit_profile_cancel_button");

const showElement = (domEl) => {
    domEl.classList.add('show');
    domEl.classList.remove("no-show");
}

const hideElement = (domEl) => {
    domEl.classList.remove('show');
    domEl.classList.add("no-show");
}

if (userRouteButtonEl) {
    userRouteButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        hideElement(userReviewEl);
        showElement(userRouteEl);
        hideElement(document.querySelector(".user_reviews_header"));
        showElement(document.querySelector(".user_routes_header"));
    });
}

if (userReviewButtonEl) {
    userReviewButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        hideElement(userRouteEl);
        showElement(userReviewEl);
        hideElement(document.querySelector(".user_routes_header"));
        showElement(document.querySelector(".user_reviews_header"));
    });
}

if (writeReviewButtonEl) {
    writeReviewButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        const routeReviewContainEL = document.querySelector(".route-review-form-container");
        showElement(routeReviewContainEL);
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