var swiper = new Swiper('.swiper-container', {
// Enable lazy loading
   lazy: true,
        pagination: {
                el: '.swiper-pagination',
                type: 'progressbar',
        },
        navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
        },

});
