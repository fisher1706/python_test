# https://www.youtube.com/watch?v=GVv7MNo_i2Y&list=PLrzHY9riBq3bu8xnTqukuj_6JpWD8LFB5&index=44
# https://www.youtube.com/watch?v=tM16UeEoI-c&list=PLrzHY9riBq3bu8xnTqukuj_6JpWD8LFB5&index=45


"""
Полезно использовать: [daemon=True], queue, pool executor

Плюсы:
- относительно просто
- быстро
- не умирает из-за одного

Минусы:
- потребление ресурсов
- неуправляемость потоками, какой и когда поток работает и запущен
- проблемы потоков (блокировки, состояние гонки и т. д., GIL - не защищает)
"""
