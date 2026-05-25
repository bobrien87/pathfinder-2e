---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 660}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This enables armor to collapse into a disguised, portable form.

**Activate**`pf2:3` (concentrate, manipulate)

**Effect** You doff your armor, which folds into another wearable object, such as a bangle or amulet with light Bulk. This wearable object has features that hint at the armor it hides. You aren't wearing the armor while it's in this form, but at the GM's discretion, you can still activate properties that might feasibly come from the wearable item the armor has become. If the armor is in its portable form, you can use this activation to revert it to armor, which you can don in 1 minute.

**Source:** `= this.source` (`= this.source-type`)
