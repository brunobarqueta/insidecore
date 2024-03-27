import DividerTitle from './DividerTitle/DividerTitle'
import RochaInput from './Input/RochaInput'
import RochaTable from './Table/RochaTable'
import ServiceTypeButtons from './ServiceTypeButtons/ServiceTypeButtons'
import logoRocha from '../assets/logo-rocha.svg'
import { useState } from 'react'

const Simulation = () => {
    const [active, setActive] = useState("FCL")

    return (
        <div className="bg-white min-h-screen font-helvetica pb-1">
            <nav className="bg-orange-500 text-white p-4 flex items-center justify-between">
                <div className="flex items-center">
                    <img src={logoRocha} alt="Logo" className="h-12 mr-4" />
                    <span className="text-lg font-bold">Simulações</span>
                </div>
                <div className="flex items-center space-x-8 font-semibold text-xs">
                    <a href="#" className="hover:text-gray-200">
                        Manual de Uso
                    </a>
                    <a href="#" className="hover:text-gray-200">
                        Início
                    </a>
                    <a href="#" className="hover:text-gray-200">
                        Painel Administrativo
                    </a>
                </div>
            </nav>
            <div className="w-full h-10 pl-16 shadow-md border border-1 text-md mt-4 font-bold flex items-center text-gray-500">SIMULAÇÕES</div>
            <div className="bg-gray-100 m-6 pt-6 pb-28 px-6">
                <ServiceTypeButtons active={active} setActive={setActive} />

                <DividerTitle title="dados" />

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mx-auto max-w-4xl">
                    <RochaInput id={'empresa'} label={'Empresa'} />
                    <RochaInput id={'nome'} label={'Nome'} />
                    <RochaInput id={'data-criacao'} label={'Data da Criação'} />
                    {active == "FCL" ? <RochaInput id={'cif'} label={'CIF'} /> : <div></div>}
                    <RochaInput id={'telefone'} label={'Telefone'} />
                    <RochaInput id={'email'} label={'Email'} />
                </div>

                <DividerTitle title="serviços inerentes" />
                <RochaTable
                    headerText="Tipo de Container"
                    rowData={[
                        { tipo: 'CONTAINER 40”', qtd: '' },
                        { tipo: 'CONTAINER 20”', qtd: '' },
                        { tipo: 'One Top 20”', qtd: '' },
                        { tipo: 'Flat Rack 20”', qtd: '' },
                    ]}
                />

                <DividerTitle title="acessórios serviços" />
                <div className="flex gap-4">
                    <RochaInput id={'data-entrada'} label={'Data de entrada'} />
                    <RochaInput id={'data-saida'} label={'Data de saída'} />
                    {active == "LCL" && <RochaInput id={'cif-services'} label={'CIF'} />}
                </div>

                <DividerTitle title="acessórios serviços" />
                <RochaTable headerText="Armazenagem" rowData={[{ tipo: 'Importação 20”', qtd: '' }]} />
                <RochaTable headerText="Outros" rowData={[{ tipo: 'Fornecimento e colocação de rótulos ou adesivos, por rótulo', qtd: '' }]} />

                <DividerTitle title="serviços diversos" />
                    
                <button className="bg-green-400 uppercase font-bold text-black mt-12 py-2 px-4 rounded float-right">
                    Gerar Simulação
                </button>
                
            </div>
        </div>
    )
}

export default Simulation
