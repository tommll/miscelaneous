package main

import (
	"errors"
	"log"
	"math/rand"
	"sync"
	"time"
)

type Floor struct {
	id       int
	building *Building
}

func (f *Floor) ReceiveFromElevator(eId int) {
	log.Printf("Someone arrived at floor %d from elevator %d\n", f.id, eId)
}

func (f *Floor) Request(destId int) {

	for {
		ok := f.building.Request(f.id, destId)

		if ok == nil {
			log.Printf("Floor %d request elevator floor %d successful\n", f.id, destId)
			break
		} else {
			log.Printf("Floor %d request elevator to floor %d failed, re-try after 2s\n", f.id, destId)

			// retry after 2 Millisecond
			time.Sleep(2 * time.Millisecond)
		}
	}

}

type Elevator struct {
	id       int
	building *Building
}

func (e *Elevator) DoWork(sourceFloorId, destFloorId int) {
	// simulate work
	log.Printf("Elevator %d doing work from %d to %d\n", e.id, sourceFloorId, destFloorId)
	time.Sleep(time.Duration(rand.Intn(10) * int(time.Millisecond)))
	e.building.floors[destFloorId].ReceiveFromElevator(e.id)
	log.Printf("Elevator %d done work from %d to %d\n", e.id, sourceFloorId, destFloorId)

	e.building.Lock()
	e.building.availableStt[e.id] = true // render available again
	e.building.Unlock()
}

type Building struct {
	sync.Mutex
	floors       []Floor
	elevators    []Elevator
	availableStt []bool
}

// no lock pre-acquire
// return -1 if no elevator currently available
func (b *Building) findAvailableElevator() int {
	b.Lock()
	defer b.Unlock()

	for i, x := range b.availableStt {
		if x == true {
			b.availableStt[i] = false // mark not available
			return i
		}
	}

	return -1
}

func (b *Building) Request(from, to int) error {
	eIdx := b.findAvailableElevator()

	if eIdx == -1 {
		return errors.New("No elevator available")
	} else {
		go b.elevators[eIdx].DoWork(from, to)
		return nil
	}
}

func main() {
	n := 3
	m := 3

	b := Building{}

	floors := make([]Floor, n)
	elevators := make([]Elevator, m)
	availableStt := make([]bool, m)

	for i := 0; i < n; i++ {
		floors[i] = Floor{
			id:       i,
			building: &b,
		}
	}

	for i := 0; i < m; i++ {
		elevators[i] = Elevator{
			id:       i,
			building: &b,
		}
		availableStt[i] = true
	}

	b.floors = floors
	b.elevators = elevators
	b.availableStt = availableStt
	//log.Printf("%v\n", b.availableStt)

	go b.floors[0].Request(1)
	go b.floors[1].Request(1)
	go b.floors[2].Request(1)
	go b.floors[0].Request(2)

	time.Sleep(2 * time.Second)
}
