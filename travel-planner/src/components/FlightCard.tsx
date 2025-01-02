import { Plane, Clock } from 'lucide-react'

export interface Flight {
  name: string
  departure: string
  arrival: string
  price: string
}

export default function FlightCard({ flight }: Readonly<{ flight: Flight }>) {
  return (
    <div className="group flex items-start gap-4 p-4 rounded-xl bg-card hover:bg-card/80 transition-all duration-200 shadow-sm hover:shadow-md m-1">
      <div className="rounded-lg bg-primary/10 p-2 group-hover:scale-110 transition-transform">
        <Plane className="w-6 h-6 text-primary" />
      </div>

      <div className="space-y-2 flex-1">
        <div>
          <h3 className="font-semibold text-lg leading-none">{flight.name}</h3>
          <div className="flex items-center text-muted-foreground mt-1">
            <Clock className="w-3 h-3 mr-1" />
          </div>
        </div>

        <div className="flex  justify-between flex-col">
          <div className="flex items-center gap-2">
            <div className="flex items-center">
              <span className="text-sm font-medium">{flight.departure}</span>
              <span className="mx-2 text-muted-foreground">→</span>
              <span className="text-sm font-medium">{flight.arrival}</span>
            </div>
          </div>

          <div className=" text-green-600 font-semibold block">
            <span>{flight.price}</span>
          </div>
        </div>
      </div>
    </div>
  )
}
