import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

const SelectField = ({ ...props }) => {
    return (
        <div>
            <div className="mb-2">
                <label>{props.label}</label>
            </div>
            <Select onValueChange={(value) => props.handleSelectChange(props.name, value)} value={props.value}>
                <SelectTrigger className={props.width}>
                    <SelectValue placeholder={props.placeholder}/>
                </SelectTrigger>
                <SelectContent>
                    <SelectGroup>
                        {props.items && props.items.map(item => {
                            return <SelectItem value={item.code} key={item.code}>{item.name}</SelectItem>
                        })}
                    </SelectGroup>
                </SelectContent>
            </Select>
        </div>
    );
};

export default SelectField;
