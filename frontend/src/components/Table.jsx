import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';

import EditIcon from '../assets/edit-icon.svg';
import TrashIcon from '../assets/trash-icon.svg';
import useItemRegistration from '@/store/itemRegistration';

const ItemTable = () => {
    const items = useItemRegistration((state) => state.data);
    console.log(items);
    const removeItem = useItemRegistration((state) => state.removeItem);

    const handleDelete = (grupo) => {
        removeItem(grupo);
    };

    return (
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead className="w-[100px]">ID</TableHead>
                    <TableHead>Descrição</TableHead>
                    <TableHead>Processo</TableHead>
                    <TableHead>Valor</TableHead>
                    <TableHead>Rúbrica</TableHead>
                    <TableHead>Aplicação</TableHead>
                    <TableHead>Ações</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {items.map((item, index) => (
                    <TableRow key={index}>
                        <TableCell className="font-medium">{item.grupo}</TableCell>
                        <TableCell>{item.descricao}</TableCell>
                        <TableCell>{item.processo}</TableCell>
                        <TableCell>{item.valor}</TableCell>
                        <TableCell>{item.rubrica}</TableCell>
                        <TableCell>{item.aplicacao}</TableCell>
                        <TableCell>
                            <div className="flex gap-2">
                                <img className="cursor-pointer" src={EditIcon} />
                                <img onClick={() => handleDelete(item.grupo)} className="cursor-pointer" src={TrashIcon} />
                            </div>
                        </TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    );
};

export default ItemTable;
