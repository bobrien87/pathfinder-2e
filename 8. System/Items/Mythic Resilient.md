---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]", "[[Mythic]]"]
price: "{'gp': 70000}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Mythic resilient* runes imbue armor with unrivaled protection from a wide array of effects. The armor grants a +4 item bonus to saving throws to the wearer.

**Activate—Defy Obliteration** `pf2:r` (concentration)

**Trigger** You critically fail a saving throw

**Effect** Spend a Mythic Point; if the triggering save was made due to an effect created by a mythic monster, hazard, or other effect, it's a normal failure instead. If the save was made due to an effect that wasn't mythic, it becomes a success.

**Craft Requirements** *Mythic resilient* runes can only be crafted, etched, or transferred by a mythic character capable of making a Crafting check at mythic proficiency (such as by having the Artisan's Calling).

**Source:** `= this.source` (`= this.source-type`)
