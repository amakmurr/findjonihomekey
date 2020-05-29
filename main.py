from chart import Chart
from point import Hash, Dot, Joni, Start
from step import A, B, C

chart = Chart(6, 8, set())
chart.put_point(Hash(0, 0))
chart.put_point(Hash(0, 1))
chart.put_point(Hash(0, 2))
chart.put_point(Hash(0, 3))
chart.put_point(Hash(0, 4))
chart.put_point(Hash(0, 5))
chart.put_point(Hash(1, 0))
chart.put_point(Hash(2, 0))
chart.put_point(Hash(3, 0))
chart.put_point(Hash(4, 0))
chart.put_point(Hash(5, 0))
chart.put_point(Hash(6, 0))
chart.put_point(Hash(7, 0))
chart.put_point(Dot(1, 1))
chart.put_point(Dot(1, 2))
chart.put_point(Dot(1, 3))
chart.put_point(Dot(1, 4))
chart.put_point(Hash(1, 5))
chart.put_point(Hash(2, 1))
chart.put_point(Dot(3, 1))
chart.put_point(Dot(4, 1))
chart.put_point(Dot(5, 1))
chart.put_point(Dot(6, 1))
chart.put_point(Hash(7, 1))
chart.put_point(Dot(2, 2))
chart.put_point(Hash(2, 3))
chart.put_point(Dot(2, 4))
chart.put_point(Hash(2, 5))
chart.put_point(Dot(3, 2))
chart.put_point(Hash(4, 2))
chart.put_point(Dot(5, 2))
chart.put_point(Hash(6, 2))
chart.put_point(Hash(7, 2))
chart.put_point(Hash(3, 3))
chart.put_point(Dot(3, 4))
chart.put_point(Hash(3, 5))
chart.put_point(Hash(4, 3))
chart.put_point(Dot(5, 3))
chart.put_point(Dot(6, 3))
chart.put_point(Hash(7, 3))
chart.put_point(Dot(4, 4))
chart.put_point(Hash(4, 5))
chart.put_point(Dot(5, 4))
chart.put_point(Dot(6, 4))
chart.put_point(Hash(7, 4))
chart.put_point(Hash(5, 5))
chart.put_point(Hash(6, 5))
chart.put_point(Hash(7, 5))
chart.put_point(Hash(6, 6))
chart.put_point(Hash(7, 6))
chart.put_point(Hash(7, 7))
chart.set_join(1, 1)

assert chart.joni

possible_steps = [A(), B(), C()]
possible_points = set()
prevs_taken_steps = []
for step in possible_steps:
    while True:
        taken_steps, through_points, is_key_found = chart.find_possible_steps(step, possible_steps, prevs_taken_steps=prevs_taken_steps)
        prevs_taken_steps.append(taken_steps)
        if is_key_found:
            if through_points[-1] not in possible_points:
                possible_points.add(through_points[-1])
                chart.draw(through_points[-1], Start(chart.joni.x, chart.joni.y), through_points)
                print(f'possible key found at {through_points[-1]}')
                print(f'with taken steps : {" -> ".join([str(s) for s in taken_steps])}')
                print('=' * 50)
        else:
            break
print(f'possible dots {len(possible_points)}')
chart.draw(list(possible_points))
