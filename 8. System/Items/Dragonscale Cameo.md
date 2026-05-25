---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]", "[[Morph]]", "[[Talisman]]"]
price: "{'gp': 400}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (concentrate)

This ornamental pin, consisting of a single preserved dragon scale from a dragon mounted in a setting of precious metal, is typically affixed between the shoulder blades. When you Activate the pin, a pair of draconic wings matching the color of the scale unfurl from your shoulders, granting you a fly Speed of 50 feet for 5 minutes.

**Craft Requirements** Supply one scale from an adult or older dragon.

**Source:** `= this.source` (`= this.source-type`)
