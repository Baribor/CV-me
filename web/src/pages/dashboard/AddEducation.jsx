import InputField from "../../components/input/InputField";


export default function AddEducation() {
	return (
		<div className="grid grid-cols-2 gap-2 gap-y-4">
			<InputField
				containerStyle='col-span-2'
				label="Institution"
				type="text"
				name="institution"
			/>
			<InputField
				containerStyle='col-span-2'
				label="Degree"
				type="text"
				name="degree"
			/>
			<InputField
				label=""
				type="date"
				name="startdate"
			/>
			<InputField
				label=""
				type="date"
				name="enddate"
			/>
			<div className="col-span-2">
				<button className="font-bold text-primary text-sm hover:shadow-md px-3 py-2 active:scale-[.98]">Add another</button>
			</div>
		</div>
	)
}