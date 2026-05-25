---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Fire]]", "[[Holy]]", "[[Light]]", "[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 24000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Solidified radiance comprises this slender, featureless wand. It sheds bright light in a 20-foot radius and dim light for the next 20 feet. After you Activate the wand, the light fades, so it only sheds dim light in a 20-foot radius. The wand returns to its original brightness each dawn.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 8th-rank [[Holy Light]], dazzling your target with the beam's intensity. A creature that takes damage from the spell is [[Blinded]] for 1 round and [[Dazzled]] for a number of rounds equal to the spell rank. On a critical success on the attack roll, the target is also blinded for as long as it's dazzled from the spell. However, it can attempt a [[Fortitude]] save saving throw against your spell DC at the end of each of its turns, ending the blinded condition on a success (but remaining dazzled).

**Craft Requirements** Supply a casting of *holy light* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
