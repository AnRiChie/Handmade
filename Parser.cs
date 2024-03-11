using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;

namespace числа
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Скопипастите имя файла");
            string path = Console.ReadLine();
            Console.Clear();

            using (StreamReader sr = new StreamReader(path, System.Text.Encoding.Default))
            {
                int num; string line;
                int i = 0;
                List<int> nums = new List<int>();
                while ((line = sr.ReadLine()) != null)
                {
                    line = line.Substring(line.Length - 2);
                    num = int.Parse(line);
                    nums.Add(num);
                    i++;
                }
                i = 0;
                int j = 0;
                int[] amount = new int[101];
                for (; i < 101; i++)
                {
                    foreach (int r in nums)
                    {
                        if (r == i)
                        {
                            j++;
                        }
                    }
                    amount[i] = j;
                    Console.WriteLine(amount[i]); // числа отсюда шли в Excel для визуализации
                    j = 0;
                }
                i = 0;
                while (i < 59)
                {
                    j = j + amount[i];
                    i++;
                }
                double f = Convert.ToDouble(nums.Count);
                double d = Math.Round(j / f * 100, 2); 
                Console.WriteLine(d + "% сдали ниже 59");
                j = 0; i = 59;
                while (i >= 59 && i < 101)
                {
                    j = j + amount[i];
                    i++;
                }
                d = Math.Round(j / f * 100, 2);
                Console.WriteLine(d + "% сдали выше 59");
                int h= nums.Count;
                i = 0;
                double k = Convert.ToDouble(nums.Count) / 3.0;
                int b = Convert.ToInt32(Math.Round(k));
                while (h > b)
                {
                    h = h - amount[i];
                    i++;
                }
                
                Console.WriteLine("Всего было " + nums.Count + " участников");
                Console.WriteLine("Примерно треть (до {0}) от сдавших составляет: " + h, b);
                Console.WriteLine("Получается, проходной балл будет " + i);
            }
        }
    }
}