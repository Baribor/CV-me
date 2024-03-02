import { Link, Navigate, Outlet, useNavigate } from "react-router-dom";
import DashboardIcon from '@mui/icons-material/Dashboard';
import EngineeringIcon from '@mui/icons-material/Engineering';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import Drawer from '@mui/material/Drawer';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { useEffect, useState } from "react";
import NavItem from "../components/navigation/NavItem";
import { useRecoilState, useRecoilValue } from "recoil";
import { user } from "../store";
import { ENDPOINTS, TOKEN_KEY } from "../utils/constants";
import { makeAPIRequest } from "../utils";



const drawerWidth = 240;

export default function DashboardLayout(props) {
	const [currentUser, setCurrentUser] = useRecoilState(user);
	const navigate = useNavigate()
	const { window } = props;
	const [mobileOpen, setMobileOpen] = useState(false);
	const token = localStorage.getItem(TOKEN_KEY);
	console.log(currentUser)
	const handleLogout = () => {
		localStorage.removeItem(TOKEN_KEY)
		setCurrentUser(null);
		navigate("/signin", {
			replace: true
		})
	}

	const handleDrawerToggle = () => {
		setMobileOpen(!mobileOpen);
	};

	/* if (!token) {
		return <Navigate to="/auth/admin/login" replace={true} />;
	} */
	useEffect(() => {
		if (!currentUser && token) {
			makeAPIRequest({
				path: ENDPOINTS.get_profile,
			}).then((data) => {
				if (data.data) {
					setCurrentUser(data.data)
				}
			})
		}
	}, [])

	/* if (!currentUser && !token) {
		return <Navigate to={"/signin"} />
	} */

	const drawer = (
		<div>
			<Toolbar sx={{
				backgroundColor: '#172554'
			}}>
				<div>
					<Link to="/">
						<span className="text-white font-extrabold font-[cursive] text-3xl">CV ME</span>
					</Link>
				</div>
			</Toolbar>

			<Divider />
			<div className="w-full select-none p-3 flex flex-col gap-1">

				<NavItem text="Dashboard" to="" handleClick={handleDrawerToggle}>
					<DashboardIcon />
				</NavItem>


				<NavItem text="My CVs" to="cv" handleClick={handleDrawerToggle}>
					<EngineeringIcon />
				</NavItem>

			</div>
		</div>
	);

	const container = window !== undefined ? () => window().document.body : undefined;

	return (
		<Box sx={{ display: 'grid', gridTemplateColumns: { sm: `${drawerWidth}px 1fr` } }}>
			<CssBaseline />
			<AppBar
				position="fixed"
				sx={{
					width: { sm: `calc(100% - ${drawerWidth}px)` },
					ml: { sm: `${drawerWidth}px` },
				}}
			>
				<Toolbar sx={{
					backgroundColor: '#172554'
				}}>
					<IconButton
						color="inherit"
						aria-label="open drawer"
						edge="start"
						onClick={handleDrawerToggle}
						sx={{ mr: 2, display: { sm: 'none' } }}
					>
						<MenuIcon />
					</IconButton>
					<div className="flex justify-end w-full">
						<button className="bg-red-400 px-2 rounded-full active:scale-[.98]" onClick={handleLogout}>
							Logout
						</button>
					</div>
				</Toolbar>
			</AppBar>
			<Box
				component="nav"
				sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
				aria-label="mailbox folders"
			>
				{/* The implementation can be swapped with js to avoid SEO duplication of links. */}
				<Drawer
					container={container}
					variant="temporary"
					open={mobileOpen}
					onClose={handleDrawerToggle}
					ModalProps={{
						keepMounted: true, // Better open performance on mobile.
					}}
					sx={{
						display: { xs: 'block', sm: 'none' },
						'& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
					}}
				>
					{drawer}
				</Drawer>


				<Drawer
					variant="permanent"
					sx={{
						display: { xs: 'none', sm: 'block' },
						'& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth, border: 'none' },
					}}
					open
				>
					{drawer}
				</Drawer>
			</Box>
			<Box
				component="main"
				sx={{ p: 3, overflowY: "scroll", height: "100vh", width: { sm: `calc(100vw - ${drawerWidth}px)` } }}
			>
				<Toolbar />
				<Outlet />
			</Box>
		</Box>
	);
}