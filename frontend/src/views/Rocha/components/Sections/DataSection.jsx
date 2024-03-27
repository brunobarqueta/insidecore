import DividerTitle from '../DividerTitle/DividerTitle'
import RochaInput from '../Input/RochaInput'

const DataSection = ({...props}) => {
    return (
        <>
            <DividerTitle title="dados" hideButton={true}/>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mx-auto max-w-4xl">
                <RochaInput id={'empresa'} label={'Empresa'} />
                <RochaInput id={'nome'} label={'Nome'} />
                <RochaInput id={'data-criacao'} label={'Data da Criação'} />
                {props.active == 'FCL' ? <RochaInput id={'cif'} label={'CIF'} /> : <div></div>}
                <RochaInput id={'telefone'} label={'Telefone'} />
                <RochaInput id={'email'} label={'Email'} />
            </div>
        </>
    )
}

export default DataSection
