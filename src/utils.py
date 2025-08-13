def format_currency(value: float) -> str:
    """Formats currency values in euros."""
    return f"€ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
