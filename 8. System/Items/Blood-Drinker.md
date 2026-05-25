---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Twin]]"]
price: "{'gp': 24000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+3 greater striking keen sawtooth saber* has a black blade that always seems freshly smeared with blood.

**Activate—Drink Blood** `pf2:r` (concentrate)

**Trigger** You reduce a creature to 0 Hit Points with the weapon

**Effect** You gain a number of temporary Hit Points equal to twice the creature's level. If you're also wielding Fleshrender in your other hand, you instead gain temporary Hit Points equal to three times the creature's level. These Hit Points remain for 1 minute.

**Activate—Wall of Sabers** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Requirements** Fleshrender is within 30 feet and isn't currently held by you

**Effect** A whirling wall of sawtooth sabers appear in the air between the paired weapons. All creatures in a line between you and Fleshrender take 10d6 slashing damage and 4d6 bleed damage (DC 38 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)
