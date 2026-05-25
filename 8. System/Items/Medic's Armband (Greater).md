---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 900}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You wear this white armband with a bright blue symbol identifying you as a combat medic. You gain a +1 item bonus to Diplomacy checks to change the attitudes of diseased, poisoned, and [[Wounded]] creatures.

You gain a +2 item bonus to Medicine checks to [[Administer First Aid]] and [[Treat Wounds]].

**Activate—Do No Harm** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** An enemy within 30 feet targets you with a Strike or a spell that deals damage

**Effect** Your armband glows, showing that you're here as a medic and not as a combatant. Both you and the triggering enemy take a –8 status penalty to damage rolls until the end of your next turn.

> [!danger] Effect: Do No Harm

**Source:** `= this.source` (`= this.source-type`)
