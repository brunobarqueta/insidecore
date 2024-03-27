import { create } from 'zustand'
import useAxios from '../utils/useAxios'

const useItemRegistrationStore = create((set, get) => ({
    data: [],
    api: useAxios(),
    addItem: async(item) => {
        const { api } = get()
        const { metrics, ...rest } = item

        const metricsArray = Object.keys(metrics).map((id) => ({
            id,
            value: metrics[id].value,
        }))

        try {
            const response = await api.post('/simalfa/api/v1/service-item/', {
                ...rest,
                formula_fcl: parseInt(item.formula_fcl),
                formula_lcl: parseInt(item.formula_lcl),
                tenant: 1,
                metrics: metricsArray,
            })
            set((state) => ({ data: [...state.data, {...response.data.result }] }))

            return response

        } catch (error) {
            return error.response.data
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
            set(() => ({ data: result.sort((a, b) => a.id - b.id) }))
        } catch (error) {
            console.error('Error fetching items:', error)
        }
    },
    editItem: async(formData, id) => {
        const { api } = get()

        const { metrics, ...rest } = formData

        const metricsArray = Object.keys(metrics).map((id) => ({
            id,
            value: metrics[id].value,
        }))
        try {
            const response = await api.put(`/simalfa/api/v1/service-item/${id}/`, {
                ...rest,
                formula_fcl: parseInt(formData.formula_fcl),
                formula_lcl: parseInt(formData.formula_lcl),
                tenant: 1,
                metrics: metricsArray
            })
            set((state) => ({
                data: state.data.map((item) => {
                    if (item.id === parseInt(id)) {
                        return {...response.data.result }
                    }
                    return item
                }),
            }))

            return response
        } catch (error) {
            return error.response.data
        }
    },
}))

export default useItemRegistrationStore