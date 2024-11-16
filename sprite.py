import pygame
from abc import ABC, abstractmethod  # Для создания абстрактного класса

class Sprite(ABC, pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, x_vel, y_vel, x_acc, y_acc) -> None:
        super().__init__()  # Инициализируем базовый класс Sprite
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = x_acc
        self.y_acc = y_acc

    @abstractmethod
    def draw(self, screen):
        """
        Абстрактный метод для отрисовки.
        Он должен быть реализован в наследуемом классе.
        видимо поменяется
        """
        pass

    def apply_force(self, x_force, y_force):
        """
        Метод для применения силы (изменение ускорения).
        """
        self.x_acc += x_force
        self.y_acc += y_force

    def update(self):
        """
        Метод для обновления состояния спрайта (позиции, скорости и ускорения).
        """
        # Обновление скорости на основе ускорения
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc

        # Обновление позиции на основе скорости
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

        # Обновление координат rect для взаимодействия с Pygame
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

