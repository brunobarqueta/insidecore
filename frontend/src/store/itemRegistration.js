import create from 'zustand';

const useItemRegistrationStore = create((set) => ({
    data: [
        {
            grupo: '1.1.1.1',
            descricao: 'Teste 22',
            processo: 'Processo X',
            valor: '120,00',
            rubrica: 'Rubrica teste',
            aplicacao: 'aplicacao teste',
        },
        {
            grupo: '1.1.1.2',
            descricao: 'Teste 22',
            processo: 'Processo X',
            valor: '120,00',
            rubrica: 'Rubrica teste',
            aplicacao: 'aplicacao teste',
        },
    ],
    addItem: (item) => set((state) => ({ data: [...state.data, item]})),
    removeItem: (grupo) => set((state) => ({ data: state.data.filter(item => item.grupo !== grupo) })),
}));

export default useItemRegistrationStore;
