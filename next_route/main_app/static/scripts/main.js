let userRouteEl = document.querySelector(".user_routes");
let userReviewEl = document.querySelector(".user_reviews");
const userReviewButtonEl = document.querySelector(".user_reviews_button");
const userRouteButtonEl = document.querySelector(".user_routes_button");
const writeReviewButtonEl = document.querySelector(".write-review-button");
const editReviewButtonEl = document.querySelector('.edit-review-button');
const deleteReviewButtonEl = document.querySelector(".delete-review-button");
const deleteReviwCancelButtonEl = document.querySelector(".delete-review-cancel-button");

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
    });
}

if (userReviewButtonEl) {
    userReviewButtonEl.addEventListener("click", (e) => {
        e.preventDefault();
        hideElement(userRouteEl);
        showElement(userReviewEl);
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

if (deleteReviewButtonEl) {
    deleteReviewButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        const deleteReviewFormEl = document.querySelector(".delete-review-form-container");
        showElement(deleteReviewFormEl);
    })
}

if (deleteReviwCancelButtonEl) {
    deleteReviwCancelButtonEl.addEventListener('click', (e) => {
        e.preventDefault();
        console.log("Testing")
        const deleteReviewFormEl = document.querySelector(".delete-review-form-container");
        hideElement(deleteReviewFormEl);
    })
}