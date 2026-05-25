---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

When used as catalysts, *chaos falcon feathers* lend flexibility to spells that deal with elemental energy. For the duration of a catalyzed [[Resist Energy]] spell, you can Sustain the Spell on an adjacent target, touching them and changing the type of energy to which they have resistance. This reduces the remaining duration of the spell by 1 minute; if the spell has less than a minute remaining, it reduces the duration to 1 round.

**Source:** `= this.source` (`= this.source-type`)
