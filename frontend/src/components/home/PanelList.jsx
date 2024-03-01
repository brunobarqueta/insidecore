import ListItem from './ListItem';
import React from 'react';
import useSearchStore from '@/store/search';

const PanelList = () => {
    const items = useSearchStore((state) => state.items);
    const searchText = useSearchStore((state) => state.searchText);

    const filteredItems = items.filter((item) =>
        item.title.toLowerCase().includes(searchText.toLowerCase())
    );

    return (
        <>
            <div className="flex flex-auto gap-28 mt-5 mb-2 ml-8 mr-1 text-xs text-gray-500 font-light">
                <p className="w-4/5">Painel</p>
                <p className="mr-2">Data</p>
                <p className="ml-1">Ações</p>
                <p>Status</p>
            </div>
            <div className="flex flex-col gap-4">
                {filteredItems.map((item, i) => (
                    <ListItem key={i} title={item.title} date={item.date} />
                ))}
            </div>
        </>
    );
};

export default PanelList;
