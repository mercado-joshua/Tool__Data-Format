import pprint

class FormatVariable:
    def get_variable(self, var_name, var_value):
        self.__var_name = var_name
        self.__var_value = var_value
        return self

    def create_file(self, specified_path):
        file = open(specified_path, 'w')
        file.write(f'{self.__var_name} = {pprint.pformat(self.__var_value)}\n')
        file.close()

def main():
    test = FormatVariable()
    test.get_variable('cats', [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}])
    test.create_file('testvar.py')

if __name__ == '__main__':
    main()