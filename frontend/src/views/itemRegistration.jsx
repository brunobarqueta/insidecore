import { Minus, Plus } from 'lucide-react'
import { useEffect, useState } from 'react'

import Input from '@/components/Input'
import MaskInput from '@/components/MaskInput'
import NavBar from '@/components/NavBar'
import { Player } from '@lottiefiles/react-lottie-player'
import SelectField from '@/components/SelectField'
import Table from '@/components/Table'
import Table2 from '@/components/Table2'
import Textarea from '@/components/TextArea'
import loading from '../assets/loading'
import useFormulaStore from '@/store/formula'
import useItemRegistration from '@/store/itemRegistration'
import { useParams } from 'react-router-dom'
import { useToast } from '@/components/ui/use-toast'

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
    const { formulas, fetchFormulas } = useFormulaStore((state) => state)
    const { toast } = useToast()
    const [metricsData, setMetricsData] = useState({})
    const [isLoading, setIsLoading] = useState(false)
    const [metricsAreOpen, setMetricsAreOpen] = useState(false)
    const [isEditMode, setIsEditMode] = useState(false)
    const [filteredMetrics, setFilteredMetrics] = useState([])
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
        if (formData.formula_fcl || formData.formula_lcl) {
            const selectedFormula1 = formulas.find((formula) => formula.id === formData.formula_fcl)
            const selectedFormula2 = formulas.find((formula) => formula.id === formData.formula_lcl)
            const metrics1 = selectedFormula1 ? selectedFormula1.metrics : []
            const metrics2 = selectedFormula2 ? selectedFormula2.metrics : []

            const combinedMetrics = [...metrics1, ...metrics2]

            const uniqueMetrics = combinedMetrics.filter((metric, index, self) => index === self.findIndex((m) => m.id === metric.id))

            setFilteredMetrics(uniqueMetrics)
        } else {
            setFilteredMetrics([])
        }
    }, [formData, formulas])

    useEffect(() => {
        setIsEditMode(id !== undefined)
        if (id !== undefined) {
            const itemData = data.find((item) => item.id === parseInt(id))
            if (itemData) {
                setFormData({
                    code: itemData.code,
                    description: itemData.description,
                    process: itemData.process,
                    rubric: itemData.rubric,
                    application: itemData.application,
                    formula_fcl: itemData.formula_fcl.id.toString(),
                    formula_lcl: itemData.formula_lcl.id.toString(),
                })

                const metricsDataObj = {}
                itemData.service_item_metrics.forEach((metric) => {
                    metricsDataObj[metric.metric.id] = {
                        id: metric.metric.id,
                        value: metric.value,
                    }
                })
                setMetricsData(metricsDataObj)
            }
        }
    }, [id, data])

    useEffect(() => {
        fetchFormulas()
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault()
        setIsLoading(true)
        const newItem = { ...formData, metrics: metricsData }
        let response
        if (isEditMode) {
            response = await editItem(newItem, id)
        } else {
            response = await addItem(newItem)
            setFormData({ code: '', description: '', process: '', rubric: '', application: '', formula_fcl: '', formula_lcl: '' })
            setMetricsData({})
        }

        handleResponse(response)
        setIsLoading(false)
    }

    const handleResponse = (response) => {
        if (response.status === 200) {
            toast({
                title: 'Sucesso',
                description: 'Item criado/salvo com sucesso',
                type: 'success',
            })
        } else {
            const errorMessage = response.errors ? response.errors.join('\n ') : 'Erro desconhecido'
            toast({
                title: 'Erro',
                description: errorMessage,
                type: 'error',
            })
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
                <div className="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 gap-8">
                    <div>
                        <div className="mb-2">
                            <label>Código</label>
                        </div>
                        <MaskInput
                            className="border border-gray-300 min-w-[200px]"
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
                            className="border border-gray-300 min-w-[200px]"
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
                    <div className="w-auto">
                        <div className="flex cursor-pointer items-center justify-between" onClick={() => setMetricsAreOpen(!metricsAreOpen)}>
                            <p>Métricas</p>
                            {metricsAreOpen ? <Minus /> : <Plus />}
                        </div>
                        <div className={`${metricsAreOpen ? 'max-h-96 transition-max-h duration-1000 ease-out overflow-hidden' : 'max-h-0'}`}>
                            {metricsAreOpen && <Table2 data={filteredMetrics} metricsData={metricsData} setMetricsData={setMetricsData} />}
                        </div>
                    </div>
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
                    <button className={`w-36 mt-4 py-1 text-sm hover:text-gray-700 border border-blue-900 rounded-full bg-blue-900 hover:bg-gray-100 text-white ${isLoading && 'pointer-events-none'}`}>
                        {isLoading ? <Player src={loading} className="player w-5 h-5" loop autoplay /> : isEditMode ? 'Salvar' : 'Novo'}
                    </button>
                </div>
                <Table tableHeads={['Ativo', 'Código', 'Descrição', 'Processo', 'Rúbrica', 'Aplicação']} />
            </form>
        </div>
    )
}

export default ItemRegistration
