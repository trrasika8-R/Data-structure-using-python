class JobScheduler:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] > self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = (self.heap[parent_index],self.heap[index], )
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        size = len(self.heap)
        largest = index

        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if (left_child < size and self.heap[left_child][0] > self.heap[largest][0]):
                largest = left_child

            if (right_child < size and self.heap[right_child][0] > self.heap[largest][0]):
                largest = right_child

            if largest != index:
                self.heap[index], self.heap[largest] = (self.heap[largest],self.heap[index],)
                index = largest
            else:
                break

    def insert_job(self, job_name, priority):
        self.heap.append((priority, job_name))
        self._heapify_up(len(self.heap) - 1)
        print(f"\nJob '{job_name}' inserted with Priority {priority}")

    def delete_max_job(self):
        if not self.heap:
            print("\nHeap is empty!")
            return

        if len(self.heap) == 1:
            max_job = self.heap.pop()
        else:
            max_job = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)

        print( f"\nDeleted/Processed Job: '{max_job[1]}' with Priority: {max_job[0]}")

    def peek_max_job(self):
        if not self.heap:
            print("\nHeap is empty!")
            return
        max_job = self.heap[0]
        print(f"\nHighest Priority Job: '{max_job[1]}' with Priority: {max_job[0]}")
    def display_heap(self):
        """d) Display All Jobs in Heap Order"""
        if not self.heap:
            print("\nHeap is empty!")
            return
        print("\nCurrent Jobs in Max-Heap:")
        for index, (priority, job_name) in enumerate(self.heap):
            print(f"Index {index}: Job = {job_name}, Priority = {priority}")
def main():
    scheduler = JobScheduler()
    while True:
        print("\n--- MAX HEAP JOB SCHEDULER ---")
        print("1. Insert Job")
        print("2. Delete Highest Priority Job")
        print("3. Peek Highest Priority Job")
        print("4. Display All Jobs")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            job_name = input("Enter Job Name: ")
            try:
                priority = int(input("Enter Priority (integer): "))
                scheduler.insert_job(job_name, priority)
            except ValueError:
                print("Invalid priority! Please enter an integer.")

        elif choice == "2":
            scheduler.delete_max_job()

        elif choice == "3":
            scheduler.peek_max_job()

        elif choice == "4":
            scheduler.display_heap()

        elif choice == "5":
            print("Program terminated")
            break

        else:
            print("Invalid choice! Enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
