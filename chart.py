from typing import Set, List, Any

from point import Point, Joni, Dot
from step import Step, C, B, A


class Chart:

    joni = None

    def __init__(self, h: int, w: int, points: Set[Point]):
        self.h = h
        self.w = w
        self.points = points

    def put_point(self, point: Point):
        if point in self.points:
            self.points.remove(point)
        self.points.add(point)

    def set_join(self, x, y):
        self.joni = Joni(x, y)

    def can_move_joni(self, step: Step, start_point: Point = None):
        if start_point is None:
            start_point = self.joni
        joni = Joni(start_point.x + step.x, start_point.y + step.y)
        if joni in self.points:
            if isinstance(self.get_point(joni.x, joni.y), Dot):
                return joni
        return False

    def move_joni(self, step: Step):
        joni = self.can_move_joni(step, self.joni)
        if joni:
            self.joni = joni
        return joni

    def find_possible_points(self, possible_steps: List[Step], possible_points=None, start_point: Point = None):
        if possible_points is None:
            possible_points = []

        for step in possible_steps:
            steps = []
            joni = self.can_move_joni(step, start_point)
            if joni:
                steps.append(step)
                possible_points.append(joni)
                possible_points.extend(self.find_possible_points(possible_steps, possible_points, joni))
        return possible_points

    def find_possible_steps(
            self,
            start_step,
            possible_steps: List[Step],
            taken_steps: List[Step] = None,
            start_point: Point = None,
            through_points: List[Point] = None,
            prevs_taken_steps: List[List[Step]] = None,
            is_recursive_step=False
    ):
        if taken_steps is None:
            taken_steps = []
        if through_points is None:
            through_points = []
        if prevs_taken_steps is None:
            prevs_taken_steps = []
        joni = self.can_move_joni(start_step, start_point)
        if joni and joni not in through_points:
            taken_steps.append(start_step)
            through_points.append(joni)
            for step in possible_steps:
                if not is_recursive_step:
                    taken_steps = [start_step]
                    through_points = [joni]
                taken_steps, _, _ = self.find_possible_steps(
                    step,
                    possible_steps,
                    taken_steps,
                    joni,
                    through_points,
                    prevs_taken_steps,
                    True
                )
                if self.is_key_found(taken_steps, prevs_taken_steps):
                    break
        return taken_steps, through_points, self.is_key_found(taken_steps, prevs_taken_steps)

    def is_forbidden(self, possible_steps: List[Step], start_point: Point = None):
        if start_point is None:
            start_point = self.joni
        for step in possible_steps:
            if self.can_move_joni(step, start_point):
                return False
        return True

    def is_next_step_is_prev_taken_steps(self, taken_steps: List[Step], prevs_taken_steps: List[List[Step]]):
        for prev_taken_steps in prevs_taken_steps:
            if taken_steps == prev_taken_steps:
                return True
        return False

    def is_key_found(self, taken_steps: List[Step], prevs_taken_steps: List[List[Step]]):
        required_steps = [A(), B(), C()]
        is_key_found = all(step in taken_steps for step in required_steps)
        if is_key_found:
            for prev_taken_steps in prevs_taken_steps:
                if taken_steps == prev_taken_steps:
                    return False
        return is_key_found

    def get_point_list(self):
        return list(self.points)

    def get_point(self, x, y):
        point = Point(x, y)
        if point in self.points:
            point_list = self.get_point_list()
            return point_list[point_list.index(point)]
        return point

    def draw(self, jonis=None, start_point: Point = None, through_points: List[Point] = None):
        if jonis is None:
            jonis = self.joni
        if not isinstance(jonis, list):
            jonis = [jonis]
        if through_points is None:
            through_points = []
        renders = []
        render = ' \t'
        for i in range(0, self.w):
            render += f'{i}\t'
        renders.append(render)
        for y in range(0, self.h):
            render = f'{y}\t'
            for x in range(0, self.w):
                point = self.get_point(x, y)
                if point in jonis and isinstance(point, Dot):
                    render += f'{jonis[jonis.index(point)].label}\t'
                elif point in through_points:
                    render += f'{through_points.index(point) + 1}\t'
                elif start_point and point == start_point:
                    render += f'{start_point.label}\t'
                else:
                    render += f'{point.label}\t'
            renders.append(render)
        renders.reverse()
        for render in renders:
            print(render)
