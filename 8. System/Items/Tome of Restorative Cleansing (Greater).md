---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 3750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This book is dark blue on the night of the new moon, gradually shifting to bright red as the moon waxes.

**Activate** `pf2:f` (concentrate, healing, vitality)

**Frequency** once per day

**Requirements** Your last action was to cast a spell prepared from this grimoire, and the spell removed a harmful condition or affliction from yourself or an ally

**Effect** Choose one creature whose condition was removed by the required spell. Depending on the version, that creature gains 3d8 temporary Hit Points that last for 1 hour.

> [!danger] Effect: Tome of Restorative Cleansing

**Source:** `= this.source` (`= this.source-type`)
