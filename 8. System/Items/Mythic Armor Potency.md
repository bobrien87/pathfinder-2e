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

This armor is etched with a mythical ward providing unparalleled defense. Increase the armor's item bonus to AC by 4, and the armor can be etched with four property runes.

**Activate—Survive Devastation** `pf2:r` (concentration)

**Trigger** An enemy critically succeeds against you with a weapon or unarmed Strike

**Effect** Spend a Mythic Point; if the triggering Strike was made by a mythic creature, it's a normal success instead. If it was made by a non-mythic creature, it's a failure.

**Craft Requirements** *Mythic armor potency* runes can only be crafted, etched, or transferred by a mythic character capable of making a Crafting check at mythic proficiency (such as by having the Artisan's Calling).

**Source:** `= this.source` (`= this.source-type`)
