**Remove lines with multiple values**
```python
data = re.sub(r'\n\s*"(val1|val2|val3)".*', r'', data)
```

**Remove lines starting with a #**
```python
data = re.sub(r'\n.*#.*', r'', data)
```

**Remove a comma**
```python
data = re.sub(r',(\n\s*})', r'\1', data)
```

**Add quotes**
```python
data = re.sub(r'("default_risk": )([^\n]*)', r'\1"\2"', data)
```

**Remove blank lines**
```python
data = re.sub(re.compile(r'\n\s*\n', re.M | re.S), r'\n', data)
```
