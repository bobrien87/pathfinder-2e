---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 220}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Made of elemental salts and essences from the Inner Sphere or where such planes leak onto the Universe, fundamental oil is anathema to elementals and other creatures with a weakness to elemental damage. A weapon anointed with this oil acts as [[Bane Oil]] to elementals, but the damage type is the same as the target's greatest weakness if the target has weakness to acid, cold, electricity, fire, or sonic damage. If it has none of these, the additional damage is the same type as the weapon's damage type. These effects last 1 minute.

**Source:** `= this.source` (`= this.source-type`)
