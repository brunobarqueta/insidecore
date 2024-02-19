import InputMask from "react-input-mask";

const MaskInput = ({ type, name, value, onChange, placeholder, mask, className }) => {
    return (
      <InputMask
        mask={mask}
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        className={`appearance-none ${value ? "bg-white border border-blue-900" : "bg-zinc-100 "} rounded-full mx-4 md:mx-0 md:w-full h-12 py-2 px-5 text-gray-700 text-xs leading-tight focus:outline-none ${className}`}
        placeholder={placeholder}
      />
    );
  };
  
  export default MaskInput;
