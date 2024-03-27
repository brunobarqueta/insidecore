import DataPicker from '../DataPicker/DataPicker'
import DividerTitle from '../DividerTitle/DividerTitle'
import RochaInput from '../Input/RochaInput'
import { useState } from 'react'

const ComplementaryServicesSection = ({ ...props }) => {
    const [date, setDate] = useState(new Date())

    return (
        <>
            <DividerTitle title="serviços complementares" hideButton={true} />
            <div className="flex gap-4">
                <div className="flex flex-col">
                    <label className="text-sm font-bold text-gray-600">Data de entrada</label>
                    <DataPicker />
                </div>
                <div className="flex flex-col">
                    <label className="text-sm font-bold text-gray-600">Data de saída</label>
                    <DataPicker />
                </div>
                {props.active == 'LCL' && <RochaInput id={'cif-services'} label={'CIF'} />}
            </div>
        </>
    )
}

export default ComplementaryServicesSection
