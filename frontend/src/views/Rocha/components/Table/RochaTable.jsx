const RochaTable = ({ headerText, rowData }) => {
    return (
        <table className="w-full text-sm">
            <thead>
                <tr className="bg-orange-500 text-white">
                    <th className="py-1 px-2 text-left w-4/5">{headerText}</th>
                    <th className="py-1 px-2 w-1/5">QTDE</th>
                </tr>
            </thead>
            <tbody>
                {rowData.map((data, index) => (
                    <tr key={index} className="bg-gray-300 text-black">
                        <td className="py-1 px-2 border border-white">{data.tipo}</td>
                        <td className="py-1 px-2 border border-white text-center">{data.qtd}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default RochaTable;
