---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Light]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (manipulate)

A sparkling candy coating covers a sprite apple. For 10 minutes after consuming a sprite apple, you shed bright light in a @Template[emanation|distance:20] (and dim light for the next 20 feet). While shedding this light, you can't be [[Concealed]] if you're visible, and if you're [[Invisible]], you're concealed instead rather than being undetected. The light matches the vibrant color of the apple's candy coating. Creatures in the bright light are subject to another effect, depending on the type of apple.

Creatures in the bright light feel kind and inviting, taking a –1 item penalty to their Will DC against Diplomacy checks.

**Source:** `= this.source` (`= this.source-type`)
