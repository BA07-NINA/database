import Breadcrumbs from '@/components/Breadcrumbs'
import Sidebar from '@/components/Sidebar'
import Navbar from '@/components/Navbar'
import { createRootRoute, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/router-devtools'

export const Route = createRootRoute({
  component: () => (
    <div className='flex flex-col'>
        <Navbar />
      <div className='flex'>
    
        <Sidebar />
        <div className='flex-1'>
        <Breadcrumbs />
        <Outlet />
        </div>
      </div>
    </div>
  ),
})