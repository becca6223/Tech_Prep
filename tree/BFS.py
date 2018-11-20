#Pseudo code

def searchRoute(graph, start, end):
    if start == end:
        return True
    
    queue = []
    queue.append(start)
    start.state = State.visiting
        
    while queue != []:
        node = queue.pop(0) #de-queue
            for neighbor in node.neighbors:
                if neighbor.state == State.unvisited:
                    if neighbor == end:
                        return True
                    else:
                        neighbor.state = State.visiting
                        queue.append(neighbor)
            node.state = State.visited
                    
            
