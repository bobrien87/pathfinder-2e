---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Extradimensional]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When etched, this rune creates an extradimensional space that links to the weapon that wields it. The space can hold up to 1 Bulk but can contain only poisons and magic oils that could be applied to the weapon. Stowing or retrieving an item in the space requires an Interact action, except when using the rune's activation.

**Activate** `pf2:1` (concentrate)

**Requirements** At least one magic oil or poison is stored inside the rune's extradimensional space

**Effect** For 1 minute, you can apply stored oils and poisons to the weapon without needing any hands free. Applying them takes the same number of actions as normal. An oil or poison applied this way pours directly from the extradimensional space onto the weapon, and when it's fully applied, its empty vial is ejected.

**Source:** `= this.source` (`= this.source-type`)
