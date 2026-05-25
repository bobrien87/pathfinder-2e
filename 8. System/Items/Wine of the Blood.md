---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This wine, prepared using the blood of a creature with overwhelming vitality, soothes the body, mind, and spirit with a temporary sense of euphoria and rest. When you drink wine of the blood, you recover 2d10 healing Hit Points. Additionally, the wine attempts to counteract every negative emotion effect affecting you, with a counteract rank of 3 and a counteract modifier of +9. Lastly, you gain a +1 status bonus to all Will saves and a +2 status bonus against emotion effects for 1 minute.

> [!danger] Effect: Wine of the Blood

**Source:** `= this.source` (`= this.source-type`)
