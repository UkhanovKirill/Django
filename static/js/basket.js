window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target = event.target;
        $.ajax({
            url: '/baskets/basket-edit/' + target.name + '/' + target.value + '/',
            success: function (data) {
                $('.basket_list').html(data.result);
            }
        })
    })

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