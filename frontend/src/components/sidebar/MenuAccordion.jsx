import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '../ui/accordion';

import { Link } from 'react-router-dom';
import { useState } from 'react';

const MenuAccordion = () => {
    const [openItem, setOpenItem] = useState(null);

    const handleAccordionItemClick = (value) => {
        setOpenItem(openItem === value ? null : value);
    };

    return (
        <Accordion type="single" collapsible className="w-full flex-grow">
            <AccordionItem value="painel">
                <AccordionTrigger className="font-bold" onClick={() => handleAccordionItemClick('painel')} isOpen={openItem === 'painel'}>
                    Painéis
                </AccordionTrigger>
                <AccordionContent>Criar um novo</AccordionContent>
                <AccordionContent>Publicados</AccordionContent>
                <AccordionContent>Rascunhos</AccordionContent>
            </AccordionItem>
            <AccordionItem value="gestao">
                <AccordionTrigger className="font-bold" onClick={() => handleAccordionItemClick('gestao')} isOpen={openItem === 'gestao'}>
                    Gestão
                </AccordionTrigger>
                <AccordionContent>Coisas de gestão</AccordionContent>
            </AccordionItem>
            <Link to="configs">
                <p className="mt-2 font-bold">Configurações</p>
            </Link>
        </Accordion>
    );
};

export default MenuAccordion;
