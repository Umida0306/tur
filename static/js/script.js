document.addEventListener('DOMContentLoaded', function() {
    const currencySelector = document.getElementById('currency-selector');

    currencySelector.addEventListener('change', function() {
        const selectedCurrency = currencySelector.value;
        const prices = document.querySelectorAll('.price');

        prices.forEach(priceElement => {
            const basePrice = parseFloat(priceElement.getAttribute('data-price'));
            let convertedPrice;

            if (selectedCurrency === 'USD') {
                convertedPrice = (basePrice / 75).toFixed(2); // Примерный курс USD к RUB
                priceElement.innerText = ${convertedPrice} $;
            } else if (selectedCurrency === 'EUR') {
                convertedPrice = (basePrice / 85).toFixed(2); // Примерный курс EUR к RUB
                priceElement.innerText = ${convertedPrice} €;
            } else {
                priceElement.innerText = ${basePrice} руб.;
            }
        });
    });
});