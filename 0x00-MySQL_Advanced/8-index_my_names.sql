-- creates an index idx_name_first on table names and first letter name

CREATE INDEX idx_name_first
ON name(name(1));
