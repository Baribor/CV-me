import Box from '@mui/material/Box';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import StepContent from '@mui/material/StepContent';
import { useState } from 'react';
import AddEducation from './AddEducation';
import AddExperience from './AddExperience';
import AddProject from './AddProject';
import AddSkill from './AddSkill';


const steps = ['Education', 'Experience', 'Project', 'Skill'];
export default function CreateCVPage() {
	const [activeStep, setActiveStep] = useState(0);

	const handlePreviousClicked = () => {
		setActiveStep((cur) => {
			if (cur === 0)
				return 0;
			return cur - 1;
		})
	}

	const handleNextClicked = () => {

		setActiveStep((cur) => {
			if (cur === 3)
				return 3;
			return cur + 1;
		})
	}
	return (

		<Box sx={{ width: '100%', height: "100%", position: 'relative' }}>
			<div className='text-end'>
				<button className='bg-primary text-white px-2 pl-4 hover:bg-white hover:text-primary rounded-ss-full border-primary border active:scale-[.98] shadow-md border-e-white' onClick={handlePreviousClicked}>Previous</button>
				<button className='border border-primary rounded-ee-full px-2 pe-4 text-primary active:scale-[.98] shadow-md hover:bg-primary hover:text-white' onClick={handleNextClicked}>Next</button>
			</div>
			<Stepper activeStep={activeStep} orientation='vertical'>
				{steps.map((label) => {
					const stepProps = {};
					const labelProps = {};
					return (
						<Step key={label} {...stepProps}>
							<StepLabel {...labelProps}>{label}</StepLabel>
							<StepContent>
								{
									label === 'Education' ?
										(
											<AddEducation />
										) :
										label === "Experience" ?
											(
												<AddExperience />
											) :
											label === "Project" ?
												(
													<AddProject />
												) :
												(
													<AddSkill />
												)
								}
							</StepContent>
						</Step>
					);
				})}

			</Stepper>
		</Box>

	)
}