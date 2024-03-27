import DividerTitle from '../DividerTitle/DividerTitle';
import Modal from '../Modal/Modal';
import RochaTable from '../Table/RochaTable';
import useItemRegistrationStore from '@/store/itemRegistration';
import { useState } from 'react';

const InherentServicesSection = () => {
    const { data } = useItemRegistrationStore((state) => state);
    const [isOpen, setIsOpen] = useState(false);
    const [selectedItems, setSelectedItems] = useState([]);

    const filteredData = data.filter(item => item.code.startsWith('1'));

    const handleAddButton = (selectedItems) => {
        setSelectedItems(selectedItems);
        setIsOpen(false)
    };

    return (
        <>
            <DividerTitle title="serviços inerentes" clickFunction={() => setIsOpen(true)} />
            <RochaTable
                headerText="Tipo de Container"
                rowData={selectedItems}
            />
            <Modal
                modalData={filteredData}
                isOpen={isOpen}
                onClose={() => setIsOpen(false)}
                onAdd={handleAddButton} // Passa a função de inserir para o modal
            />
        </>
    );
};

export default InherentServicesSection;
