import { create } from 'zustand'
import useAxios from '../utils/useAxios'

const useItemRegistrationStore = create((set) => ({
    data: [{
            id: 1,
            code: '2',
            description: 'Teste 22',
            process: 'test2',
            rubric: 'Rubrica teste 2',
            application: 'aplicacao teste 2',
        },
        {
            id: 2,
            code: '1',
            description: 'Teste 11',
            process: 'test',
            rubric: 'Rubrica teste 1',
            application: 'aplicacao teste 1',
        },
    ],
    addItem: (item) => set((state) => ({ data: [...state.data, item] })),
    removeItem: (id) => set((state) => ({ data: state.data.filter((item) => item.id !== id) })),
    fetchItems: async() => {
        const api = useAxios()
        try {
            const { data } = await api.get('/simalfa/api/v1/service-item')
            const { result } = data
            //this one works with the api >>>>>
            //set((state) => ({ data: result }))
            set(() => ({ result }))
        } catch (error) {
            console.error('Error fetching items:', error)
        }
    },
}))

export default useItemRegistrationStore