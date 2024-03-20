import { create } from 'zustand'
import useAxios from '../utils/useAxios'

const useFormulaStore = create((set, get) => ({
    formulas: [],
    api: useAxios(),
    fetchFormulas: async() => {
        const { api } = get()
        try {
            const response = await api.get('/simalfa/api/v1/formula/')
            const updatedFormulas = response.data.result.map((formula) => ({
                ...formula,
                id: formula.id.toString(),
            }))
            set(() => ({ formulas: updatedFormulas }))
        } catch (error) {
            console.error('Error fetching items:', error)
        }
    },
}))

export default useFormulaStore