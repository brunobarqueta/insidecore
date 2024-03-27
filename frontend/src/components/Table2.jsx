import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'
import { useEffect, useState } from 'react'

import Input from './Input'

const Table2 = ({ data, metricsData, setMetricsData }) => {

    const handleChange = (event, id) => {
        const { name, value } = event.target
        setMetricsData((prevState) => ({
            ...prevState,
            [id]: {
                ...prevState[id],
                [name]: value,
            },
        }))
    }

    return (
        <>
            {data && data.length > 0 && (
                <Table className="mt-2">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Descrição</TableHead>
                            <TableHead>Valor</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {data.map((item) => (
                            <TableRow key={item.id}>
                                <TableCell>{item.description}</TableCell>
                                <TableCell>
                                    <Input
                                        className="border border-gray-300 w-[300px]"
                                        type="text"
                                        name="value"
                                        value={parseInt(metricsData[item.id]?.value) || ''}
                                        onChange={(e) => handleChange(e, item.id)}
                                        placeholder="Valor"
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
