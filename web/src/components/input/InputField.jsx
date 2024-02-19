
export default function InputField({ label, containerStyle, ...props }) {

	return (
		<div className={containerStyle + " flex flex-col"}>
			<label htmlFor={props.id} className="font-semibold">{label}</label>
			<input {...props} className="border-primary border h-12 rounded-lg focus:border-2 px-2 select-none outline-none text-gray-800" />
		</div>
	)
}