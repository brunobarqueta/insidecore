import { create } from 'zustand'
import useAxios from '../utils/useAxios'

const useMetricStore = create((set, get) => ({
    metrics: [],
    api: useAxios(),
    fetchMetrics: async() => {
        const { api } = get()
        try {
            const response = await api.get('/simalfa/api/v1/metrics/')
            const updatedMetrics = response.data.result.map((metric) => ({
                ...metric,
                id: metric.id.toString(),
            }))
            set(() => ({ metrics: updatedMetrics }))
        } catch (error) {
            console.error('Error fetching items:', error)
        }
    },
}))

export default useMetricStore