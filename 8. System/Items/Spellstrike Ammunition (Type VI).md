---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 600}"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:2` Cast a Spell

Mystic patterns create a magic reservoir within this ammunition. You activate *spellstrike ammunition* by Casting a Spell into the ammunition. The spell must be of a spell rank the ammunition can hold, and the spell must be able to target a creature other than the caster. A creature hit by activated *spellstrike ammunition* is targeted by the spell. If the creature isn't a valid target for the spell, the spell is lost.

The ammunition affects only the target hit, even if the spell would normally affect more than one target. If the spell requires a spell attack roll, use the result of your ranged attack roll with the ammunition to determine the degree of success of the spell. If the spell requires a saving throw, the target attempts the save against your spell DC. Combine the Strike and spell's damage for the purpose of resistances and weaknesses.

The maximum rank of spell the ammunition can hold determines its item level and Price.

Maximum Spell Rank 6th

**Source:** `= this.source` (`= this.source-type`)
