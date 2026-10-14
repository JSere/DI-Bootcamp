import datetime

class Airline:
    def __init__(self, airline_id, name):
        self.id = airline_id
        self.name = name
        self.planes = []

class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, flight_date, airline=None):
        selected_plane = None
        for plane in self.planes:
            if airline and plane.company != airline:
                continue
            if plane.available_on_date(flight_date, self):
                selected_plane = plane
                break
        
        if not selected_plane:
            return None

        flight = Flight(flight_date, destination, self, selected_plane)
        selected_plane.next_flights.append(flight)
        selected_plane.next_flights.sort(key=lambda f: f.date)

        self.scheduled_departures.append(flight)
        self.scheduled_departures.sort(key=lambda f: f.date)

        destination.scheduled_arrivals.append(flight)
        destination.scheduled_arrivals.sort(key=lambda f: f.date)

        return flight

    def info(self, start_date, end_date):
        print(f"Flights departing from {self.city} between {start_date} and {end_date}:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f" - Flight {flight.id} to {flight.destination.city} on {flight.date}")

class Airplane:
    def __init__(self, airplane_id, current_location, company):
        self.id = airplane_id
        self.current_location = current_location
        self.company = company
        self.next_flights = []
        company.planes.append(self)
        current_location.planes.append(self)

    def fly(self, destination):
        if not self.next_flights:
            return False
        
        next_flight = self.next_flights[0]
        if next_flight.destination != destination:
            return False

        next_flight.take_off()
        next_flight.land()
        self.next_flights.pop(0)
        return True

    def location_on_date(self, date):
        loc = self.current_location
        for flight in self.next_flights:
            if flight.date <= date:
                loc = flight.destination
            else:
                break
        return loc

    def available_on_date(self, date, location):
        if self.current_location != location:
            loc_on_date = self.location_on_date(date)
            if loc_on_date != location:
                return False
        
        for flight in self.next_flights:
            if flight.date == date:
                return False
        return True

class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{date}"

    def take_off(self):
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)

    def land(self):
        self.plane.current_location = self.destination
        if self.plane not in self.destination.planes:
            self.destination.planes.append(self.plane)

jfk = Airport("JFK")
lax = Airport("LAX")

delta = Airline("DL", "Delta Air Lines")
plane1 = Airplane(101, jfk, delta)

flight_date = datetime.date.today() + datetime.timedelta(days=1)
scheduled_flight = jfk.schedule_flight(lax, flight_date, delta)

print(f"Scheduled Flight ID: {scheduled_flight.id}")
jfk.info(flight_date, flight_date)

plane1.fly(lax)
print(f"Plane current location after flight: {plane1.current_location.city}")