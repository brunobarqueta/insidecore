import { create } from 'zustand';

const useSearchStore = create((set) => ({
    searchText: '',
    setSearchText: (text) => set({ searchText: text }),
    items: [{
            title: 'Dashboard de visualização financeira',
            date: '20/20/2023',
        },
        {
            title: 'Teste título',
            date: '09/01/2020',
        },
        {
            title: 'Dashboard de visualização financeira',
            date: '20/20/2023',
        },
        {
            title: 'Teste título',
            date: '09/01/2020',
        },
        {
            title: 'Dashboard de visualização financeira',
            date: '20/20/2023',
        },
        {
            title: 'Teste título',
            date: '09/01/2020',
        },
        {
            title: 'Dashboard de visualização financeira',
            date: '20/20/2023',
        },
        {
            title: 'Teste título',
            date: '09/01/2020',
        },
        {
            title: 'Dashboard de visualização financeira',
            date: '20/20/2023',
        },
        {
            title: 'Teste título',
            date: '09/01/2020',
        },
    ],
    setItems: (items) => set({ items }),
}));

export default useSearchStore;