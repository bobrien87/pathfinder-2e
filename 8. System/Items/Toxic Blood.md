---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]", "[[Poison]]"]
price: "{'gp': 650}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Your blood flows with tetrodotoxin or a similar toxin, poisoning enemies who dare to bite you.

Creatures that damage you with an attack using their mouths (such as a jaws or fang Strike) must attempt a DC 26 [[Fortitude]] save saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Sickened]] 1.
- **Failure** The creature takes 2d6 poison damage and is sickened 1.
- **Critical Failure** The creature takes 4d6 poison damage and is [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
