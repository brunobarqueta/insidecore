import { useState } from 'react'

const ServiceTypeButtons = ({...props}) => {

    return (
        <>
            <div className="text-2xl text-center font-semibold">TIPO DE SERVIÇO</div>
            <div className="flex justify-center gap-4 mt-2">
                <button className={`w-28 h-10 rounded ${props.active == 'FCL' ? 'bg-orange-500 text-white' : 'bg-white font-semibold text-black'}`} onClick={() => props.setActive('FCL')}>
                    FCL
                </button>
                <button className={`w-28 h-10 rounded ${props.active == 'LCL' ? 'bg-orange-500 text-white' : 'bg-white font-semibold text-black'}`} onClick={() => props.setActive('LCL')}>
                    LCL
                </button>
            </div>
        </>
    )
}

export default ServiceTypeButtons
