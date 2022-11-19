class Program
{
    //struct for flower list
    //struct as "CharStruct"
    struct CharStruct
    {
        public char c;
    }

    //main program running
    static void Main(string[] args)
    {

        //passing struct CharStruct onto the class "CircularLinkedList" with type as Struct "CharStruct"
        //this creates the object "list" that can be used with that class
        CircularLinkedList<CharStruct> list = new CircularLinkedList<CharStruct>();

        //Program loop
        while (true)
        {
            //get newline separated char input
            string input = Console.ReadLine();
            char charInput = input[0];

            //check the number of flowers
            int length = list.GetLength();

            //dealing with G and R inputs
            if (charInput == 'G' && length >= 1 && (list.Get(length - 1).c == 'G' || list.Get(0).c == 'G'))
            {
                // If last 3 are GGG
                // it's reasonable to check when there are at least 3 characters
                // when "G" is inputted, the condition is false
                if (length >= 3 && list.Get(length - 2).c == 'G' && list.Get(length - 3).c == 'G')
                {
                    Console.WriteLine("Invalid pattern.");
                }
                // If 1st, 2nd, are GG, and the 3rd isn't G (i.e. GGAG G --> INVALID!)
                // single case
                // "G" input is invalid by circular list condition
                else if (length >= 4 && list.Get(0).c == 'G' && list.Get(1).c == 'G' && list.Get(2).c == 'G' && list.Get(3).c != 'G')
                {
                    Console.WriteLine("Invalid pattern.");
                }
                // If 1st and 2 last are GG and the 2nd isn't G (i.e. GAGG G --> INVALID!)
                // "G" input is invalid by circular list condition
                else if (length >= 4 && list.Get(0).c == 'G' && list.Get(length - 3).c != 'G' && list.Get(length - 2).c == 'G')
                {
                    Console.WriteLine("Invalid pattern.");
                }
                // when there is no incorrect underlying conditions
                // adds "G"
                else
                {
                    list.Add(new CharStruct() { c = 'G' });
                }
                // debug
                // Console.WriteLine("First condition executed.");
                continue;
            }
            //dealing with J and O inputs
            if (charInput == 'J' || charInput == 'G' || charInput == 'O' || charInput == 'R')
            {
                // Since we need to check before R too,
                // If length is 0, then we can't check the element before R
                // this is to check whether the character before R is null
                if (length == 0 && charInput == 'R')
                {
                    Console.WriteLine("Invalid pattern.");
                }
                //check whether if xRy has same value for x and y or not.
                //we need at least 2 characters to compare
                //and when R is currently the head
                else if (length >= 1 && list.Get(length - 1).c == 'R' && list.Get(length - 2).c == charInput)
                {
                    Console.WriteLine("Invalid pattern.");
                }
                else
                {
                    list.Add(new CharStruct() { c = charInput });
                }
                // Console.WriteLine("Second condition executed.");
            }
            else
            {

                for (int i = 0; i < length; i++)
                {
                    Console.Write(list.Get(i).c);
                }
                break;
            }
            // debug
            // Console.Write("Current flower list : ");
            // for (int i = 0; i <= length; i++)
            //     {
            //         Console.Write(list.Get(i).c);
            //     }
            // Console.WriteLine("");
        }
        // debug
        // Console.WriteLine("\nProgram terminated!");
    }
}