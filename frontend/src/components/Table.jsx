import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table'

import EditIcon from '../assets/edit-icon.svg'
import { Link } from 'react-router-dom'
import { Switch } from './ui/switch'
import TrashIcon from '../assets/trash-icon.svg'
import { useEffect } from 'react'
import useItemRegistration from '@/store/itemRegistration'

const ItemTable = () => {
    const { data, removeItem, fetchItems } = useItemRegistration((state) => state)

    const handleDelete = (code) => {
        removeItem(code)
    }

    useEffect(() => {
        fetchItems()
    }, [])

    return (
        <>
            {data && data.length > 0 ? (
                <Table className="mt-8">
                    <TableHeader>
                        <TableRow>
                            <TableHead>Ativo</TableHead>
                            <TableHead className="w-[100px]">Código</TableHead>
                            <TableHead>Descrição</TableHead>
                            <TableHead>Processo</TableHead>
                            {/*<TableHead>Valor</TableHead>*/}
                            <TableHead>Rúbrica</TableHead>
                            <TableHead>Aplicação</TableHead>
                            <TableHead>Ações</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {data.map((item) => (
                            <TableRow key={item.id}>
                                <TableCell>
                                    <Switch checked={item.active} onClick={() => handleDelete(item.id)}/>
                                </TableCell>
                                <TableCell className="font-medium">{item.code}</TableCell>
                                <TableCell>{item.description}</TableCell>
                                <TableCell>{item.process}</TableCell>
                                {/*<TableCell>{item.valor}</TableCell>*/}
                                <TableCell>{item.rubric}</TableCell>
                                <TableCell>{item.application}</TableCell>
                                <TableCell>
                                    <div className="flex gap-2">
                                        <Link to={`/item-registration/${item.id}`}>
                                            <img className="cursor-pointer" src={EditIcon} alt="Editar" />
                                        </Link>
                                        {/*<img onClick={() => handleDelete(item.id)} className="cursor-pointer" src={TrashIcon} alt="Excluir" />*/}
                                    </div>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            ) : (
                <div className="flex justify-center mt-20">
                    <p>Nenhum item cadastrado</p>
                </div>
            )}
        </>
    )
}

export default ItemTable
