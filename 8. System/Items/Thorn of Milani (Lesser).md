---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 12}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You hit a creature with the affixed weapon.

This pure white thorn glows bright with the spirit of justice. When you activate the thorn, you deal an additional 1d4 spirit damage with the holy trait. You then gain weakness 1 to unholy until the end of your next turn.

> [!danger] Effect: Thorn of Milani (Spirit Damage)

> [!danger] Effect: Thorn of Milani (Unholy Weakness)

**Source:** `= this.source` (`= this.source-type`)
