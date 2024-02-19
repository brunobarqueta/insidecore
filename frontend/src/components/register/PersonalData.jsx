import Input from '../Input';
import MaskInput from '../MaskInput';
import profileIcon from '../../assets/profile-icon.svg';

const PersonalData = ({
    fullName,
    setFullName,
    cpf,
    setCpf,
    phone,
    setPhone,
}) => {
    return (
        <>
            <div>
                <div className="inline-flex mt-4 ml-4 mb-4">
                    <img className="mr-2" width="25px" height="25px" src={profileIcon} />
                    <p className="text-blue-900">Dados pessoais</p>
                </div>
                <Input
                    type="text"
                    name="name"
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                    placeholder="Nome completo"
                />
            </div>
            <div className="flex space-x-4 mt-4">
                <div className="w-1/2">
                    <MaskInput
                        mask="999.999.999-99" 
                        type="text"
                        name="cpf"
                        value={cpf}
                        onChange={(e) => setCpf(e.target.value)}
                        placeholder="CPF/CNPJ"
                    />
                </div>
                <div className="w-1/2">
                    <MaskInput
                        mask="(99) 99999-9999"
                        type="text"
                        name="phone"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                        placeholder="Telefone"
                    />
                </div>
            </div>
        </>
    );
};

export default PersonalData;
