window.onload = function () {
    $('.product_list').on('click', 'input[class="btn"]', function () {
        let target = event.target;
        $.ajax({
            url: '/baskets/basket-add/' + target.name + '/',
            success: function (data) {
                $('.product_list').html(data.result);
            }
        })
    })
}