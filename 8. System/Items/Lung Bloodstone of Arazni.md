---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Artifact]]", "[[Divine]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *Lung Bloodstone of Arazni* represents suffering. While you carry the Lung Bloodstone, you gain the ability to turn your pain into a weapon against your enemies.

**Activate—Strength Through Pain** `pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** You take damage

**Effect** You allow the pain to resonate within you, making you stronger. You gain a +1 status bonus to your next Strike or spell attack before the end of your next turn.

> [!danger] Effect: Strength Through Pain

**Activate—Admonish** `pf2:2` (auditory, emotion, incapacitation, mental)

**Requirements** You worship Arazni or are favored by her

**Frequency** once per day

**Effect** You point your finger at a creature within 60 feet that has wronged you, and you verbally admonish them. The creature takes 1d4 mental damage for every level you have ([[Will]] save against your class DC). On a failed save, the creature is also [[Stunned]] 1 ([[Stunned]] 3 on a critical failure).

**Destruction** To destroy the *Lung Bloodstone*, a worshipper of Arazni must willingly impale themself with the Bloodstone's horned figurehead, dealing themselves @Damage[3d6[piercing], 3d6[persistent,bleed]]{3d6 piercing damage and 3d6 persistent bleed} damage. The *Lung Bloodstone* then evaporates into a cloud of noxious vapors, as [[Toxic Cloud]] (DC 28), that follows the creature that destroyed the *Bloodstone* for its duration.

**Source:** `= this.source` (`= this.source-type`)
