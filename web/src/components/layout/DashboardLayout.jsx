import { Navigate, Outlet, useNavigate } from "react-router-dom";
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
import { useState } from "react";
import NavItem from "../navigation/NavItem";


const drawerWidth = 240;

export default function DashboardLayout(props) {
	const navigate = useNavigate()
	const { window } = props;
	const [mobileOpen, setMobileOpen] = useState(false);

	const handleLogout = () => {
		//localStorage.removeItem(ADMIN_KEY)
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

	const drawer = (
		<div>
			<Toolbar />
			<Divider />
			<div className="w-full border-r-2 select-none p-3 flex flex-col gap-1">

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
					backgroundColor: "white",
					color: "black"
				}}
			>
				<Toolbar>
					<IconButton
						color="inherit"
						aria-label="open drawer"
						edge="start"
						onClick={handleDrawerToggle}
						sx={{ mr: 2, display: { sm: 'none' } }}
					>
						<MenuIcon />
					</IconButton>
					<Typography variant="h6" noWrap component="div" sx={{ color: "blue" }}>
						Dashboard
					</Typography>
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
						'& .MuiDrawer-paper': { boxSizing: 'border-box', width: drawerWidth },
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