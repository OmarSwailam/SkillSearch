document.addEventListener('DOMContentLoaded', function () {
    // let searchForm = document.getElementById('searchForm')
    // let pageLinks = document.getElementsByClassName('page-link')

    // if (searchForm) {
    //     for (let i = 0; pageLinks.length > i; i++) {
    //         pageLinks[i].addEventListener('click', function (e) {
    //             e.preventDefault()
    //             console.log('button clicked')
    //             let page = this.dataset.page
    //             searchForm.innerHTML += `<input value="${page}" name="page" hidden/>`
    //             searchForm.submit()
    //         })
    //     }
    // }

    setTimeout(function () {
        $(".alert").delay(1000).slideUp(200, function () {
            $(this).alert('close');
        });
    }, 3000);

});
