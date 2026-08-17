            print("Visitor found:", result.name, result.time, result.purpose)
        else:
            print("Visitor not found.")

    elif choice == 3:
        name = input("Enter visitor name to delete: ")
        root = bst.delete(root, name)
        print("Entry deleted successfully.")

    elif choice == 4:
        print("\nLog Entries in sorted order:")
        bst.inorder(root)

    elif choice == 5:
        print("Total entries:", bst.count(root))

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
