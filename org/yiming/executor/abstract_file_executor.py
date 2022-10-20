from abc import abstractmethod, ABC


class AbstractFileExecutor(ABC):

    def execute(self, input_file_name, output_file_name, **kwargs):
        print("start parsing file " + input_file_name + " and count words " + str(kwargs))
        self.pre_execute()
        analyze_data = self.internal_execute(input_file_name, **kwargs)
        self.output_result(output_file_name, analyze_data)
        print("end parsing file " + input_file_name + " for count words " + str(kwargs))

    @abstractmethod
    def pre_execute(self):
        pass

    @abstractmethod
    def internal_execute(self, input_file_name, **kwargs):
        pass

    @abstractmethod
    def output_result(self, output_file, analyze_data):
        pass
