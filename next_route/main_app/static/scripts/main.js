let userRouteEl = document.querySelector(".user_routes");
let userReviewEl = document.querySelector(".user_reviews");
const userReviewButtonEl = document.querySelector(".user_reviews_button");
const userRouteButtonEl = document.querySelector(".user_routes_button");
const writeReviewButtonEl = document.querySelector(".write-review-button");

const showElement = (domEl) => {
    domEl.classList.add('show');
    domEl.classList.remove("no-show");
}

const hideElement = (domEl) => {
    domEl.classList.add('show');
    domEl.classList.remove("no-show");
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