import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { useEffect, useState } from 'react'

import Input from './Input'
import useMetricStore from '@/store/metrics'

const Table2 = () => {
    const { metrics, fetchMetrics } = useMetricStore((state) => state)
    const [tableData, setTableData] = useState({});

    useEffect(() => {
        fetchMetrics()
    }, [])

    const handleChange = (event, id) => {
        const { name, value } = event.target;
        setTableData(prevState => ({
            ...prevState,
            [id]: {
                ...prevState[id],
                [name]: value
            }
        }));
    };

    return (
        <>
            {metrics && metrics.length > 0 && (
                <Table className="mt-2">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Descrição</TableHead>
                            <TableHead>Valor</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {metrics.map((item) => (
                            <TableRow key={item.id}>
                                <TableCell>{item.description}</TableCell>
                                <TableCell>
                                    <Input
                                        className="border border-gray-300 w-[300px]"
                                        type="text"
                                        name="qtd"
                                        value={tableData[item.id]?.qtd || ''}
                                        onChange={(e) => handleChange(e, item.id)}
                                        placeholder="Descrição"
                                        fixedBg={true}
                                    />
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            )}
        </>
    )
}

export default Table2
