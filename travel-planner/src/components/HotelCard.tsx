import { Home, Star, MapPin, DollarSign } from "lucide-react";

export interface Hotel {
  name: string;
  address: string;
  rating: string;
  price: string;
}

export default function HotelCard({ hotel }: Readonly<{ hotel: Hotel }>) {
  return (
    <div className="group flex items-start gap-4 p-4 rounded-xl bg-card hover:bg-card/80 transition-all duration-200 shadow-sm hover:shadow-md">
      <div className="rounded-lg bg-primary/10 p-2 group-hover:scale-110 transition-transform">
        <Home className="w-6 h-6 text-primary" />
      </div>

      <div className="space-y-2 flex-1">
        <div>
          <h3 className="font-semibold text-lg leading-none">{hotel.name}</h3>
          <div className="flex items-center text-muted-foreground mt-1">
            <MapPin className="w-3 h-3 mr-1 flex-shrink-0" />
            <p className="text-sm truncate">{hotel.address}</p>
          </div>
        </div>

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-1">
            <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
            <span className="text-sm font-medium">{hotel.rating}</span>
          </div>

          <div className="flex items-center text-green-600 font-semibold">
            <DollarSign className="w-4 h-4" />
            <span>{hotel.price}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
