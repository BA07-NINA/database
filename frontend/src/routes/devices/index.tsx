import { devicesQueryOptions } from '@/api/query'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'
import {
  type ColumnDef,
  flexRender,
  getCoreRowModel,
  getSortedRowModel,
  type SortingState,
  useReactTable,
} from "@tanstack/react-table"
import { Device } from '@/types'
import { useSuspenseQuery } from '@tanstack/react-query'
import { createFileRoute, Link } from '@tanstack/react-router'

export const Route = createFileRoute('/devices/')({
  loader: async ({ context: { queryClient } }) =>  await queryClient.prefetchQuery(devicesQueryOptions),
  component: RouteComponent,
})

function RouteComponent() {
  const { data: devices } = useSuspenseQuery(devicesQueryOptions)

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead className="w-[100px]">Device</TableHead>
          <TableHead>Project</TableHead>
          <TableHead>Start Date</TableHead>
          <TableHead>End Date</TableHead>
          <TableHead>Last Upload</TableHead>
          <TableHead>Battery Level</TableHead>
          <TableHead>Folder Size</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {devices.map((device: Device) => (
          <TableRow key={device.id}>
            <TableCell className="font-medium">
              <Link
                to="/devices/$deviceId"
                params={{ deviceId: device.id }}
                className="text-blue-500 hover:underline"
              >
                {device.id}
              </Link>
            </TableCell>
            <TableCell>{device.project}</TableCell>
            <TableCell>{device.startDate}</TableCell>
            <TableCell>{device.endDate}</TableCell>
            <TableCell>{device.lastUpload}</TableCell>
            <TableCell>{device.batteryLevel}%</TableCell>
            <TableCell>{device.folderSize}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}
