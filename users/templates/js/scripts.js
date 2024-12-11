document.getElementById("aplicar-filtros").addEventListener("click", function () {
    const filtroPrecio = document.getElementById("precio").value;
    const destinos = document.querySelectorAll(".destino");

    destinos.forEach((destino) => {
        const precio = destino.getAttribute("data-precio");

        if (filtroPrecio === "todos" || filtroPrecio === precio) {
            destino.style.display = "block";
        } else {
            destino.style.display = "none";
        }
    });
});














document.getElementById("aplicar-filtros").addEventListener("click", function () {
    const filtroPrecio = document.getElementById("precio").value;
    const destinos = document.querySelectorAll(".destino");

    destinos.forEach((destino) => {
        const precio = destino.getAttribute("data-precio");

        if (filtroPrecio === "todos" || filtroPrecio === precio) {
            destino.style.display = "block";
        } else {
            destino.style.display = "none";
        }
    });
});
