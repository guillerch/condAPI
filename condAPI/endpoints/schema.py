class SchemaGenerator:
    def __init__(self):
        self.schema = None

    def generate_schema(self, data):
        if isinstance(data, dict):
            return {k: self.generate_schema(v) for k, v in data.items()}
        elif isinstance(data, list):
            if not data:
                return []
            element_schemas = [self.generate_schema(item) for item in data]
            unique_schemas = []
            for schema in element_schemas:
                if schema not in unique_schemas:
                    unique_schemas.append(schema)
            return unique_schemas
        else:
            return type(data).__name__

    def set_schema(self, data):
        self.schema = self.generate_schema(data)

    def get_schema(self):
        return self.schema

    def compare_schema(self, data):
        """
        Compares the current schema with the schema generated from the received JSON.
        Allows the types received in lists to be a subset of the types defined in the schema.
        Returns (True, None) if compatible, (False, error_msg) otherwise.
        """

        def _compare(s1, s2, path="root"):
            if type(s1) != type(s2):
                return (
                    False,
                    f"Different type in '{path}': expected {type(s1).__name__}, received {type(s2).__name__}",
                )
            if isinstance(s1, dict):
                if set(s1.keys()) != set(s2.keys()):
                    missing_key = set(s1.keys()) - set(s2.keys())
                    extras = set(s2.keys()) - set(s1.keys())
                    msg = []
                    if missing_key:
                        msg.append(f"Missing keys in '{path}': {missing_key}")
                    if extras:
                        msg.append(f"Extra keys in '{path}': {extras}")
                    return False, "; ".join(msg)
                for k in s1:
                    ok, err = _compare(s1[k], s2[k], f"{path}.{k}")
                    if not ok:
                        return False, err
                return True, None
            if isinstance(s1, list):
                expected_types = set(map(str, s1))
                received_types = set(map(str, s2))
                if not received_types.issubset(expected_types):
                    return False, (
                        f"Disallowed types in list '{path}': "
                        f"expected {expected_types}, received {received_types}"
                    )
                return True, None
            if s1 != s2:
                return (
                    False,
                    f"Incorrect type in '{path}': expected {s1}, received {s2}",
                )
            return True, None

        return _compare(self.schema, self.generate_schema(data))
