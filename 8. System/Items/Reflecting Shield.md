---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 18000}"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This high-grade silver buckler (Hardness 6, HP 24, BT 12) is polished to a mirrorlike sheen. The shield functions as a [[Spellguard Shield]] that can also reflect spells.

**Activate—Reflect Spell** R (concentrate)

**Frequency** once per day

**Trigger** You're targeted by a spell

**Requirements** The *reflecting shield* is raised

**Effect** You attempt to reflect the spell on its caster. The shield attempts to counteract the spell, with a counteract rank of 9th and a counteract modifier of +30. If the spell is successfully counteracted, it's turned back on its caster

**Craft Requirements** The initial raw materials must include at least 2,750 gp of silver.

**Source:** `= this.source` (`= this.source-type`)
