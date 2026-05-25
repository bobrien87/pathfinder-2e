---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Air]]", "[[Consumable]]", "[[Magical]]", "[[Mythic]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This glass bottle holds breezes captured from the heart of the Plane of Air. When you inhale the bottle's contents, the air fills your lungs so completely that you no longer need to breathe, at least for a time. While the effect lasts, you also gain a status bonus against inhaled threats, such as inhaled poisons. If you spend 1 Mythic Point when you activate the day's breath, you inhale so deeply that you increase the effect's duration.

You don't need to breathe for 3 days. While the effect lasts, you gain a +2 status bonus to saves against inhaled threats. If you spend 1 Mythic Point, you don't need to breathe for 30 days.

**Source:** `= this.source` (`= this.source-type`)
