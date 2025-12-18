def compress_numbers(arr):
    if not arr:
        return []

    result = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])

    return result


class TestCompressNumbers:
    def test_compress_numbers_basic(self):
        """Базовые тесты"""
        assert compress_numbers([1, 1, 2, 2, 3]) == [1, 2, 3]
        assert compress_numbers([0, 0, 1, 1, 0]) == [0, 1, 0]
        assert compress_numbers([1, 2, 3]) == [1, 2, 3]
        assert compress_numbers([]) == []

    def test_compress_numbers_edge_cases(self):
        """Крайние случаи"""
        assert compress_numbers([1]) == [1]
        assert compress_numbers([1, 1, 1, 1]) == [1]
        assert compress_numbers([1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]

    def test_compress_numbers_negative(self):
        """Отрицательные числа и ноль"""
        assert compress_numbers([-1, -1, 0, 0, 1, 1]) == [-1, 0, 1]
        assert compress_numbers([0, 0, -5, -5, 10]) == [0, -5, 10]

    def test_compress_numbers_float(self):
        """Числа с плавающей точкой"""
        assert compress_numbers([1.5, 1.5, 2.0, 2.0]) == [1.5, 2.0]
        assert compress_numbers([0.1, 0.1, 0.2]) == [0.1, 0.2]

    def test_compress_numbers_mixed_types(self):
        """Разные типы данных (если функция должна работать с любыми comparable типами)"""
        assert compress_numbers(['a', 'a', 'b', 'b']) == ['a', 'b']
        assert compress_numbers([True, True, False, False]) == [True, False]

    def test_compress_numbers_original_not_changed(self):
        """Проверка, что оригинальный массив не изменяется"""
        original = [1, 1, 2, 2, 3]
        result = compress_numbers(original)
        assert original == [1, 1, 2, 2, 3]
        assert result == [1, 2, 3]

    def test_compress_numbers_large_input(self):
        """Большие массивы"""
        arr = [1] * 1000 + [2] * 1000 + [3] * 1000
        expected = [1, 2, 3]
        assert compress_numbers(arr) == expected