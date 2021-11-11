let userRouteEl = document.querySelector(".user_routes");
let userReviewEl = document.querySelector(".user_reviews");
const userReviewButtonEl = document.querySelector(".user_reviews_button");
const userRouteButtonEl = document.querySelector(".user_routes_button");

userRouteButtonEl.addEventListener("click", (e) => {
    e.preventDefault();
    userReviewEl.classList.remove("show");
    userReviewEl.classList.add("no-show");
    userRouteEl.classList.remove("no-show");
    userRouteEl.classList.add("show");
});

userReviewButtonEl.addEventListener("click", (e) => {
    e.preventDefault();
    userRouteEl.classList.remove("show");
    userRouteEl.classList.add("no-show");
    userReviewEl.classList.remove("no-show");
    userReviewEl.classList.add("show");
});