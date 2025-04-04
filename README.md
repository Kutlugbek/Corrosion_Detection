# Corrosion_Detection
# **Обнаружение коррозии в видео**

Этот проект предоставляет решение для автоматического обнаружения коррозии на объектах, снятых на видео. Используя алгоритмы обработки изображений, код может выявить признаки коррозии на поверхностях и продемонстрировать это на примере видео.

### **Как это работает**

Процесс обнаружения коррозии основывается на анализе кадров видео и применении фильтров и алгоритмов для выявления изменений на поверхности, которые могут указывать на наличие коррозии. Процесс включает:

1. **Обработка видеоданных**: Код извлекает кадры из видеопотока и преобразует их в формат, пригодный для анализа.
2. **Выявление коррозии**: Используются методы обработки изображений и нейросети для обнаружения характерных признаков коррозии.
3. **Отображение результата**: После анализа, алгоритм показывает результат с пометкой о том, где была обнаружена коррозия.

### **Пример работы**

Ниже приведены два GIF-изображения, демонстрирующие работу алгоритма:
1. **До обработки** - Исходное видео с объектом, на котором может быть коррозия.
2. **После обработки** - Видео с выделенными участками, где была обнаружена коррозия.

![До обработки](GIF/Bridge_Construction_Inspection_simple_compose.gif)
# *До обработки: оригинальный кадр из видео.*

![После обработки](GIF/output_video_with_red_highlight.gif)
# *После обработки: обнаруженные участки коррозии на объекте.*

### **Установка и запуск**

1. **Клонируйте репозиторий**:
   ```bash
   git clone [https://github.com/username/repository-name.git](https://github.com/Kutlugbek/Corrosion_Detection.git)
   cd Corrosion_Detection
   ```

2. **Запустите код**:
   Для анализа видео, просто передайте путь к видеофайлу в командной строке:
   ```bash
   python main.py
   ```

3. **Результат**:
   После выполнения скрипта, вы получите обработанное видео с отмеченными участками коррозии.

### **Используемые технологии**

- **Python** 3.x
- **OpenCV**: для обработки видео и изображений
- **NumPy**: для работы с данными и числовыми операциями
