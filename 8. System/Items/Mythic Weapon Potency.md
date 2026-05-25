---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]", "[[Mythic]]"]
price: "{'gp': 70000}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weapon strikes with peerless accuracy to pierce the defenses of the mightiest monstrosities. Attack rolls with this weapon gain a +4 item bonus, and the weapon can be etched with four property runes.

**Activate—Unerring Blow** `pf2:r` (concentration)

**Trigger** You roll an attack roll to Strike with this weapon and receive a critical failure

**Effect** Spend a Mythic Point and reroll your attack roll with mythic proficiency, taking the higher of the two results.

**Craft Requirements** *Mythic weapon* potency runes can only be crafted, etched, or transferred by a mythic character capable of making a Crafting check at mythic proficiency (such as by having the Artisan's Calling).

**Source:** `= this.source` (`= this.source-type`)
