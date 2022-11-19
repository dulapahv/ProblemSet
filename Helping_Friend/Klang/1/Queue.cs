class Queue<T> where T : struct
{
    private Node<T> top = null;
    private int length = 0;

    public void Push(T value)
    {
        Node<T> node = new Node<T>(value);
        if(this.top == null)
        {
            this.top = node;
        }
        else
        {
            Node<T> lastNode = this.GetNode(this.length-1);
            lastNode.SetNext(node);
        }
        this.length++;
    }

    public T Pop()
    {
        Node<T> node = this.top;
        this.top = this.top.Next();
        this.length--;
        return node.GetValue();
    }

    public T Get(int index)
    {
        Node<T> ptr = this.GetNode(index);
        return ptr.GetValue();
    }

    public int GetLength()
    {
        return this.length;
    }

    private Node<T> GetNode(int index)
    {
        Node<T> ptr = this.top;
        while(index > 0)
        {
            ptr = ptr.Next();
            index--;
        }
        return ptr;
    }
}