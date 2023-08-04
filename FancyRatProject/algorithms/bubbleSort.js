function bubbleSort(lista) {
    let lon = lista.length;
    let swapped;
    do {
        swapped = false;
        // Recorrer la lista
        for (let i = 0; i < lon - 1; i++) {
            // Verificar si los dos valores están ordenados
            if (lista[i] > lista[i + 1]) {
                // Ordenar si es necesario
                let temp = lista[i];
                lista[i] = lista[i + 1];
                lista[i + 1] = temp;
                swapped = true;
            }
        }
        lon--;
    } while (swapped);
    return lista;
}

function mostrarLista(lista) {
    for (let i = 0; i < lista.length; i++) {
        process.stdout.write(lista[i] + " ");
    }
    console.log(lista);
}

let lista = [5, 2, 4, 1, 3];
mostrarLista(lista);
lista = bubbleSort(lista);
mostrarLista(lista);