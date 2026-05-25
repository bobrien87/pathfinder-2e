---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 600}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate)

**Requirements** You must have the potion patch affixed to your skin.

A potion patch is a sticky, bandage-like pad that can be filled with one potion and affixed to the skin. Filling the patch and affixing it is a 1-minute activity that takes two hands and has the manipulate trait. A patch has a maximum level of potion it can absorb, depending on the patch's type. When you Activate the patch, the potion affects you without you needing to have the potion in your hand. The patch's magic is negated after it's used, the next time you make your daily preparations, or when another potion patch is affixed to you, whichever comes first.

The potion can be any level.

**Source:** `= this.source` (`= this.source-type`)
