import { create } from 'zustand'
import useAxios from '../utils/useAxios'

const useGroupStore = create((set, get) => ({
    groups: [],
    api: useAxios(),
    fetchGroups: async() => {
        const { api } = get()
        try {
            const response = await api.get('/simalfa/api/v1/groups/')
            const updatedGroups = response.data.result.map((group) => ({
                ...group,
                code: group.code.toString(),
            }))
            set(() => ({ groups: updatedGroups }))
        } catch (error) {
            console.error('Error fetching items:', error)
        }
    },
}))

export default useGroupStore