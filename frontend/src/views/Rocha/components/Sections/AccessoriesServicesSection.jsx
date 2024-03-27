import DividerTitle from "../DividerTitle/DividerTitle"
import Modal from "../Modal/Modal";
import RochaTable from "../Table/RochaTable"
import useItemRegistrationStore from "@/store/itemRegistration";
import { useState } from "react";

const AccessoriesServiceSection = () => {
    const { data } = useItemRegistrationStore((state) => state);
    const [isOpen, setIsOpen] = useState(false);
    const [selectedItems, setSelectedItems] = useState([]);

    const filteredData = data.filter(item => item.code.startsWith('2'));

    const handleAddButton = (selectedItems) => {
        setSelectedItems(selectedItems);
        setIsOpen(false)
    };

    return (
        <>
            <DividerTitle title="serviços acessórios" clickFunction={() => setIsOpen(true)} />
            <RochaTable headerText="Armazenagem" rowData={selectedItems} />
            {/*<RochaTable headerText="Outros" rowData={[{ tipo: 'Fornecimento e colocação de rótulos ou adesivos, por rótulo', qtd: '' }]} />*/}
            <Modal
                modalData={filteredData}
                isOpen={isOpen}
                onClose={() => setIsOpen(false)}
                onAdd={handleAddButton} // Passa a função de inserir para o modal
            />
        </>
    )
}

export default AccessoriesServiceSection
