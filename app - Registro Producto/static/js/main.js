const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const listDelete = Array.from(btnDelete)
    listDelete.forEach((list) => {
        list.addEventListener('click', (e) => {
            if(!confirm('¿Estás seguro que quieres eliminar este producto?')) {
                e.preventDefault();
            }
        })
    })
}