document.addEventListener('DOMContentLoaded', function () {
    const toggleFavoriteButtons = document.querySelectorAll('.toggle-favorite');

    // Obtener el token CSRF desde la meta etiqueta
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    toggleFavoriteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product-id');
            const isFavorito = this.getAttribute('data-favorito') === 'true';

            fetch(`/favoritos/${isFavorito ? 'remove' : 'add'}/${productId}/`, {
                method: isFavorito ? 'DELETE' : 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                }
            }).then(response => {
                if (response.ok) {
                    // Actualiza el estado del botón
                    const heartIcon = this.querySelector('use');
                    if (isFavorito) {
                        heartIcon.setAttribute('xlink:href', '#heart');  // Corazón vacío
                        this.setAttribute('data-favorito', 'false');
                    } else {
                        heartIcon.setAttribute('xlink:href', '#heart-filled');  // Corazón lleno
                        this.setAttribute('data-favorito', 'true');
                    }
                } else {
                    console.error('Error al actualizar el favorito:', response.statusText);
                }
            }).catch(error => console.error('Error:', error));
        });
    });
});

