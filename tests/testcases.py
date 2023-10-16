test_data = [
    {
        'body': {"a": 1, "b": "2.2"},
        'headers': {"hello": "world", "c": "3"}
    },
    {
        'body': {"a": 1, "b": "2.2"},
        'headers': {"hello": "world", "c": "3"}
    },
    {
        'body': {"b": "2.2", "a": 1},
        'headers': {"c": "3", "hello": "world"}
    },
    {
        'body': {"ABC": "123", "z": "6"},
        'headers': {"a": "5", "S": "9"}
    },
    {
        'body': {"a": 1, "h": "600"},
        'headers': {"a": "1", "ABC": "123"}
    }
]

queries = [
    {"a": 1, "b": "2.2"},  # есть только в body
    {"S": "9"},  # есть только в headers
    {"o": "2", "S": "9"},  # "o": "2" нет нигде, "S": "9" есть в headers
    {"ABC": "123"},  # есть и в body, и в headers
    {"u": "0"},  # нет нигде
]

test_data_hash = (
    'b2e5857f28db5467cc742aca343912ed390c3f5452f69a8fd68f4d45bdf5cf21',
    'b2e5857f28db5467cc742aca343912ed390c3f5452f69a8fd68f4d45bdf5cf21',
    'b2e5857f28db5467cc742aca343912ed390c3f5452f69a8fd68f4d45bdf5cf21',
    'c827e3b1368ee2048099d1228cc89d77dcae09e7e5bd3bae13ba40e9f773ab26',
    'c1d855c5e84d949cdc9d7389e3685479819a4520defb6db44d2c617cd1d5099d',
    'e6bd998c6743963d679514834033cfbae2afcabb25e9af7',  # несуществующий
)
