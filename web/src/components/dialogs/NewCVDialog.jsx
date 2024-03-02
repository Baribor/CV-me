import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import { enqueueSnackbar } from 'notistack';
import * as yup from "yup";
import { useFormik } from 'formik';
import { useNavigate } from 'react-router-dom';

const validationSchema = yup.object({
	title: yup.string().required("Title is required"),
})

export default function NewCVDialog({ handleClose }) {
	const navigate = useNavigate();

	const formik = useFormik({
		validationSchema,
		initialValues: {
			title: '',
		},

		onSubmit: async ({ title }) => {
			navigate("create-cv")
		}
	})


	return (
		<>
			<Dialog open={true} >
				<DialogTitle>New CV</DialogTitle>
				<DialogContent>
					<DialogContentText>
						Enter the title. <br /> <span className='text-xs text-blue-950'>This serves as a way to identify the CV</span>
					</DialogContentText>
					<div className='w-screen max-w-[350px]'></div>
					<TextField
						autoFocus
						margin="dense"
						id="title"
						label="Title"
						fullWidth
						variant="standard"
						onChange={formik.handleChange}
						value={formik.values.title}
						error={formik.touched.title && Boolean(formik.errors.title)}
						helperText={formik.touched.title && formik.errors.title}
					/>
				</DialogContent>
				<DialogActions>
					<Button onClick={() => handleClose()}>Cancel</Button>
					<Button onClick={formik.handleSubmit}>Confirm</Button>
				</DialogActions>
			</Dialog>
		</>
	);
}
