import { useEffect, useState } from 'react'

import AccessoriesServiceSection from './Sections/AccessoriesServicesSection'
import ComplementaryServicesSection from './Sections/ComplementaryServicesSection'
import DataSection from './Sections/DataSection'
import DiverseServicesSection from './Sections/DiverseServicesSection'
import InherentServicesSection from './Sections/InherentServicesSection'
import Modal from './Modal/Modal'
import NavBar from './Nav/NavBar'
import ServiceTypeButtons from './ServiceTypeButtons/ServiceTypeButtons'
import useItemRegistrationStore from '@/store/itemRegistration'

const Simulation = () => {
    const [active, setActive] = useState('FCL')
    const { data, fetchItems } = useItemRegistrationStore((state) => state)
    const [isOpen, setIsOpen] = useState(true)
    
    useEffect(() => {
        fetchItems()
    }, [])

    return (
        <div className="bg-white min-h-screen font-helvetica pb-1">
            <NavBar />
            <div className="w-full h-10 pl-16 shadow-md border border-1 text-md mt-4 font-bold flex items-center text-gray-500">SIMULAÇÕES</div>
            <div className="bg-gray-100 m-6 pt-6 pb-28 px-6">
                <ServiceTypeButtons active={active} setActive={setActive} />

                <DataSection active={active} setActive={setActive}/>
                <InherentServicesSection />
                <ComplementaryServicesSection active={active} setActive={setActive}/>
                <AccessoriesServiceSection />
                <DiverseServicesSection />

                <button className="bg-green-400 uppercase font-bold text-black mt-12 py-2 px-4 rounded float-right">Gerar Simulação</button>
            </div>
        </div>
    )
}

export default Simulation
