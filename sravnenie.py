import timeit
from b_m import boyer_moore_search, build_shift_table
from kmp import kmp_search, compute_lps
from rk import rabin_karp_search, polynomial_hash




def read_file (filename):
    with open (filename, "r", encoding="cp1251") as f:
        return f.read()

def measure_time(search_functions, text, pattern):
    start_time = timeit.default_timer()
    result  = search_functions(text, pattern)
    execution_time = timeit.default_timer() - start_time
    return result, execution_time

#test_data = text
real_pattern = "Двійковий або логарифмічний"
fake_pattern = "Памагите!!"

text1 = read_file("article_1.txt")
text2 = read_file("article_2.txt")

search_functions = [
    ("Алгоритм Боєра-Мура",  boyer_moore_search),
    ("Алгоритм Кнута-Морріса-Пратта", kmp_search),
    ("Алгоритм Рабіна-Карпа", rabin_karp_search,  
    )  
   
]

patterns = [
    ("Реальний рядок", real_pattern),
    ("Вигаданний рядок", fake_pattern)
]

def compare_search_func(text, search_functions, patterns):
    results = {}
    for pname, pat in patterns:
        print(f"🔎 Пошук: {pname}: {pat}")
        results[pname] = {}
        for name, func in search_functions:
            _, t = measure_time(func, text, pat)
            print(f"{name}: {t:.6f} с")
            results[pname][name] = t
    return results


if __name__ == "__main__":
    print("Порівняння алгоритмів для article_1.txt ")
    results1 = compare_search_func(text1, search_functions, patterns)

    print("Порівняння алгоритмів для article_2.txt")
    results2 = compare_search_func(text2, search_functions, patterns)

