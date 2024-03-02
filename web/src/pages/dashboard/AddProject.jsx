import InputField from "../../components/input/InputField";


export default function AddProject() {
	return (
		<div className="grid grid-cols-2 gap-2 gap-y-4">
			<InputField
				containerStyle='col-span-2'
				label="Project Name"
				type="text"
				name="projectName"
			/>
			<InputField
				containerStyle='col-span-2'
				label="Description"
				type="text"
				name="description"
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