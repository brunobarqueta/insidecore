import { Plus } from 'lucide-react'

const DividerTitle = ({ ...props }) => {
    return (
        <div className="my-6">
            <div className="flex justify-between items-center">
                <p className="uppercase text-3xl font-bold text-gray-700 text-left">{props.title}</p>
                {!props.hideButton && (
                    <button className="ml-auto rounded-full h-6 w-6 bg-orange-500 text-white flex items-center justify-center" onClick={props.clickFunction}>
                        <Plus className="h-5 w-5" />
                    </button>
                )}
            </div>
            <div className="w-full h-0.5 shadow-lg bg-gray-500 border-gray-400" />
        </div>
    )
}

export default DividerTitle
