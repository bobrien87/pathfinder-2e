---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]"]
price: "{'gp': 15000}"
usage: "etched-onto-slashing-melee-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Originally created as a means of slaying the legendary jabberwock, *vorpal* weapons prove equally effective against nearly any foe with a head.

**Activate—Snicker-Snack** R (concentrate, death, incapacitation)

**Trigger** You roll a natural 20 on a Strike with the weapon against a creature that has a head, critically succeed, and deal slashing damage.

**Effect** The target must succeed at a DC 37 [[Fortitude]] save or be decapitated. This kills any creature except ones that don't require a head to live. For creatures with multiple heads, this usually kills the creature only if you sever its last head.

**Source:** `= this.source` (`= this.source-type`)
