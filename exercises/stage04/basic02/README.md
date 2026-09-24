# Inventory Category Summary

A store's product catalog arrives as two parallel lists. Given, don't modify:

```python
product_names = ["Widget", "Gadget", "Gizmo", "Widget", "Sprocket"]
product_categories = ["tools", "electronics", "electronics", "tools", "tools"]
```

Implement:

- `category_by_product(names: list[str], categories: list[str]) -> dict` -- `{name: cat for name, cat in zip(names, categories)}` (a **dict comprehension**). Since `"Widget"` appears twice in the data, the resulting dict has only one `"Widget"` key -- later entries silently overwrite earlier ones with the same key, which is exactly what a real dict does.
- `unique_categories(categories: list[str]) -> set` -- `set(categories)`.
- `products_in_category(names: list[str], categories: list[str], target: str) -> list[str]` -- `[name for name, cat in zip(names, categories) if cat == target]` (a **list comprehension** with an `if` filter). Compare its result for `"tools"` against `category_by_product`'s: the list comprehension keeps **every** match (so `"Widget"` appears twice), while the dict comprehension above collapsed the duplicate -- same source data, two different container semantics.
- `category_counts(categories: list[str]) -> dict` -- `{cat: categories.count(cat) for cat in set(categories)}` (another dict comprehension, this time over a `set` to avoid counting each category more than once).
- `product_count(names: list[str]) -> int` -- `len(names)`.

See the Study Reference presentation, Topic 4 (Basic tier), for the theory.
