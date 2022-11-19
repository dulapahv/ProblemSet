class CircularLinkedList<T> where T : struct
{
    private Node<T> head = null;
    private int length = 0;

    public void Add(T value)
    {
        Node<T> node = new Node<T>(value);
        node.SetNext(this.head);
        if(this.head == null)
        {
            this.head = node;
            this.head.SetNext(node);
        }
        else
        {
            int index = this.length;
            Node<T> ptr = this.head;
            while(index > 1)
            {
                ptr = ptr.Next();
                index--;
            }
            ptr.SetNext(node);
        }
        this.length++;
    }

    public void Remove(int index)
    {
        if(index == 0)
        {
            Node<T> tailPtr = this.head;
            int tailIndex = this.length - 1;
            while(tailIndex > 0)
            {
                tailPtr = tailPtr.Next();
                tailIndex--;
            }
            tailPtr.SetNext(this.head.Next());

            Node<T> ptr = this.head;
            this.head = this.head.Next();
            ptr.SetNext(null);
        }
        else
        {
            Node<T> previousPtr = this.head;
            while(index > 1)
            {
                previousPtr = previousPtr.Next();
                index--;
            }
            Node<T> ptr = previousPtr.Next();
            previousPtr.SetNext(ptr.Next());
            ptr.SetNext(null);
        }
        this.length--;
    }

    public void Insert(int index, T value)
    {
        Node<T> node = new Node<T>(value);
        if(index == 0)
        {
            Node<T> tailPtr = this.head;
            int tailIndex = this.length - 1;
            while(tailIndex > 0)
            {
                tailPtr = tailPtr.Next();
                tailIndex--;
            }
            tailPtr.SetNext(node);

            node.SetNext(this.head);
            this.head = node;
        }
        else
        {
            Node<T> previousPtr = this.head;
            while(index > 1)
            {
                previousPtr = previousPtr.Next();
                index--;
            }
            node.SetNext(previousPtr.Next());
            previousPtr.SetNext(node);
        }
        this.length++;
    }

    private Node<T> GetNode(int index)
    {
        index %= this.length;
        index += this.length;

        Node<T> ptr = this.head;
        while(index > 0)
        {
            ptr = ptr.Next();
            index--;
        }
        return ptr;
    }

    public T Get(int index)
    {
        return this.GetNode(index).GetValue();
    }

    public void Set(int index, T value)
    {
        Node<T> ptr = this.GetNode(index);
        ptr.SetValue(value);
    }

    public int GetLength()
    {
        return this.length;
    }

    public void Concatenate(CircularLinkedList<T> other)
    {
        for(int i=0; i<other.GetLength(); i++)
        {
            this.Add(other.Get(i));
        }
    }
}