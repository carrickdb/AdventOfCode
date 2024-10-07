/*
A for Rock, B for Paper, and C for Scissors
X for lose, Y for draw, and Z for win
1 for Rock, 2 for Paper, and 3 for Scissors
0 lost, 3 draw, 6 won

beats ->
Rock Paper Scissors

AX -> 0 + 3 = 3
AY -> 3 + 1 = 4
AZ -> 6 + 2 = 8
BX -> 0 + 1 = 1
BY -> 3 + 2 = 5
BZ -> 6 + 3 = 9
CX -> 0 + 2 = 2
CY -> 3 + 3 = 6
CZ -> 6 + 1 = 7

*/

string result = "BXCXAXAYBYCYCZAZBZ";
int total = 0;
using (StreamReader reader = new StreamReader("/Users/carrickbartle/Desktop/input"))
{
    string line;
    while ((line = reader.ReadLine()) != null)
    {
        string throws = line.TrimEnd().Replace(" ", "");
        total += (result.IndexOf(throws) + 2) / 2;
    }
}
Console.WriteLine("hello???");
Console.WriteLine(total);


/*
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
1 for Rock, 2 for Paper, and 3 for Scissors
0 if you lost, 3 if the round was a draw, and 6 if you won

AX -> 1 + 3 = 4
AY -> 2 + 6 = 8
AZ -> 3 + 0 = 3
BX -> 1 + 0 = 1
BY -> 2 + 3 = 5
BZ -> 3 + 6 = 9
CX -> 1 + 6 = 7
CY -> 2 + 0 = 2
CZ -> 3 + 3 = 6

1 2 3 4 5 6 7 8 9
012345678901234567
BXCYAZAXBYCZCXAYBZ
(i+2)/2
*/
//string result = "BXCYAZAXBYCZCXAYBZ";
//int total = 0;
//using (StreamReader reader = new StreamReader("/Users/carrickbartle/Desktop/input"))
//{
//    string line;
//    while ((line = reader.ReadLine()) != null)
//    {
//        string throws = line.TrimEnd().Replace(" ", "");
//        total += (result.IndexOf(throws) + 2)/2;
//    }
//}
//Console.WriteLine(total);
