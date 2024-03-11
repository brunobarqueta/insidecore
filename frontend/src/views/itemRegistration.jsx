import Input from '@/components/Input';
import MaskInput from '@/components/MaskInput';
import NavBar from '@/components/NavBar';
import SelectField from '@/components/SelectField';
import Table from '@/components/Table';
import Textarea from '@/components/TextArea';
import useItemRegistration from '@/store/itemRegistration';
import { useState } from 'react';

const processItems = [
    {
        value: 'test',
        text: 'Test',
    },
    {
        value: 'test2',
        text: 'Test 2',
    },
    {
        value: 'test3',
        text: 'Test 3',
    },
];

const groupItems = [
    {
        value: '1',
        text: '1',
    },
    {
        value: '2',
        text: '2',
    },
    {
        value: '3',
        text: '3',
    },
];

const ItemRegistration = () => {
    const [formData, setFormData] = useState({
        grupo: '',
        item: '',
        subItem: '',
        descricao: '',
        processo: '',
        valor: '',
        rubrica: '',
        aplicacao: '',
    });

    const setItemRegistration = useItemRegistration((state) => state.addItem);

    const handleSubmit = (e) => {
        e.preventDefault();
        const newItem = { ...formData };
        setItemRegistration(newItem);
        setFormData({ grupo: '', item: '', subItem: '', descricao: '', processo: '', valor: '', rubrica: '', aplicacao: '' });
    };

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSelectChange = (name, value) => {
        setFormData({ ...formData, [name]: value });
        console.log(formData);
    };

    return (
        <div className="w-full h-full bg-gray-100">
            <NavBar />
            <form className="mt-4 px-32 py-32" onSubmit={handleSubmit}>
                <div className="flex gap-8">
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="grupo"
                        label={'Grupo'}
                        items={groupItems}
                        placeholder={'Selecione'}
                        width={'min-w-[100px]'}
                    />
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="item"
                        label={'Item'}
                        items={groupItems}
                        placeholder={'Selecione'}
                        width={'min-w-[100px]'}
                    />
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="subItem"
                        label={'Sub Item'}
                        items={groupItems}
                        placeholder={'Selecione'}
                        width={'min-w-[100px]'}
                    />
                    <div>
                        <div className="mb-2">
                            <label>Descrição</label>
                        </div>
                        <Input
                            className="border border-gray-300 w-[300px]"
                            type="text"
                            name="descricao"
                            value={formData.descricao}
                            onChange={handleChange}
                            placeholder="Descrição"
                            fixedBg={true}
                        />
                    </div>
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="processo"
                        label={'Processo'}
                        items={processItems}
                        placeholder={'Selecion.'}
                        width={'min-w-[140px]'}
                    />
                    <div>
                        <div className="mb-2">
                            <label>Valor</label>
                        </div>
                        <MaskInput
                            className="border border-gray-300"
                            mask="999.999,99"
                            type="text"
                            name="valor"
                            value={formData.valor}
                            onChange={handleChange}
                            placeholder="0.00"
                            fixedBg={true}
                        />
                    </div>
                </div>
                <div className="flex gap-8 mt-8">
                    <div className="w-3/5">
                        <div className="mb-2">
                            <label>Rubrica</label>
                        </div>
                        <Textarea name="rubrica" onChange={handleChange} value={formData.rubrica}/>
                    </div>
                    <div className="w-2/5">
                        <div className="mb-2">
                            <label>Aplicação</label>
                        </div>
                        <Textarea name="aplicacao" onChange={handleChange} value={formData.aplicacao}/>
                    </div>
                </div>
                <div className="float-right">
                    <button className="w-36 mt-4 py-1 text-md text-gray-700 border border-blue-900 rounded-full hover:bg-blue-900 hover:text-white">
                        Novo
                    </button>
                </div>
                <Table />
            </form>
        </div>
    );
};

export default ItemRegistration;
