import { createFileRoute, Link } from '@tanstack/react-router'

export const Route = createFileRoute('/devices')({
  component: RouteComponent,
})

function RouteComponent() {
  return (
    <div>
      En imaginær tabell: 
    <Link to="/device/deviceDashboard" className="[&.active]:font-bold"> Device 1 </Link>
    </div>
  )
}
