import { deviceQueryOptions } from '@/api/query';
import DeviceNav from '@/components/DeviceNav'
import { Device } from '@/types';
import { useSuspenseQuery } from '@tanstack/react-query';
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/devices/$deviceId')({
  loader: async ({ params: { deviceId }, context: { queryClient } }) => {
    await queryClient.prefetchQuery(deviceQueryOptions(deviceId))
    
    return { deviceId }
  },
  component: RouteComponent,
})

function RouteComponent() {
  const { deviceId } = Route.useParams()

  const { data: device } = useSuspenseQuery(deviceQueryOptions(deviceId))

  return (
    <>

      <div>
        <p>{device.id}</p>
      </div>
    </>
  )
}