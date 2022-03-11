window.onload = function () {
    $('.product_list').on('click', 'button[type="button"]', function () {
        let target = event.target.value;
        $.ajax({
            url: '/baskets/basket-add/' + target + '/',
            success: function (data) {
                $('.product_list').html(data.result);
            }
        })
    })
}