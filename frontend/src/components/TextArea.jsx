const Textarea = ({ ...props }) => {
  return (
    <textarea
      {...props}
      className={`appearance-none bg-gray-100 border border-gray-300 rounded-2xl resize-none mx-4 md:mx-0 md:w-full h-32 py-5 px-5 text-gray-700 text-md leading-tight focus:outline-none ${props.className}`}
    />
  );
};

export default Textarea;
