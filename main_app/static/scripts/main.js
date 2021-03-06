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

// All my functions I used 
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

// USER PROFILE EVENT LISTENERS

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

if (document.querySelector(".edit-review-button-profile")) {
    const editReviewProfileButtonEl = document.querySelectorAll(".edit-review-button-profile");
    const deleteReviewProfileButtonEl = document.querySelectorAll(".delete-review-button-profile");
    const editReviewFormProfileEl = document.querySelectorAll(".edit-review-form");
    const editReviewCancelEl = document.querySelectorAll(".edit-review-cancel-button");
    const deleteReviewFormProfileEl = document.querySelectorAll(".delete-review-form-container");
    const deleteReviewCancelEl = document.querySelectorAll(".delete-review-cancel-button")

    for (let i = 0; i < editReviewProfileButtonEl.length; i++) {
        editReviewProfileButtonEl[i].addEventListener('click', (e) => {
            showElement(editReviewFormProfileEl[i]);
        });
        editReviewCancelEl[i].addEventListener('click', (e) => {
            hideElement(editReviewFormProfileEl[i])
        });
        deleteReviewProfileButtonEl[i].addEventListener('click', (e) => {
            showElement(deleteReviewFormProfileEl[i]);
        });
        deleteReviewCancelEl[i].addEventListener('click', (e) => {
            hideElement(deleteReviewFormProfileEl[i]);
        })
    }
}

if (document.querySelector(".profile-page-container")) {
    let browserWidth = window.innerWidth;
    const imgEl = document.createElement("img");
    imgEl.classList.add("profile-card-background");
    imgEl.src="https://www.seattlenorthcountry.com/imager/s3_amazonaws_com/snohomish-2018/craft/Main-Images/SeattleNorthCountry_RockClimbing_Header-1920x1080_930104bc5592b0f48aa7a928055610d9.jpg";

    window.addEventListener('load', (e) => {
        browserWidth = window.innerWidth;
        if (browserWidth < 1100) {
            const profilePageEl = document.querySelector(".profile-page-container");
            profilePageEl.append(imgEl);
        }
    });

    window.addEventListener("resize", (e) => {
        browserWidth = window.innerWidth;
        if (browserWidth < 1100) {
            if (!(document.querySelector(".profile-card-background"))) {
                const profilePageEl = document.querySelector(".profile-page-container");
                profilePageEl.append(imgEl);
            } else {
                console.log("Holy jesus. What is that!?! WHAT THE FUCK IS THAT???");
            }
        } else {
            document.querySelector(".profile-page-container").removeChild(document.querySelector(".profile-card-background"));
        }
    })
}

// ROUTE PAGE EVENT LISTENERS

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

if (document.querySelector(".continue-button")) {
    document.querySelector(".continue-button").addEventListener('click', (e) => {
        e.preventDefault();
        hideElement(document.querySelector(".route-form-first-half"));
        showElement(document.querySelector(".second-form-half"));
    })
}

if (document.querySelector(".route-go-back")) {
    document.querySelector(".route-go-back").addEventListener('click', (e) => {
        e.preventDefault();
        hideElement(document.querySelector(".second-form-half"));
        showElement(document.querySelector(".route-form-first-half"));
    })
}

if (document.querySelector(".route-sort-option")) {
    const sortRoutes = (e) => {
        e.preventDefault();
        if (e.target.value !== "default" && window.location.href.includes("?") && !(window.location.href.includes("sort"))) {
            let url = window.location.href.toString();
            window.location.assign(url + "&sort=" + e.target.value);
        } else if (e.target.value !== "default" && window.location.href.includes("sort")) {
            const url = window.location.href.toString();
            const oldUrlPart = url.substring(url.indexOf("sort"), url.length);
            window.location.assign(url.replace(oldUrlPart, "sort=" + e.target.value));
        }
    }
    document.querySelector(".route-results-button").addEventListener("change", (e) => sortRoutes(e));
}