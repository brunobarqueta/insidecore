import { useEffect, useState } from 'react'

import Input from '@/components/Input'
import NavBar from '@/components/NavBar'
import SelectField from '@/components/SelectField'
import Table from '@/components/Table'
import Textarea from '@/components/TextArea'
import useGroup from '@/store/group'
import useItemRegistration from '@/store/itemRegistration'
import { useParams } from 'react-router-dom'

const processItems = [
    {
        code: 'test',
        name: 'Test',
    },
    {
        code: 'test2',
        name: 'Test 2',
    },
    {
        code: 'test3',
        name: 'Test 3',
    },
]

const ItemRegistration = () => {
    const { id } = useParams()
    const { data, addItem, editItem } = useItemRegistration((state) => state)
    const { groups, fetchGroups } = useGroup((state) => state)
    const [isEditMode, setIsEditMode] = useState(false)
    const [formData, setFormData] = useState({
        code: '',
        description: '',
        process: '',
        rubric: '',
        application: '',
    })

    useEffect(() => {
        setIsEditMode(id !== undefined)
        if (id !== undefined) {
            const itemData = data.find((item) => item.id === parseInt(id))
            if (itemData) {
                setFormData(itemData)
            }
        }
    }, [id])

    useEffect(() => {
        fetchGroups()
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const newItem = { ...formData }
        if (isEditMode) {
            editItem(newItem)
        } else {
            addItem(newItem)
            setFormData({ code: '', description: '', process: '', rubric: '', application: '' })
        }
        
    }

    const handleChange = (e) => {
        const { name, value } = e.target
        setFormData({ ...formData, [name]: value })
    }

    const handleSelectChange = (name, value) => {
        setFormData({ ...formData, [name]: value })
    }

    return (
        <div className="w-full h-full bg-gray-100 font-inter">
            <NavBar />
            <form className="mt-4 px-32 py-32" onSubmit={handleSubmit}>
                <div className="flex gap-8">
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="code"
                        label={'Grupo'}
                        items={groups}
                        placeholder={'Selecione'}
                        width={'min-w-[200px]'}
                        value={formData.code}
                    />
                    <div>
                        <div className="mb-2">
                            <label>Descrição</label>
                        </div>
                        <Input
                            className="border border-gray-300 w-[300px]"
                            type="text"
                            name="description"
                            value={formData.description}
                            onChange={handleChange}
                            placeholder="Descrição"
                            fixedBg={true}
                        />
                    </div>
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="process"
                        label={'Processo'}
                        items={processItems}
                        placeholder={'Selecione'}
                        width={'min-w-[200px]'}
                        value={formData.process}
                    />
                </div>
                <div className="flex gap-8 mt-8">
                    <div className="w-3/5">
                        <div className="mb-2">
                            <label>Rubrica</label>
                        </div>
                        <Textarea name="rubric" onChange={handleChange} value={formData.rubric} />
                    </div>
                    <div className="w-2/5">
                        <div className="mb-2">
                            <label>Aplicação</label>
                        </div>
                        <Textarea name="application" onChange={handleChange} value={formData.application} />
                    </div>
                </div>
                <div className="float-right">
                    <button className="w-36 mt-4 py-1 text-sm hover:text-gray-700 border border-blue-900 rounded-full bg-blue-900 hover:bg-gray-100 text-white">
                        {isEditMode ? 'Salvar' : 'Novo'}
                    </button>
                </div>
                <Table />
            </form>
        </div>
    )
}

export default ItemRegistration
