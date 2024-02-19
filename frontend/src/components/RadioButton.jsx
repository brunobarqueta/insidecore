const RadioButton = ({ name, value, checked, onChange, label }) => {
    return (
      <label className="flex items-center space-x-2 cursor-pointer">
        <input
          type="radio"
          name={name}
          value={value}
          checked={checked}
          onChange={onChange}
          className="h-5 w-5 border border-grey-400 rounded-full appearance-none checked:bg-teal-300 checked:border-blue-900 focus:outline-none cursor-pointer"
        />
        <span className="text-xs text-gray-500">{label}</span>
      </label>
    );
  };
  
  export default RadioButton;