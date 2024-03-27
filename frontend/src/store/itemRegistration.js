import { create } from 'zustand'
import useAxios from '../utils/useAxios'

const useItemRegistrationStore = create((set, get) => ({
    data: [],
    api: useAxios(),
    addItem: async(item) => {
        const { api } = get()

        try {
            const response = await api.post('/simalfa/api/v1/service-item/', {
                ...item,
                code: parseInt(item.code),
                formula_fcl: 1,
                formula_lcl: 1,
                tenants: [1],
                metrics: [1],
            })
            set((state) => ({ data: [...state.data, {...item, id: response.data.result.id, active: response.data.result.active }] }))
        } catch (error) {
            console.log(error)
        }
    },
    removeItem: async(id) => {
        const { api } = get()
        try {
            await api.patch(`/simalfa/api/v1/service-item/${id}/`)
            set((state) => ({
                data: state.data.map((item) => {
                    if (item.id === id) {
                        return {
                            ...item,
                            active: !item.active,
                        }
                    }
                    return item
                }),
            }))
        } catch (error) {
            console.error('Error updating item:', error)
        }
    },
    fetchItems: async() => {
        const { api } = get()
        try {
            const { data } = await api.get('/simalfa/api/v1/service-item')
            const { result } = data
            //this one works with the api >>>>>
            set(() => ({ data: result.sort((a, b) => a.id - b.id) }))
                //set(() => ({ result }))
        } catch (error) {
            console.error('Error fetching items:', error)
        }
    },
    editItem: async(formData) => {
        const { api, data } = get()
        try {
            const response = await api.put(`/simalfa/api/v1/service-item/${formData.id}/`, {
                ...formData,
                code: parseInt(formData.code),
                formula_fcl: 1,
                formula_lcl: 1,
                tenants: [1],
                metrics: [1],
            })
            set((state) => ({
                data: state.data.map((item) => {
                    if (item.id === formData.id) {
                        return {...response.data.result }
                    }
                    return item
                }),
            }))
        } catch (error) {
            console.error('Error updating item:', error)
        }
    },
}))

export default useItemRegistrationStore