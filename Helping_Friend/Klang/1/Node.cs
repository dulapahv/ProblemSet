class Node<T> where T : struct
{
    private T value;
    private Node<T> next = null;

    public Node(T value)
    {
        this.SetValue(value);
    }

    public void SetNext(Node<T> next)
    {
        this.next = next;
    }

    public Node<T> Next()
    {
        return this.next;
    }

    public T GetValue()
    {
        return this.value;
    }

    public void SetValue(T value)
    {
        this.value = value;
    }
}