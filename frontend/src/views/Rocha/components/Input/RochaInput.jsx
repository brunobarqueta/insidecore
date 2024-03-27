const RochaInput = ({...props}) => {
    return (
        <div className="flex flex-col">
            <label htmlFor={props.id} className="text-sm font-bold text-gray-600">{props.label}</label>
            <input type="text" id={props.id} className="input-field h-7 border rounded text-sm px-2" />
        </div>
    )
}

export default RochaInput
