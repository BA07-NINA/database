import Breadcrumbs from '@/components/Breadcrumbs'
import Sidebar from '@/components/Sidebar'
import Navbar from '@/components/Navbar'
import { createRootRoute, createRootRouteWithContext, Outlet } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/router-devtools'
import { QueryClient } from '@tanstack/react-query'

export const Route = createRootRouteWithContext<{
  queryClient: QueryClient
}>()({
  component: RootComponent
})

function RootComponent() {
  return (
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
  )
}