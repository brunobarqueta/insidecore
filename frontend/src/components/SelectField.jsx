import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

const SelectField = ({ ...props }) => {
    return (
        <div>
            <div className="mb-2">
                <label>{props.label}</label>
            </div>
            <Select onValueChange={(value) => props.handleSelectChange(props.name, value)}>
                <SelectTrigger className={props.width}>
                    <SelectValue placeholder={props.placeholder}/>
                </SelectTrigger>
                <SelectContent>
                    <SelectGroup>
                        {props.items.map(item => {
                            return <SelectItem value={item.value} key={item.value}>{item.text}</SelectItem>
                        })}
                    </SelectGroup>
                </SelectContent>
            </Select>
        </div>
    );
};

export default SelectField;
