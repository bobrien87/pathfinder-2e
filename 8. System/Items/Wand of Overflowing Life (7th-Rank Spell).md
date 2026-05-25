---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Healing]]", "[[Magical]]", "[[Vitality]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 15000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This alabaster wand has a clear crystal at the tip.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Heal]] at 7th-rank.

After you cast the spell, at the start of your next turn, excess healing magic wells up from the wand and heals you, as though you cast the 1-action version of *heal* on yourself at 7th-rank. You gain this benefit only once per turn, even if you cast multiple *heal* spells from *wands of overflowing life* in the same turn.

**Craft Requirements** Supply a casting of *heal* at 7th-rank.

**Source:** `= this.source` (`= this.source-type`)
