---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Arcane]]", "[[Mythic]]", "[[Wand]]"]
price: "{'gp': 1000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Runelord Xanderghul often crafted *Cyrusian wands* to bolster his access to his favorite illusion spells. All *Cyrusian wands* look different but equally audacious in their coloration, shape, and glittering gemstone adornments.

A *Cyrusian wand* only ever contains an arcane spell with the illusion trait.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You Cast the Spell at the indicated rank. If you spend 1 Mythic Point as part of this activation, resolve the spell's effects at mythic proficiency.

**Activate—Presume Success** `pf2:r`

**Frequency** once per day

**Trigger** You fail the DC 10 flat check when you overcharge the wand

**Effect** You disbelieve your failure, willing the check to success. Spend 1 Mythic Point and reroll the flat check, then resolve the spell's effects at mythic proficiency.

**Craft Requirements** You must be a mythic arcane spellcaster capable of supplying a casting of the spell at the listed rank.

**Source:** `= this.source` (`= this.source-type`)
