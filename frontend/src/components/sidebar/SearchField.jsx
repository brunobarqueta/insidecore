import Input from '../Input';
import { Search } from 'lucide-react';
import useSearchStore from '@/store/search';

const SearchField = () => {
    const searchText = useSearchStore((state) => state.searchText);
    const setSearchText = useSearchStore((state) => state.setSearchText);

    const handleSearchChange = (e) => {
        setSearchText(e.target.value);
    };

    return (
        <div className="relative mt-10 mb-8">
            <Input
                type="text"
                value={searchText}
                onChange={handleSearchChange}
                className="appearance-none bg-zinc-100 rounded-full w-full h-8 py-2 px-4 md:px-5 text-gray-700 text-xs leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Buscar"
            />
            <Search className="h-4 w-4 absolute top-3 right-3 md:top-2 md:right-3 text-gray-400" />
        </div>
    );
};

export default SearchField;
