---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This obsidian ring allows you to partially warp your spells through the Netherworld, allowing them to strike directly at a target's body.

**Activate** `pf2:f` (concentrate, spellshape)

**Effect** If your next action is to Cast a Spell that requires a spell attack roll against Armor Class, choose Fortitude DC or Reflex DC. You make your spell attack roll against that defense instead of AC. If the spell has multiple targets, the choice of DC applies to all of them.

**Source:** `= this.source` (`= this.source-type`)
