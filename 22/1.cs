string text = System.IO.File.ReadAllText("/Users/carrickbartle/Desktop/input");
string[] numsList = text.Split(new string[] { "\n\n" }, StringSplitOptions.None);
List<int> sums = new List<int>();
foreach (string numStr in numsList)
{
    string[] numStrs = numStr.TrimEnd().Split('\n');
    List<int> curr = numStrs.Select(int.Parse).ToList();
    sums.Add(curr.Sum());
}
sums.Sort((x, y) => y - x);
Console.WriteLine(sums.Take(3).Sum());

//int maxCals = 0;
//string text = System.IO.File.ReadAllText("/Users/carrickbartle/Desktop/input");
//string[] numsList = text.Split(new string[] { "\n\n" }, StringSplitOptions.None);
//foreach (string numStr in numsList)
//{
//    string[] numStrs = numStr.TrimEnd().Split('\n');
//    List<int> curr = numStrs.Select(int.Parse).ToList();
//    maxCals = Math.Max(maxCals, curr.Sum());
//}
//Console.WriteLine(maxCals);