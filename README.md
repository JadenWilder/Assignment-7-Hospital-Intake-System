# Doctor Reporting Tree & Emergency Queue

This assignment simulates a medical management system built using non-linear data structures. Students will implement a custom binary tree to model a doctor reporting structure and a min-heap to manage patient urgency in an emergency room queue. These components provide practice in recursive methods, priority-based operations, and tree traversal techniques.

## Classes

### `DoctorNode` Class
Represents a doctor in the reporting hierarchy.

**Constructor**
```python
DoctorNode(name)
```

**Attributes**
- `name` (str): The doctor’s name.
- `left` (DoctorNode or None): Reference to the left report.
- `right` (DoctorNode or None): Reference to the right report.

### `DoctorTree` Class
Manages the binary tree structure of doctor reports.

**Constructor**
```python
DoctorTree()
```

**Attributes**
- `root` (DoctorNode or None): Reference to the root doctor.

**Methods**
- `insert(parent_name: str, employee_name: str, side: str) -> bool`
  - Adds a new doctor under a specified parent node on the given side.
- `preorder(node: DoctorNode) -> list`
  - Returns a list of doctor names using preorder traversal.
- `inorder(node: DoctorNode) -> list`
  - Returns a list of doctor names using inorder traversal.
- `postorder(node: DoctorNode) -> list`
  - Returns a list of doctor names using postorder traversal.

---

### `Patient` Class
Represents a patient waiting for emergency care.

**Constructor**
```python
Patient(name, urgency)
```

**Attributes**
- `name` (str): The patient’s name.
- `urgency` (int): A score from 1 to 10, where 1 is most urgent.

### `MinHeap` Class
Manages patients using a priority queue based on urgency.

**Constructor**
```python
MinHeap()
```

**Attributes**
- `data` (list): List of Patient instances. Index 0 is the most urgent patient.

**Methods**
- `insert(patient: Patient) -> None`
  - Adds a new patient and reorders the heap.
- `remove_min() -> Patient`
  - Removes and returns the most urgent patient.
- `peek() -> Patient`
  - Returns the most urgent patient without removing.
- `print_heap() -> None`
  - Prints each patient and their urgency level.
  ## Design Memo

A binary tree is appropriate for representing the hospital's doctor reporting structure because it organizes relationships between doctors through parent and child nodes. Each doctor can have a left and right report, making the structure easy to visualize and navigate. The tree also allows the system to search for a parent doctor and insert a new doctor in a specific position.

Preorder, inorder, and postorder traversals are useful for different software engineering tasks. Preorder visits the current node before its children, making it useful for copying a tree or displaying a hierarchy from top to bottom. Inorder visits the left subtree, current node, and right subtree. In a binary search tree, this traversal can return values in sorted order. Postorder visits children before the current node, making it useful for deleting a tree safely or processing dependent tasks before their parent.

A min-heap helps simulate emergency intake because it automatically keeps the patient with the lowest urgency score at the root. Since a score of 1 represents the highest priority, the most urgent patient can be selected efficiently. Inserting and removing patients take O(log n) time, while checking the next patient takes O(1) time. These operations make heaps useful when patients arrive continuously and staff must determine who should be treated next. In a real hospital, clinical staff must determine urgency accurately, and software should support rather than replace professional medical judgment.