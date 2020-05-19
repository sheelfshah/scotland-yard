from read_graph import get_game
game= get_game()

def taxi_move(a,b,p,g):
    station1=game[a-1]
    station2=game[b-1]
    if p==0:
        if station2.number in station1.taxi_conn:
        	return ticket_checker("t",p,g)
    else:
        if (station2.number in station1.taxi_conn) and not (station2.number in g.moves[1:]):
            return ticket_checker("t",p,g)
    return False

def bus_move(a,b,p,g):
    station1=game[a-1]
    station2=game[b-1]
    if p==0:
        if station2.number in station1.bus_conn:
        	return ticket_checker("b",p,g)
    else:
        if (station2.number in station1.bus_conn) and not (station2.number in g.moves[1:]):
            return ticket_checker("b",p,g)
    return False

def underground_move(a,b,p,g):
    station1=game[a-1]
    station2=game[b-1]
    if p==0:
        if station2.number in station1.underground_conn:
        	return ticket_checker("u",p,g)
    else:
        if (station2.number in station1.underground_conn) and not (station2.number in g.moves[1:]):
            return ticket_checker("u",p,g)
    return False

def blackticket_move(a,b,p,g):
    station1=game[a-1]
    station2=game[b-1]
    if (station2.number in station1.boat_conn) or (station2.number in station1.taxi_conn) or (station2.number in station1.bus_conn) or (station2.number in station1.underground_conn):
    	return ticket_checker("x",p,g)
    return False

def ticket_checker(v1,p,g, v2=None):
    if v2==None:
        if v1=="t":
            return (g.transports[p][0]>0)
        elif v1=="b":
            return (g.transports[p][1]>0)
        elif v1=="u":
            return (g.transports[p][2]>0)
        elif v1=="x":
            return (g.transports[p][3]>0)
    elif v1==v2:
        if v1=="t":
            return (g.transports[p][0]>1)
        elif v1=="b":
            return (g.transports[p][1]>1)
        elif v1=="u":
            return (g.transports[p][2]>1)
        elif v1=="x":
            return (g.transports[p][3]>1)
    else:
        if v1=="t":
            v1n=0
        elif v1=="b":
            v1n=1
        elif v1=="u":
            v1n=2
        elif v1=="x":
            v1n=3
        if v2=="t":
            v2n=0
        elif v2=="b":
            v2n=1
        elif v2=="u":
            v2n=2
        elif v2=="x":
            v2n=3
        return (g.transports[p][v1n]>0 and g.transports[p][v2n]>0)
