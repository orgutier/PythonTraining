def category_by_product(names: list[str], categories: list[str]) -> dict:
    return {name: cat for name, cat in zip(names, categories)}


def unique_categories(categories: list[str]) -> set:
    return set(categories)


def products_in_category(names: list[str], categories: list[str], target: str) -> list[str]:
    return [name for name, cat in zip(names, categories) if cat == target]


def category_counts(categories: list[str]) -> dict:
    return {cat: categories.count(cat) for cat in set(categories)}


def product_count(names: list[str]) -> int:
    return len(names)
