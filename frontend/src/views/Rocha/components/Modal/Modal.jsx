// Modal.js

import { useEffect, useState } from 'react';

import { Check } from 'lucide-react';

const Modal = ({ modalData, isOpen, onClose, onAdd }) => {
    const [selectedItems, setSelectedItems] = useState([]);
    const [prevSelectedItems, setPrevSelectedItems] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [filteredData, setFilteredData] = useState([]);
    
    useEffect(() => {
        if (isOpen) {
            setPrevSelectedItems(selectedItems);
        }
    }, [isOpen]);

    useEffect(() => {
        const filtered = modalData.filter(item =>
            item.description.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setFilteredData(filtered);
    }, [modalData, searchTerm]);

    const handleSelect = (item) => {
        const selectedIndex = selectedItems.indexOf(item);
        if (selectedIndex === -1) {
            setSelectedItems([...selectedItems, item]);
        } else {
            const updatedSelectedItems = [...selectedItems];
            updatedSelectedItems.splice(selectedIndex, 1);
            setSelectedItems(updatedSelectedItems);
        }
    };

    const handleSearchChange = (e) => {
        setSearchTerm(e.target.value);
    };

    const handleAddButton = () => {
        onAdd(selectedItems);
    };

    const handleCancel = () => {
        setSelectedItems(prevSelectedItems);
        onClose();
    };

    return (
        <div className={`fixed inset-0 flex justify-center items-center ${isOpen ? '' : 'hidden'}`}>
            {isOpen && (
                <>
                    <div className="absolute inset-0 bg-gray-900 bg-opacity-50" onClick={handleCancel}></div>
                    <div className="flex flex-col bg-white p-12 rounded-md shadow-md w-2/5 h-3/5 relative z-10">
                        <div className="flex flex-col mb-4 items-center">
                            <p>Pesquise os itens que deseja selecionar</p>
                            <input type="text" className="border border-gray-300 p-2 rounded-md text-center w-2/3 h-8" value={searchTerm} onChange={handleSearchChange} />
                        </div>
                        <div className="h-64 mb-4 overflow-y-auto">
                            {filteredData.map((item) => (
                                <div key={item.id} className="flex items-center justify-between bg-gray-200 border border-white pl-3 py-1" onClick={() => handleSelect(item)}>
                                    <p>{item.description}</p>
                                    {selectedItems.includes(item) && <Check className="w-6 h-6 text-green-500" />}
                                </div>
                            ))}
                        </div>
                        <div className="flex justify-center gap-8 mt-8">
                            <button onClick={handleAddButton} className="bg-orange-500 text-white font-semibold py-1 px-4 rounded h-8 w-24">
                                Inserir
                            </button>
                            <button onClick={handleCancel} className="bg-red-500 text-white font-semibold py-1 px-4 rounded h-8 w-24">
                                Cancelar
                            </button>
                        </div>
                    </div>
                </>
            )}
        </div>
    );
};

export default Modal;
