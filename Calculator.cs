namespace Project
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    double result = 0.0;

                    Console.WriteLine("Введите первое значение\n");
                    double var1 = Convert.ToDouble(Console.ReadLine());

                    Console.WriteLine("Введите действие (+ ; - ; * ; / ; ^ ; v = sqrt)\n");
                    char act = Convert.ToChar(Console.ReadLine());

                    if (act == 'v')
                    {   
                        if (var1 >= 0)
                        {
                            result = Math.Pow(var1, 0.5);
                        }
                        else
                        {
                            Console.WriteLine("Нет вещественных корней");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Введите второе значение\n");
                        double var2 = Convert.ToDouble(Console.ReadLine());

                        switch (act)
                        {
                            case '+':
                                result = var1 + var2;
                                break;
                            case '-':
                                result = var1 - var2;
                                break;
                            case '*':
                                result = var1 * var2;
                                break;
                            case '^':
                                result = Math.Pow(var1, var2);
                                break;
                            case '/':
                                if (var2 != 0)
                                {
                                    result = var1 / var2;
                                }
                                else
                                {
                                    Console.WriteLine("Ошибка деления на ноль");
                                }
                            break;
                        }        
                    }
                    Console.WriteLine("= " + result + '\n');
                }
                catch (Exception)
                {
                    Console.WriteLine("Не обнаружено распознаваемых символов\nПовторите попытку\n");
                }
            }
        }
    }
}