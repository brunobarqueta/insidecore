import { useEffect, useState } from 'react'

import Input from '@/components/Input'
import MaskInput from '@/components/MaskInput'
import NavBar from '@/components/NavBar'
import SelectField from '@/components/SelectField'
import Table from '@/components/Table'
import Table2 from '@/components/Table2'
import Textarea from '@/components/TextArea'
import useFormulaStore from '@/store/formula'
import useGroup from '@/store/group'
import useItemRegistration from '@/store/itemRegistration'
import { useParams } from 'react-router-dom'

const processItems = [
    {
        id: 'test',
        description: 'Test',
    },
    {
        id: 'test2',
        description: 'Test 2',
    },
    {
        id: 'test3',
        description: 'Test 3',
    },
]

const ItemRegistration = () => {
    const { id } = useParams()
    const { data, addItem, editItem } = useItemRegistration((state) => state)
    const { groups, fetchGroups } = useGroup((state) => state)
    const { formulas, fetchFormulas } = useFormulaStore((state) => state)
    const [isEditMode, setIsEditMode] = useState(false)
    const [formData, setFormData] = useState({
        code: '',
        description: '',
        process: '',
        rubric: '',
        application: '',
        formula_fcl: '',
        formula_lcl: '',
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
        //fetchGroups()
        fetchFormulas()
        console.log(formulas)
    }, [])

    useEffect(() => {
        console.log(formData)
    }, [formData])

    const handleSubmit = async (e) => {
        e.preventDefault()
        const newItem = { ...formData }
        console.log(newItem)
        if (isEditMode) {
            editItem(newItem)
        } else {
            addItem(newItem)
            //setFormData({ code: '', description: '', process: '', rubric: '', application: '' })
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
                    <div>
                        <div className="mb-2">
                            <label>Código</label>
                        </div>
                        <MaskInput
                            className="border border-gray-300 w-[300px]"
                            mask="9.999.999.999" 
                            type="text"
                            name="code"
                            value={formData.code}
                            onChange={handleChange}
                            placeholder="X.XXX.XXX.XXX"
                            fixedBg={true}
                        />
                    </div>
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
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="formula_fcl"
                        label={'Formula FCL'}
                        items={formulas}
                        placeholder={'Selecione'}
                        width={'min-w-[200px]'}
                        value={formData.formula_fcl}
                    />
                    <SelectField
                        handleSelectChange={handleSelectChange}
                        name="formula_lcl"
                        label={'Formula LCL'}
                        items={formulas}
                        placeholder={'Selecione'}
                        width={'min-w-[200px]'}
                        value={formData.formula_lcl}
                    />
                </div>
                <div className="w-1/3">
                    <Table2 />
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
                <Table 
                    tableHeads={['Ativo', 'Código', 'Descrição', 'Processo', 'Rúbrica', 'Aplicação']}

                />
            </form>
        </div>
    )
}

export default ItemRegistration
