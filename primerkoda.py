from abc import ABCMeta, abstractmethod
#иппортируем из модуля abc, то что нам нужно для создания абстрактного базавого класса
class IOperator(object):
    """
    Интерфейс, который должны реализовать как декоратор,
    так и оборачиваемый объект.
    """
    __metaclass__ = ABCMeta
  """
    Используем абстрактный метод, для которого выше велючили метакласс. Этот метод ОБЯЗАТЕЛЬНО переопределяется 
    и реализуется в наслеуемых классах!
    
   
    """
    @abstractmethod
    def operator(self):
        pass


class Component(IOperator):
    """Компонент программы"""
    def operator(self):
        return 10.0


class Wrapper(IOperator):
    """
    Декоратор
   
    
    """
    def __init__(self, obj):
        self.obj = obj

    def operator(self):
        return self.obj.operator() + 5.0


comp = Component()
comp = Wrapper(comp)
print comp.operator()
# 15.0
