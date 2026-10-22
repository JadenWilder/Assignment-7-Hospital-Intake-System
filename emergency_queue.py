
class Patient:
    """A patient with a name and an urgency score from 1 to 10."""

    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or isinstance(urgency, bool):
            raise TypeError("Urgency must be an integer.")
        if not 1 <= urgency <= 10:
            raise ValueError("Urgency must be between 1 and 10.")

        self.name = name
        self.urgency = urgency


class MinHeap:
    """A min-heap that serves patients with the lowest urgency score first."""

    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        """Move a patient upward until the heap property is restored."""
        while index > 0:
            parent = (index - 1) // 2

            if self.data[index].urgency >= self.data[parent].urgency:
                break

            self.data[index], self.data[parent] = (
                self.data[parent],
                self.data[index],
            )
            index = parent

    def heapify_down(self, index):
        """Move a patient downward until the heap property is restored."""
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (
                left < size
                and self.data[left].urgency
                < self.data[smallest].urgency
            ):
                smallest = left

            if (
                right < size
                and self.data[right].urgency
                < self.data[smallest].urgency
            ):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index],
            )
            index = smallest

    def insert(self, patient):
        """Add a patient and restore the heap property."""
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be inserted.")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        """Print patients in their current internal heap order."""
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        """Return the highest-priority patient without removing them."""
        if not self.data:
            raise IndexError("Cannot peek at an empty queue.")

        return self.data[0]

    def remove_min(self):
        """Remove and return the highest-priority patient."""
        if not self.data:
            raise IndexError("Cannot remove from an empty queue.")

        if len(self.data) == 1:
            return self.data.pop()

        minimum = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return minimum


if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    next_up = heap.peek()
    print("Next patient:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("Patient served:", served.name)

    heap.print_heap()
