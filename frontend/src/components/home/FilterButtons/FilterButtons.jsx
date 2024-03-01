import ToggleButton from './ToggleButton';
import { useState } from 'react';

const FilterButtons = () => {
    const [activeButton, setActiveButton] = useState('Todos');

    const handleClick = (label) => {
        setActiveButton(label);
    };

    return (
        <div className="flex gap-4 mt-12">
            <ToggleButton label="Todos" isActive={activeButton === 'Todos'} onClick={() => handleClick('Todos')} />
            <ToggleButton label="Publicado" isActive={activeButton === 'Publicado'} onClick={() => handleClick('Publicado')} />
            <ToggleButton label="Rascunho" isActive={activeButton === 'Rascunho'} onClick={() => handleClick('Rascunho')} />
        </div>
    );
};

export default FilterButtons;
