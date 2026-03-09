$(function () {
    const $button = $('#show-more-cases');
    const $wrap = $('#works-more-wrap');
    const $list = $('#works-list');

    if (!$button.length) {
        return;
    }

    let isLoading = false;

    $button.on('click', function (e) {
        e.preventDefault();

        if (isLoading) {
            return;
        }

        const url = $button.data('url');
        const nextPage = $button.data('next-page');

        if (!nextPage) {
            return;
        }

        isLoading = true;
        $button.addClass('is-loading');
        $button.find('span').text('Загрузка...');

        $.ajax({
            url: url,
            type: 'GET',
            data: {
                page: nextPage
            },
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function (response) {
                $list.append(response.html);

                if (response.has_next) {
                    $button.data('next-page', response.next_page);
                    $button.find('span').text('Показать еще');
                } else {
                    $wrap.remove();
                }
            },
            error: function () {
                $button.find('span').text('Ошибка загрузки');
                setTimeout(function () {
                    $button.find('span').text('Показать еще');
                }, 1500);
            },
            complete: function () {
                isLoading = false;
                $button.removeClass('is-loading');
            }
        });
    });
});